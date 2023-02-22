def word_search(grid, word):
    row = len(grid)
    col = len(grid[0])
    word = list(word)
    wordLen = len(word)

    def backtracking(r, c, index):
        if r > row - 1 or c > col - 1 or r < 0 or c < 0 or index > wordLen - 1 or grid[r][c] != word[index]:
            return False

        grid[r][c] = "#"
        # r,c
        directions = [(0, -1),  # left
                      (0, 1),  # right
                      (-1, 0),  # top
                      (1, 0)]  # bottom

        result = False
        for dr, dc in directions:
            result = backtracking(r + dr, c + dc, index + 1)
            if result: break

        grid[r][c] = word[index]
        return result


    for rr in range(row):
        for cc in range(col):
            if backtracking(rr, cc, 0):
                return True
    return False


if __name__ == '__main__':
    print(word_search(
        [["N", "W", "L", "I", "M"], ["V", "I", "L", "Q", "O"], ["O", "L", "A", "T", "O"], ["R", "T", "A", "I", "N"],
         ["O", "I", "T", "N", "C"]], "LATIN"))
    print(word_search(
        [["J", "D", "E", "I", "Y"], ["G", "I", "L", "M", "O"], ["Z", "A", "I", "E", "O"], ["L", "T", "B", "S", "N"],
         ["S", "I", "T", "C", "C"]], "AIM"))
    print(word_search(
        [["L", "S", "T", "I", "M"], ["I", "I", "L", "M", "O"], ["S", "K", "I", "E", "O"], ["P", "T", "A", "S", "J"],
         ["M", "X", "T", "A", "C"]], "GRAB"))
    print(word_search(
        [["C", "S", "S", "A", "M"], ["O", "I", "L", "L", "O"], ["O", "L", "I", "T", "O"], ["R", "T", "A", "S", "N"],
         ["S", "I", "T", "A", "C"]], "SALT"))
    print(word_search(
        [["H", "D", "L", "I", "M"], ["R", "I", "L", "Z", "O"], ["W", "B", "A", "E", "O"], ["H", "U", "K", "V", "N"],
         ["S", "Y", "E", "D", "C"]], "BAKED"))

    inputo = [
        ([['E', 'D', 'X', 'I', 'W'],
          ['P', 'U', 'F', 'M', 'Q'],
          ['I', 'C', 'Q', 'R', 'F'],
          ['M', 'A', 'L', 'C', 'A'],
          ['J', 'T', 'I', 'V', 'E']], "educative"),

        ([['O', 'Y', 'O', 'I'],
          ['B', 'I', 'E', 'M'],
          ['K', 'D', 'Y', 'R'],
          ['M', 'T', 'W', 'I'],
          ['Z', 'I', 'T', 'O']], "DYNAMIC"),

        ([['h', 'e', 'c', 'm', 'l'],
          ['w', 'l', 'i', 'e', 'u'],
          ['a', 'r', 'r', 's', 'n'],
          ['s', 'i', 'i', 'o', 'r']], "WARRIOR"),

        ([['C', 'Q', 'N', 'A'],
          ['P', 'S', 'E', 'I'],
          ['Z', 'A', 'P', 'E'],
          ['J', 'V', 'T', 'K']], "save"),

        ([['A']], "ABC"),

        ([['P', 'S', 'S', 'I', 'W', 'P'],
          ['P', 'Y', 'C', 'A', 'Q', 'T'],
          ['I', 'S', 'H', 'P', 'F', 'Y'],
          ['M', 'T', 'O', 'L', 'O', 'I'],
          ['J', 'I', 'N', 'O', 'G', 'K'],
          ['I', 'M', 'D', 'T', 'Y', 'T']], "PSYCHOLOGY")
    ]
    num = 1

    for i in inputo:
        print(num, ".\tGrid =", sep="")
        for j in range(len(i[0])):
            print("\t\t", i[0][j])
        if i[1] == "":
            print('\n\tWord = ""')
        else:
            print(f"\n\tWord =  {i[1]}")
        search_result = word_search(i[0], i[1])
        if search_result:
            print("\n\tSearch result = Word found")
        else:
            print("\n\tSearch result = Word could not be found")
        num += 1
        print("-" * 100, "\n")

