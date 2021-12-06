import argparse

def run(day: int,part: int, test: bool):

    print(f"Running day {day} part {part} as test {test}")

    mod_name = f"src.python.day_{day}"

    mod = __import__(mod_name,fromlist=[f"day_{day}"])

    data_file_name = f"day_{day}" + "_test.txt" if test else f"day_{day}.txt"

    input_path = f"data/{data_file_name}"

    ret = getattr(mod,f"part{part}")(input_path)

    print(f"Result = {ret}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    day = parser.add_argument("day",type = int)
    part = parser.add_argument("part",type= int)
    test = parser.add_argument("test",type= int)
    args = parser.parse_args()

    run(args.day,args.part,args.test)