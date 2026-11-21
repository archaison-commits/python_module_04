#!/usr/bin/env python3

import sys
import typing


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) <= 1:
        print("Usage: ft_stream_management.py <file>")
    else:
        try:
            text = sys.argv[1]
            print(f"Accessing file '{text}'")
            file: typing.IO[str] = open(text, "r")
            content: str = file.read()
            file.close()
            line_number: int = 1
            file = open(text, "r")
            print("---\n")
            for line in file:
                print(f"[FRAGMENT {line_number:03d}]", line, end="")
                line_number += 1
            file.close()
            transf_content: str = ""
            line_number = 1
            beg_line: int = 1
            for char in content:
                if beg_line == 1:
                    transf_content += (f"[FRAGMENT {line_number:03d}] ")
                    beg_line = 0
                if char == "\n":
                    transf_content += "#\n"
                    line_number += 1
                    beg_line = 1
                else:
                    transf_content += char
            if len(content) > 0 and content[-1] != "\n":
                transf_content += "#"
            print("\n---")
            print(f"File '{text}' closed.\n")
            print("Transform data:")
            print("---\n")
            print(transf_content)
            print("\n---")
            sys.stdout.write("Enter new file name (or empty):")
            sys.stdout.flush()
            new_file: str = sys.stdin.readline()
            if len(new_file) > 0 and new_file[-1] == "\n":
                new_file = new_file[:-1]
            if new_file:
                try:
                    print(f"Saving data to '{new_file}'")
                    dest_file = open(new_file, "w", encoding="utf-8")
                    try:
                        dest_file.write(transf_content)
                    finally:
                        dest_file.close()
                    print(f"Data saved in file '{new_file}'.")
                except OSError as e:
                    sys.stderr.write(f"[STDERR] Error opening file "
                                     f"'{new_file}': {e}\nData not saved.\n")
                    sys.stderr.flush()
            else:
                print("Not saving data.")
        except OSError as e:
            sys.stderr.write(f"[STDERR] Error opening file '{text}': {e}\n")
            sys.stderr.flush()
