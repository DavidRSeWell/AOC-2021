import numpy as np

def process_input(input_path: str):
    input_nums = []
    games = []
    with open(input_path) as f:
        line1 = f.readline()
        input_nums = [int(i.strip()) for i in line1.split(",")]
        game_num = -1 
        game = []
        while True:
            line = f.readline()
            if not line:
                games.append(game)
                break
            if line == "\n":
                print("New game")
                game_num += 1
                if len(game) == 5:
                    games.append(game)
                else:
                    print("Game < 0")
                    print(game)
                game = []
                continue
            line = [int(i.strip()) for i in line.split()]
            print(line)
            game.append(list(line))
    print("Done processing input")
    games = np.array(games)
    print("Input Nums")
    print(input_nums)
    print("Games")
    print(games.shape)
    return (input_nums,games)

def part1(input_path: str):
    in_nums, games = process_input(input_path)

    winner = -1
    winning_num = -1
    for n_i in in_nums:
        games[np.where(games == n_i)] = -1
        # Check winning boards
        # Check Rows
        game_rows = np.where(games.sum(axis=2) == -5) 
        if len(game_rows[0]) > 0:
            print("We have a winner")
            print(len(game_rows))
            print(game_rows)
            winner = game_rows[0][0]
            winning_num = n_i
            break
        # Check Cols
        game_col = np.where(games.sum(axis=1) == -5) 
        if len(game_col[0]) > 0:
            print("We have a winnerrows")
            print(len(game_col))
            print(game_col)
            winner = game_col[0][0]
            winning_num = n_i
            break
    print("Winning game is")
    print(games[winner])
    tot = games[winner][np.where(games[winner] > -1)].sum()
    print(tot)
    print(winner)
    return tot*winning_num

 
def part2(input_path: str):
    in_nums, games = process_input(input_path)

    winner = -1
    winning_num = -1
    completed_games = [-1 for _ in range(games.shape[0])]
    for n_i in in_nums:
        if sum(completed_games) == 0:
            break
        games[np.where(games == n_i)] = -1
        # Check winning boards
        # Check Rows
        game_rows = np.where(games.sum(axis=2) == -5) 
        print("Game ros")
        print(game_rows)
        if len(game_rows[0]) > 0:
            for res in set(game_rows[0]):
                completed_games[res] = 0
                #games = np.delete(games,winner,0)
                if sum(completed_games) == 0:
                    print("Final game!")
                    print(n_i)
                    winning_num = n_i
                    winner = res
                    break

        # Check Cols
        game_col = np.where(games.sum(axis=1) == -5) 
        if len(game_col[0]) > 0:
            for res in set(game_col[0]):
                completed_games[res] = 0
                if sum(completed_games) == 0:
                    print("Final game!")
                    print(n_i)
                    winning_num = n_i
                    winner = res
                    break



    print("Winning game is")
    print(completed_games)
    print(games[winner])
    tot = games[winner][np.where(games[winner] > -1)].sum()
    print(tot)
    print(winner)
    return tot*winning_num
