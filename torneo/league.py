def getGames(teams):
    games = []

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            games.append([teams[i], teams[j]])
            games.append([teams[j], teams[i]])

    return games


if __name__ == '__main__':
    teams = ['A']
    print(getGames(teams))
    print(len(getGames(teams)))
    teams = ['A', 'B']
    print(getGames(teams))
    print(len(getGames(teams)))
    teams = ['A', 'B', 'C']
    print(getGames(teams))
    print(len(getGames(teams)))
    teams = ['A', 'B', 'C', 'D']
    print(getGames(teams))
    print(len(getGames(teams)))
    teams = ['A', 'B', 'C', 'D', 'E']
    print(getGames(teams))
    print(len(getGames(teams)))
    teams = ['A', 'B', 'C', 'D', 'E', 'F']
    print(getGames(teams))
    print(len(getGames(teams)))
    teams = ['A', 'B', 'C', 'D', 'E', 'F']
    print(getGames(teams))
    print(len(getGames(teams)))
