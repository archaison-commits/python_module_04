#!/usr/bin/env python3

import sys
import typing


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) <= 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        try:
            text = sys.argv[1]
            print(f"Accessing file '{text}'")
            file: typing.IO = open(text, "r")
            content: str = file.read()
            file.close()
            line_number: int = 1
            file = open(text, "r")
            print("---\n")
            for line in file:
                print(f"[FRAGMENT {line_number:03d}]", line, end="")
                line_number += 1
            file.close()
            file = open(text, "w")
            line_number: int = 1
            beg_line: int = 1
            for char in content:
                if beg_line == 1:
                    file.write(f"[FRAGMENT {line_number:03d}] ")
                    beg_line = 0
                if char == "\n":
                    file.write("#\n")
                    line_number += 1
                    beg_line = 1
                else:
                    file.write(char)
            print("\n---")
            print(f"File '{text}' closed.\n")
            print("Transform data:")
            file.close()
            file = open(text, "r")
            line_number: int = 1
            print("---\n")
            print(file.read())
            print("\n---")
            file.close()
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{text}': {e}")
        new_file = input("Enter new file name (or empty):")
        try:
            transformed_file = open(text, "r")
            content: str = transformed_file.read()
            transformed_file.close()
            dest_file = open(new_file, "w", encoding="utf-8")
            print(f"Saving data to '{new_file}'")
            dest_file.write(content)
            dest_file.close()
            print(f"Data saved in file '{new_file}'.")
        except OSError as e:
            print("Not saving data")

