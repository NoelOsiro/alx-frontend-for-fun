#!/usr/bin/python3

"""
Basic Markdown to HTML Converter

Usage: python3 markdown2html.py input.md output.html
"""

import sys


def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as md_file:
        markdown_text = md_file.read()
        html_content = parse_markdown(markdown_text)
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)


def parse_markdown(markdown_text):
    lines = markdown_text.split('\n')
    html_lines = []
    in_code_block = False

    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            html_lines.append(line)
        elif in_code_block:
            html_lines.append(line)
        else:
            html_line = parse_markdown_line(line)
            html_lines.append(html_line)

    return '\n'.join(html_lines)


def parse_markdown_line(markdown_line):
    if markdown_line.startswith('#'):
        level = len(markdown_line.split()[0])
        return f'<h{level}>{markdown_line[level+1:]}</h{level}>'
    elif markdown_line.startswith('* '):
        return f'<li>{markdown_line[2:]}</li>'
    elif markdown_line.startswith('1. '):
        return f'<li>{markdown_line[3:]}</li>'
    else:
        return f'<p>{markdown_line}</p>'


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
