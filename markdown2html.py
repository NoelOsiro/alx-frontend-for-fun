#!/usr/bin/python3

"""
Markdown to HTML Converter

Usage: python3 markdown2html.py input.md output.html
"""


import sys
import markdown


def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as md_file:
        markdown_text = md_file.read()
        html_content = markdown.markdown(markdown_text)
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 markdown2html.py input.md output.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
