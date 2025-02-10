# Queryano - Google Dork Query Generator

## 🔍 Overview
Queryano is a powerful Python-based **Google Dork Query Generator** that helps security researchers, penetration testers, and digital forensics experts construct advanced Google search queries using Google dork operators. The tool enables users to generate custom search queries and export them in various formats.

## 📌 Features
✅ **Custom Query Builder** - Supports Google dork operators like `site:`, `intitle:`, `inurl:`, `filetype:`, etc.  
✅ **Batch Processing** - Read multiple query configurations from a JSON file and process them in one go.  
✅ **Multiple Output Formats** - Save queries in `CSV`, `JSON`, `HTML`, and `TXT`.  
✅ **Command-Line Interface (CLI)** - Easily generate queries using command-line arguments.  
✅ **Lightweight & Fast** - No unnecessary dependencies, making it easy to run on any system.  

## 🚀 Installation
Ensure you have Python 3 installed. Then, clone the repository and navigate to the project directory:

```sh
# Clone the repository
git clone https://github.com/yourusername/queryano.git
cd queryano

# Run the script
python queryano.py --help
```

## ⚙️ Usage

### **1️⃣ Generating a Single Query**
Run the script with desired parameters. Example:

```sh
python queryano.py --site example.com --intitle "admin login" --filetype pdf --output txt json
```

🔹 **Generated Query Output:**
```
Generated Google Dork Query:
site:example.com intitle:"admin login" filetype:pdf
```
This query will be saved in `dork_query_results.txt` and `dork_query_results.json`.

---

### **2️⃣ Batch Query Processing**
If you have multiple queries, create a **batch JSON file**:

```json
[
    {"site": "example.com", "intitle": "login"},
    {"inurl": "admin", "filetype": "pdf"}
]
```

Run the script:
```sh
python queryano.py --batch queries.json --output csv html
```
Each query will be processed, and results will be stored in **CSV and HTML** formats.

---

### **3️⃣ Available Google Dork Operators**
| Operator       | Description                                      | Example Usage                           |
|--------------|------------------------------------------------|----------------------------------|
| `site:`     | Limit results to a specific domain             | `site:example.com`               |
| `intitle:`  | Find pages with keywords in the title         | `intitle:"login page"`           |
| `inurl:`    | Find pages with keywords in the URL           | `inurl:admin`                    |
| `intext:`   | Find pages with keywords in the body text     | `intext:"confidential"`          |
| `filetype:` | Search for specific file types                | `filetype:pdf`                   |
| `ext:`      | Find files with a specific extension          | `ext:xlsx`                        |
| `link:`     | Find pages linking to a specific URL         | `link:example.com`               |
| `cache:`    | Search for cached versions of a URL          | `cache:example.com`              |
| `related:`  | Find pages related to a specific URL         | `related:example.com`            |
| `allintitle:` | Find pages with multiple keywords in title | `allintitle:"admin dashboard"`   |
| `allinurl:` | Find pages with multiple keywords in URL    | `allinurl:login dashboard`       |
| `allintext:` | Find pages with multiple keywords in text  | `allintext:password recovery`    |

---

## 📄 Output Formats
Queryano supports multiple output formats:
- **TXT**: Plain text file containing the generated query.
- **CSV**: CSV file with query data.
- **JSON**: JSON-formatted output for structured data storage.
- **HTML**: Simple HTML report with query details.

Example command:
```sh
python queryano.py --site example.com --intitle "confidential" --output txt csv
```

---

## 🔥 Examples
### **Basic Query:**
```sh
python queryano.py --site example.com --inurl "admin"
```
🔹 Output:
```
site:example.com inurl:admin
```

### **Advanced Query:**
```sh
python queryano.py --site example.com --intitle "login" --filetype pdf --allintext "password reset"
```
🔹 Output:
```
site:example.com intitle:"login" filetype:pdf allintext:"password reset"
```

### **Batch Queries from JSON:**
```json
[
    {"site": "github.com", "intitle": "API key"},
    {"site": "pastebin.com", "intext": "password"}
]
```
Command:
```sh
python queryano.py --batch queries.json --output json html
```

---

## 🛠️ Future Improvements
🚀 Add API support to fetch search results automatically.  
🚀 Improve error handling for incorrect parameters.  
🚀 Implement a GUI-based version for ease of use.  

---

## 🏆 Contribution
Contributions are welcome! Feel free to submit issues or pull requests. To contribute:
1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Commit changes and push.
4. Open a pull request.

---

## 📜 License
This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.

---

## 📧 Contact
For queries or suggestions, reach out via:
- **GitHub Issues**: [Open an issue](https://github.com/yourusername/queryano/issues)
- **Telegram**: @cometteetcaramel

