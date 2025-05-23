import os
import sys

def delete_empty_text_files(directory):
    """
    Deletes small .txt files in the specified directory and returns the count of deleted files.
    A file is considered small if it has a size of less than 100 bytes.
    
    Args:
        directory (str): The path to the directory to scan for text files.
    
    Returns:
        int: Number of small text files deleted.
    """
    deleted_count = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file ends with .txt
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                try:
                    # Check if file size is very small (less than 100 bytes)
                    if os.path.getsize(file_path) < 100:
                        os.remove(file_path)
                        deleted_count += 1
                        print(f"Deleted small file (<100 bytes): {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
    
    return deleted_count

if __name__ == "__main__":
    # Check if a directory is provided as a command-line argument
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        # If no directory is provided, use the directory where the script is located
        directory = os.path.dirname(os.path.abspath(__file__))
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    print(f"Scanning directory: {directory}")
    count = delete_empty_text_files(directory)
    print(f"Total small text files deleted: {count}")
