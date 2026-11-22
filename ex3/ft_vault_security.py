#!/usr/bin/env python3


def secure_archive(file_name: str, file_content: str = "",
                   action: int = 1) -> tuple[bool, str]:
    if action == 1:
        try:
            with open(file_name, "r") as file:
                content: str = file.read()
                return True, content
        except OSError as e:
            return False, str(e)
    elif action == 2:
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(file_content)
                content_saved: str = "Content successfully written to file"
                return True, content_saved
        except OSError as e:
            return False, str(e)
    return False, "Invalid action"


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("nonexistent.txt"), "\n")
    print("Using 'secure_archive' to read from a innaccessible file:")
    print(secure_archive(
        "/home/archaison/permission_test/innaccessible.txt"
        ), "\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("regular.txt"), "\n")
    success, content = secure_archive("regular.txt")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", content, 2))
