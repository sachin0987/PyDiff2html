## **PyDiff: File Comparison Tool**

**Overview**

This Python tool is designed to efficiently compare two text files and generate a detailed HTML report highlighting their differences. It provides a user-friendly interface and offers customizable options for the type of diff to generate.

**Key Features**

* **Flexible Diff Types:** Choose from four diff types:
  - **All:** Shows all differences between the files.
  - **Changes:** Highlights only the modified lines.
  - **Removed:** Displays only the lines that have been removed from the first file.
  - **Added:** Shows only the lines that have been added to the second file.
* **Customizable Output:**
  - **Output File Path:** Specify the desired location for the generated HTML report.
  - **Diff Type:** Select the type of diff that best suits your needs.
* **User-Friendly Interface:**
  - **Command-Line Arguments:** Easily provide input files and output options through the command line.
  - **Clear Output:** The tool provides informative messages about the generated report.

**Usage**

1. **Clone or Download:** Obtain the source code for the tool.
2. **Run the Script:** Execute the Python script from your terminal or command prompt.
3. **Provide Input:** Specify the paths to the two files you want to compare.
4. **Customize Output (Optional):**
   - Use the `-o` flag to specify a different output file path.
   - Use the `-t` flag to choose the desired diff type.

**Example**

```bash
python file_comparator.py file1.txt file2.txt -o my_diff.html -t changes
