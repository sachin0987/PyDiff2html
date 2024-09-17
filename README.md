# PyDiff2Html: File Comparison Tool

`PyDiff2html` is a Python tool designed to compare two text files and generate an HTML report with color-coded differences. This tool supports various types of diffs, making it easy to visualize changes between file versions.

## Features

- Compare two files and generate a diff report in HTML format.
- Supports different types of diffs: `all`, `changes`, `removed`, `added`.
- Easy to use via command-line arguments.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone the repository or download the script file.

   ```bash
   git clone https://github.com/yourusername/PyDiff2html.git
   cd PyDiff2html
   ```

3. (Optional) Set up a virtual environment and install dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

To compare two files and generate an HTML diff report, use the following command:

```bash
python compare_files.py <file1> <file2> [-o <output_file>] [-t <diff_type>]
```

### Arguments

- `<file1>`: Path to the first file.
- `<file2>`: Path to the second file.
- `-o`, `--output` (optional): Path to the output HTML file. Default is `diff.html`.
- `-t`, `--type` (optional): Type of diff to generate. Options are `all`, `changes`, `removed`, `added`. Default is `all`.

### Examples

1. Generate a full diff report:

   ```bash
   python compare_files.py file1.txt file2.txt
   ```

2. Generate a report highlighting changes:

   ```bash
   python compare_files.py file1.txt file2.txt -t changes
   ```

3. Generate a report showing removed lines:

   ```bash
   python compare_files.py file1.txt file2.txt -t removed
   ```

4. Generate a report showing added lines:

   ```bash
   python compare_files.py file1.txt file2.txt -t added
   ```

## Error Handling

- **FileNotFoundError**: Indicates that one or both files could not be found.
- **ValueError**: Raised if an invalid diff type is provided.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.


## Contact

For questions or feedback, please contact vsachin094@gmail.com
