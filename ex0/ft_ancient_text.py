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
            line_number: int = 1
            print("---\n")
            for char in file:
                print(f"[FRAGMENT {line_number:03d}]", char, end="")
                line_number += 1
            print("\n---")
            file.close()
            print(f"File '{text}' closed.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{text}': {e}")
