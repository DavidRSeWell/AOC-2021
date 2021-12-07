import numpy as np

def proc_input(input_path: str, part: int):
    if part == 1:
        points = []
        with open(input_path) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                p1,p2 = line.split("->")
                p_list = [int(e) for e in (p1.split(",") + p2.split(","))]
                points.append(p_list)
        return points

def part1(input_path: str):
    print("Running part1")
    points = proc_input(input_path,1)
    mat = np.array(points)
    max_x = mat[:,[0,2]].max() + 1
    max_y = mat[:,[1,3]].max() + 1
    # Only look at examples where x1 = x2 or y1 = y2
    diff1 = mat[:,0] - mat[:,2]
    diff2 = mat[:,1] - mat[:,3]
    keep1 = list(np.where(diff1 == 0)[0])
    keep2 = list(np.where(diff2 == 0)[0])
    keep = set(keep1 + keep2)
    grid = np.zeros((max_y,max_x))
    print(grid.shape)
    # First Y diffs
    for idx in keep:
        print(idx)
        x = mat[idx][[0,2]]
        x1,x2 = x.min(),x.max()
        y = mat[idx][[1,3]]
        y1,y2 = y.min(),y.max()
        print(f"x{x1} -> x{x2 + 1}")
        print(f"y{y1} -> y{y2 + 1}")
        grid[y1:y2 + 1,x1:x2 + 1] += 1
    print(grid) 
    return len(np.where(grid >= 2)[0])

def part2(input_path: str):
    print("Running part1")
    points = proc_input(input_path,1)
    mat = np.array(points)
    max_x = mat[:,[0,2]].max() + 1
    max_y = mat[:,[1,3]].max() + 1
    # Only look at examples where x1 = x2 or y1 = y2
    grid = np.zeros((max_y,max_x))
    print(grid.shape)
    def proc_diags(p1,p2):
        """
        Get all points that lie on a line
        """
        x1,y1 = p1
        x2,y2 = p2
        points = [(p1)]
        xs = np.sign(x2 - x1)
        ys = np.sign(y2 - y1)
        while True:
            x1 += xs
            y1 += ys
            p = (x1,y1)
            points.append(p)
            if p == p2:
                break
        return points

    # First Y diffs
    for idx in range(mat.shape[0]):
        print(idx)
        x = mat[idx][[0,2]]
        x1,x2 = x.min(),x.max()
        y = mat[idx][[1,3]]
        y1,y2 = y.min(),y.max()
        print(f"x{x1} -> x{x2 + 1}")
        print(f"y{y1} -> y{y2 + 1}")
        if (x1 == x2) or (y1 == y2):
            grid[y1:y2 + 1,x1:x2 + 1] += 1
        else:
            points = proc_diags((x[0],y[0]),(x[1],y[1]))
            for x_i,y_i in points:
                grid[y_i,x_i] += 1

    return len(np.where(grid >= 2)[0])

