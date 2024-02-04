PDF Renamer for Educational Documents
This Python script provides a convenient and automated way to rename PDF files within a selected directory. It's specifically tailored for educational settings where each PDF document contains a unique 10-digit student ID. The script extracts this ID from the text of the PDF and uses it as the new filename, ensuring a standardized and easily searchable file naming convention.
Features
•	Interactive Directory Selection: Utilize a file dialog to select the directory containing the PDFs to be renamed.
•	Intelligent ID Extraction: Parses each PDF for the first occurrence of a 10-digit numerical ID and uses it as the new file name.
•	File Type Verification: Ensures that the script only processes PDF files, leaving other file formats untouched.
•	Error Handling: Provides feedback if files cannot be renamed due to issues like existing file names or permission errors.
•	Count Summary: Displays the total number of files successfully renamed after the operation.
Prerequisites
Before running this script, ensure that you have the following Python libraries installed:
•	textblob
•	pdfminer.six
•	tkinter
You can install these with the following pip commands:
sh
Copy
pip install textblob
pip install pdfminer.six
Note: tkinter is typically included with Python's standard library. If not, you can install it using your operating system's package manager.
Usage
To use this script:
1.	Clone the repository or download the script to your local machine.
2.	Run the script using Python.
3.	When prompted, select the directory containing the PDF files you wish to rename.
The script will then process each PDF file in the selected directory, search for a 10-digit ID within the document's text, and rename the file accordingly. If no valid ID is found, the file will be skipped to ensure the integrity of your documents.
Contributing
Contributions to enhance this script are welcome! Please feel free to fork this repository and submit pull requests with your proposed changes.

