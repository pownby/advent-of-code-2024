from readFileLines import readFileLines

def parse(file_name = "input.txt"):
    lines = readFileLines(file_name)
    return [[int(n) for n in line.split(' ')] for line in lines]

# Example usage
if __name__ == "__main__":
    data_sets = parse("input.txt")
    print(data_sets)