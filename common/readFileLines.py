def readFileLines(file_name = "input.txt"):
    try:
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file.readlines()]

        return lines
    except FileNotFoundError:
        print(f"Error: {file_name} not found")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    

if __name__ == "__main__":
    print("Lines:", readFileLines())