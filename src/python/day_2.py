

def parse_file(file_path):
    
    lines = [] 
    with open(file_path) as f:
        lines = f.readlines()
    return lines


def part1(file_path):
    
    lines = parse_file(file_path) 

    loc = {
        "h":0,
        "d":0
    }
    
    def update(dict_,command,amount):
        if command == "up":
            dict_["d"] -= amount
        elif command == "down":
            dict_["d"] += amount
        elif command == "forward":
            dict_["h"] += amount
        else:
            raise Exception(f"Unexpected command {command}")
        return dict_

    for idx,line in enumerate(lines):
        command, amount = line.split()
        command, amount = command.strip(), int(amount)
        loc = update(loc,command,amount)
    
    return loc["h"]*loc["d"]
 
def part2(file_path):
    
    lines = parse_file(file_path) 

    loc = {
        "h":0,
        "d":0,
        "aim":0
    }
    
    def update(dict_,command,amount):
        if command == "up":
            dict_["aim"] -= amount
        elif command == "down":
            dict_["aim"] += amount
        elif command == "forward":
            dict_["h"] += amount
            dict_["d"] += dict_["aim"]*amount
        else:
            raise Exception(f"Unexpected command {command}")
        return dict_

    for idx,line in enumerate(lines):
        command, amount = line.split()
        command, amount = command.strip(), int(amount)
        loc = update(loc,command,amount)
    
    return loc["h"]*loc["d"]
       