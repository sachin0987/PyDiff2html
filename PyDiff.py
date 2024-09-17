import difflib
import os
import argparse

def compare_files(file1_path, file2_path, output_file_path, diff_type):
    """Compares two files and generates an HTML report with color-coded diffs.

    Args:
        file1_path (str): Path to the first file.
        file2_path (str): Path to the second file.
        output_file_path (str): Path to the output HTML file.
        diff_type (str): Type of diff to generate (options: 'all', 'changes', 'removed', 'added').
    """

    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()

            if diff_type == 'all':
                html_diff = difflib.HtmlDiff().make_file(file1_lines, file2_lines, file1_path, file2_path)
            elif diff_type == 'changes':
                html_diff = difflib.HtmlDiff().make_file(file1_lines, file2_lines, file1_path, file2_path, context=True)
            elif diff_type == 'removed':
                html_diff = difflib.HtmlDiff().make_file(file1_lines, file2_lines, file1_path, file2_path, context=True, numlines=0, charjunk=difflib.HtmlDiff.default_charjunk)
            elif diff_type == 'added':
                html_diff = difflib.HtmlDiff().make_file(file1_lines, file2_lines, file1_path, file2_path, context=True, numlines=0, charjunk=difflib.HtmlDiff.default_charjunk, noformat=True)
            else:
                raise ValueError("Invalid diff type. Valid options are 'all', 'changes', 'removed', or 'added'.")

            with open(output_file_path, 'w') as output_file:
                output_file.write(html_diff)

            print(f"Diff report generated: {output_file_path}")

    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two files and generate an HTML diff report.")
    parser.add_argument("file1", help="Path to the first file")
    parser.add_argument("file2", help="Path to the second file")
    parser.add_argument("-o", "--output", default="diff.html", help="Path to the output HTML file (default: diff.html)")
    parser.add_argument("-t", "--type", default="all", choices=["all", "changes", "removed", "added"], help="Type of diff to generate (default: all)")

    args = parser.parse_args()

    compare_files(args.file1, args.file2, args.output, args.type)
