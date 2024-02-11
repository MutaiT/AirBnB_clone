import os

def find_files(directory, extension):
    """Find all files with a given extension in a directory and its subdirectories."""
    files_found = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                files_found.append(os.path.join(root, file))
    return files_found

def main():
    directory = input("Enter the directory to search: ")
    extension = input("Enter the file extension to search for: ")
    files_found = find_files(directory, extension)
    if files_found:
        print("Files found:")
        for file in files_found:
            print(file)
    else:
        print("No files found with the specified extension.")

if __name__ == "__main__":
    main()
