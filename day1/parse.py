def parse(file_name = "input.txt"):
    try:
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file.readlines()]

        first = []
        second = []
        for line in lines:
            pair = line.split('   ')
            first.append(pair[0])
            second.append(pair[1])

        return first, second
    except FileNotFoundError:
        print("Error: input.txt not found")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    

# Example usage
if __name__ == "__main__":
    # Parse input into useable lists
    data_sets = parse()
    print("Lines with newlines:", data_sets)