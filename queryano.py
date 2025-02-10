import argparse
import csv
import json
import os

class Queryano:
    """
    Queryano is a class that generates Google Dork queries based on user-specified parameters.
    """

    def __init__(self):
        self.query = ""  # Initialize an empty query string

    def add_operator(self, operator, value):
        """
        Adds a Google Dork operator to the query if a value is provided.

        :param operator: The Google Dork operator (e.g., "site", "intitle").
        :param value: The value to be used with the operator.
        """
        if value:
            self.query += f"{operator}:{value} "  # Append the operator and value to the query

    def create_dork(self, **kwargs):
        """
        Constructs the Google Dork query based on provided keyword arguments.

        :param kwargs: Dictionary of Google Dork operators and their values.
        :return: The constructed Google Dork query as a string.
        """
        self.query = ""  # Reset query before building a new one

        # Basic operators
        self.add_operator("site", kwargs.get("site"))
        self.add_operator("intitle", kwargs.get("intitle"))
        self.add_operator("inurl", kwargs.get("inurl"))
        self.add_operator("intext", kwargs.get("intext"))
        self.add_operator("filetype", kwargs.get("filetype"))
        self.add_operator("ext", kwargs.get("ext"))
        self.add_operator("link", kwargs.get("link"))

        # Advanced operators
        self.add_operator("cache", kwargs.get("cache"))
        self.add_operator("related", kwargs.get("related"))
        self.add_operator("allintitle", kwargs.get("allintitle"))
        self.add_operator("allinurl", kwargs.get("allinurl"))
        self.add_operator("allintext", kwargs.get("allintext"))

        # Additional keywords
        keywords = kwargs.get("keywords")
        if keywords:
            self.query += f"{keywords} "

        return self.query.strip()  # Return the final constructed query


class ReportGenerator:
    """
    Handles generating reports in different formats (CSV, JSON, HTML, TXT).
    """

    @staticmethod
    def generate_csv(query, filename="dork_query_results.csv"):
        """ Saves the query to a CSV file. """
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Generated Query"])
            writer.writerow([query])

    @staticmethod
    def generate_json(query, filename="dork_query_results.json"):
        """ Saves the query to a JSON file. """
        report_data = {"query": query}
        with open(filename, 'w') as file:
            json.dump(report_data, file, indent=4)

    @staticmethod
    def generate_html(query, filename="dork_query_results.html"):
        """ Saves the query to an HTML file. """
        html_content = f"""
        <html>
        <head><title>Google Dork Query Result</title></head>
        <body>
            <h2>Generated Google Dork Query</h2>
            <table border="1">
                <tr>
                    <th>Query</th>
                </tr>
                <tr>
                    <td>{query}</td>
                </tr>
            </table>
        </body>
        </html>
        """
        with open(filename, 'w') as file:
            file.write(html_content)

    @staticmethod
    def generate_txt(query, filename="dork_query_results.txt"):
        """ Saves the query to a plain text file. """
        with open(filename, 'w') as file:
            file.write(f"Generated Google Dork Query:\n{query}")


def validate_query(dork_query):
    """
    Validates whether a query has been generated.

    :param dork_query: The generated Google Dork query.
    :return: True if valid, False otherwise.
    """
    if not dork_query.strip():
        print("\nError: No valid query parameters provided. Please specify at least one parameter.")
        return False
    return True


def generate_reports(query, outputs):
    """
    Generates reports in the specified output formats.

    :param query: The Google Dork query.
    :param outputs: List of output formats to generate (e.g., ["csv", "json"]).
    """
    report_generator = ReportGenerator()
    for output in outputs:
        if output == "csv":
            report_generator.generate_csv(query)
        elif output == "json":
            report_generator.generate_json(query)
        elif output == "html":
            report_generator.generate_html(query)
        elif output == "txt":
            report_generator.generate_txt(query)


def main():
    """
    Parses command-line arguments and generates Google Dork queries.
    """

    parser = argparse.ArgumentParser(description="Queryano - Google Dork Query Generator")

    # Basic query arguments
    parser.add_argument("--site", type=str, help="[site:] Limit results to a specific domain (e.g., example.com)")
    parser.add_argument("--intitle", type=str, help="[intitle:] Find pages with keywords in the title")
    parser.add_argument("--inurl", type=str, help="[inurl:] Find pages with keywords in the URL")
    parser.add_argument("--intext", type=str, help="[intext:] Find pages with keywords in the body text")
    parser.add_argument("--filetype", type=str, help="[filetype:] Search for specific file types (e.g., pdf, docx)")
    parser.add_argument("--ext", type=str, help="[ext:] Find files with a specific extension")
    parser.add_argument("--link", type=str, help="[link:] Find pages that link to a specific URL")

    # Advanced query arguments
    parser.add_argument("--cache", type=str, help="[cache:] Search for cached versions of a URL")
    parser.add_argument("--related", type=str, help="[related:] Find pages related to a specific URL")
    parser.add_argument("--allintitle", type=str, help="[allintitle:] Find pages with multiple keywords in the title")
    parser.add_argument("--allinurl", type=str, help="[allinurl:] Find pages with multiple keywords in the URL")
    parser.add_argument("--allintext", type=str, help="[allintext:] Find pages with multiple keywords in the body text")

    # Additional options
    parser.add_argument("--keywords", type=str, help="Additional keywords (optional)")
    parser.add_argument("--output", type=str, nargs='+', choices=["csv", "json", "html", "txt"],
                        help="Specify one or more output formats (csv, json, html, txt)")
    parser.add_argument("--batch", type=str, help="Path to a batch file with multiple query configurations (JSON format)")

    args = parser.parse_args()

    if args.batch:
        # Process multiple queries from a batch file
        if not os.path.exists(args.batch):
            print("\nError: Batch file not found.")
            return

        with open(args.batch, 'r') as file:
            queries = json.load(file)
            if not isinstance(queries, list):
                print("\nError: Batch file must contain a list of query configurations.")
                return

            for i, query_config in enumerate(queries, start=1):
                print(f"\nProcessing query {i}/{len(queries)}...")
                queryano = Queryano()
                dork_query = queryano.create_dork(**query_config)

                if not validate_query(dork_query):
                    continue

                print("Generated Query:", dork_query)

                if args.output:
                    generate_reports(dork_query, args.output)

    else:
        # Process a single query from CLI arguments
        queryano = Queryano()
        dork_query = queryano.create_dork(
            site=args.site, intitle=args.intitle, inurl=args.inurl, intext=args.intext,
            filetype=args.filetype, ext=args.ext, link=args.link, cache=args.cache,
            related=args.related, allintitle=args.allintitle, allinurl=args.allinurl,
            allintext=args.allintext, keywords=args.keywords
        )

        if not validate_query(dork_query):
            return

        print("\nGenerated Google Dork Query:")
        print(dork_query)

        if args.output:
            generate_reports(dork_query, args.output)
        else:
            print("\nNo output format specified. Query printed above.")


if __name__ == "__main__":
    main()
