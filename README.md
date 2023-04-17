# Infovore

Infovore is an open-source service that can read nearly any data and document format (structured or unstructured) and answer queries about the data in that document. It is designed to be extensible and easy to integrate with various data sources and formats.


## Main Components

1. **Reader**: Reads and parses different data/document formats
2. **Processor**: Processes and structures the parsed data
3. **QueryEngine**: Answers queries using the structured data
4. **API**: Handles user input and output

## TODO
Here are several suggested file types we may cover in the future:
1. Excel (XLSX): Use a library like `openpyxl` to read and extract data from worksheets, rows, and cells, then convert the data into natural language text for the LLM.
2. Word (DOCX): Use a library like `python-docx` to read and extract text and data from paragraphs, tables, and other elements, which can be directly fed to the LLM.
3. PowerPoint (PPTX): Use a library like `python-pptx` to read and extract text and data from slides, shapes, and text boxes, and convert it into a readable format for the LLM.
4. PDF: Use a library like `PyPDF2` or `pdfplumber` to extract text from PDF files, and feed the extracted text to the LLM.
5. CSV: Use Python's built-in `csv` module to read and parse the rows and columns, then convert the tabular data into natural language text for the LLM.
6. JSON: Use Python's built-in `json` module to parse the JSON data, and convert the hierarchical data into natural language text for the LLM.
7. Email (EML, MSG): Use a library like `email.parser` or `msg-extractor` to parse the email file and extract data from headers, body, and attachments, then convert the extracted data into natural language text for the LLM.
8. Text (TXT): Read raw text files, which can be directly fed to the LLM.
9. Markdown (MD): Read the raw text file and use a library like `markdown-it-py` to parse the Markdown syntax, extracting data from specific elements, and convert it into plain text for the LLM.
10. HTML: We may either read the entire HTML DOM and eliminate superfluous characters (i.e. SVGs, class names, etc.). Or use a library like `BeautifulSoup` to parse and navigate the HTML DOM, extracting data from specific elements, and convert it into plain text for the LLM.

## Getting Started

These instructions will help you set up and run the Infovore project on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x
* Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the Infovore repository:

```
git clone https://github.com/yourusername/infovore.git
```

2. Change to the project directory:

```
cd infovore
```

3. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

4. Install the required Python packages:

```
pip install -r requirements.txt
```

5. Run the project:

```
python main.py
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

* Thanks to all the open-source libraries used in this project
* Special thanks to the community for their support and contributions
