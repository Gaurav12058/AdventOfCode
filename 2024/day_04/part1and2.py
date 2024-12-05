with open("input.txt", "r") as file:
    # Part 1
    total = 0
    puzzle = []
    for line in file:
        row = [letter for letter in line.strip()]
        puzzle.append(row)

    # horizontals and verticals
    for i in range(len(puzzle)-3):
        for j in range(len(puzzle[i])):
            if(puzzle[i][j] == "X" and puzzle[i+1][j] == "M" and puzzle[i+2][j] == "A" and puzzle[i+3][j] == "S"):
                total += 1
            if(puzzle[i][j] == "S" and puzzle[i+1][j] == "A" and puzzle[i+2][j] == "M" and puzzle[i+3][j] == "X"):
                total += 1
            if(puzzle[j][i] == "X" and puzzle[j][i+1] == "M" and puzzle[j][i+2] == "A" and puzzle[j][i+3] == "S"):
                total += 1
            if(puzzle[j][i] == "S" and puzzle[j][i+1] == "A" and puzzle[j][i+2] == "M" and puzzle[j][i+3] == "X"):
                total += 1

    # diagonals
    for i in range(len(puzzle)-3):
        for j in range(len(puzzle[i])-3):
            if(puzzle[i][j] == "X" and puzzle[i+1][j+1] == "M" and puzzle[i+2][j+2] == "A" and puzzle[i+3][j+3] == "S"):
                total += 1
            if(puzzle[i][j] == "S" and puzzle[i+1][j+1] == "A" and puzzle[i+2][j+2] == "M" and puzzle[i+3][j+3] == "X"):
                total += 1
            if(puzzle[i+3][j] == "X" and puzzle[i+2][j+1] == "M" and puzzle[i+1][j+2] == "A" and puzzle[i][j+3] == "S"):
                total += 1
            if(puzzle[i+3][j] == "S" and puzzle[i+2][j+1] == "A" and puzzle[i+1][j+2] == "M" and puzzle[i][j+3] == "X"):
                total += 1

    print("Part 1:", total)


    # Part 2
    total = 0
    for i in range(len(puzzle)-2):
        for j in range(len(puzzle[i])-2):
            if(puzzle[i][j] == "M" and puzzle[i+1][j+1] == "A" and puzzle[i+2][j+2] == "S" and puzzle[i][j+2] == "M" and puzzle[i+2][j] == "S"):
                total += 1
            if(puzzle[i][j] == "M" and puzzle[i+1][j+1] == "A" and puzzle[i+2][j+2] == "S" and puzzle[i][j+2] == "S" and puzzle[i+2][j] == "M"):
                total += 1
            if(puzzle[i][j] == "S" and puzzle[i+1][j+1] == "A" and puzzle[i+2][j+2] == "M" and puzzle[i][j+2] == "M" and puzzle[i+2][j] == "S"):
                total += 1
            if(puzzle[i][j] == "S" and puzzle[i+1][j+1] == "A" and puzzle[i+2][j+2] == "M" and puzzle[i][j+2] == "S" and puzzle[i+2][j] == "M"):
                total += 1

    print("Part 2:", total)
