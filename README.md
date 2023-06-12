# Data Translation Pipeline
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains a set of Python scripts that allow you to convert CSV (Comma-Separated Values) files to different formats such as HTML, JSON, and XML. These scripts provide a convenient way to transform your data and facilitate interoperability with other systems. Whether you need to present your data in a web-friendly format, exchange it with JSON-based APIs, or work with XML-based systems, these tools have got you covered.
## Scripts 
1. **mycsv.py** : This module provides utility functions used by other scripts. It includes functions to read data from a file or standard input and to parse CSV data into headers and data. 
2. **csv2html.py** : This script converts a CSV file to an HTML table. It uses the `mycsv` module to read the CSV file and generate the HTML code for the table. 
3. **csv2json.py** : This script converts a CSV file to a JSON object. It reads the CSV file using the `mycsv` module, and then constructs a JSON object with headers and data. 
4. **csv2xml.py** : This script converts a CSV file to an XML file. It utilizes the `mycsv` module to read the CSV file and generates an XML file with headers and data. 
5. **json2csv.py** : This script converts a JSON object to a CSV file. It uses the `mycsv` module and the `json` module to parse the JSON object and generate a CSV file with headers and data. 
6. **xml2csv.py** : This script converts an XML file to a CSV file. It utilizes the `mycsv` module and the `untangle` library to parse the XML file and generate a CSV file with headers and data.

## Usage

To use these conversion tools, follow these steps: 
1. Make sure you have Python installed on your system (version 3 or above). 
2. Clone this repository to your local machine using the following command:

```bash

$ git clone https://github.com/wangyuhsin/data-translation-pipeline.git
``` 
3. Navigate to the cloned repository's directory:

```bash

$ cd data-translation-pipeline
``` 
4. Place your CSV file in the same directory or provide the path to the file as a command-line argument when running the scripts. 
5. Run the desired script by executing the following command:

```bash

$ python [script_name.py] [path_to_file]
```

Replace `script_name.py` with the name of the script you want to use (`csv2html.py`, `csv2json.py`, `csv2xml.py`, `json2csv.py`, or `xml2csv.py`).<br><br> 
For example:

```bash

$ python xml2csv.py data.xml | python csv2json.py > data.json
```

6. The output will be displayed in the console or saved to a file, depending on the script.
## Dependencies

The following dependencies are required to run these scripts:
- Python (version 3 or above) 
- `untangle` library (for `xml2csv.py`) 
- `mycsv` module (provided in the repository)

You can install the `untangle` library using the following command:

```bash

$ pip install untangle
```

## License

This repository is licensed under the MIT License. You are free to use, modify, and distribute the code for both commercial and non-commercial purposes. See the [LICENSE](https://chat.openai.com/LICENSE)  file for more details.
## Acknowledgments

The `mycsv` module used in these scripts is adapted from the MSDS 692 course materials provided by the University of San Francisco (USFCA-MSDS). Special thanks to the course instructors for the inspiration.
