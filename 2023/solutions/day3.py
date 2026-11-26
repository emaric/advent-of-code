from utils import Point, print_grid


def part_one(input: str):
    lines = input.strip().split("\n")
    max_col = len(lines[0]) - 1
    p = Point(0,max_col)
    grid = {}

    symbols: [Point] = []
    npoints = []
    nvalues = []

    dcount = 0
    n = 0
    cur_npoints = []
    for line in lines:
        for ch in line[::-1]:
            grid[p] = ch
            if ch.isdigit():
                n += int(ch) * 10 ** dcount
                dcount += 1
                cur_npoints.append(p)
            else:
                if n > 0:
                    nvalues.append(n)
                    npoints.append(cur_npoints)
                    dcount = 0
                    n = 0
                    cur_npoints = []
                if ch != ".":
                    symbols.append(p)

            p = p.W
        p = p.S
        p.col = max_col
    
    ans = 0
    indices = set() 
    for symbol in symbols:
        for i in range(len(npoints)):
            if i not in indices:
                if set(npoints[i]) & set(symbol.adjacent_points):
                    indices.add(i)

    for i in indices:
        ans += nvalues[i]

    return ans


def part_two(input: str):
    lines = input.strip().split("\n")
    max_col = len(lines[0]) - 1
    p = Point(0,max_col)
    grid = {}

    symbols: [Point] = []
    npoints = []
    nvalues = []

    dcount = 0
    n = 0
    cur_npoints = []
    for line in lines:
        for ch in line[::-1]:
            grid[p] = ch
            if ch.isdigit():
                n += int(ch) * 10 ** dcount
                dcount += 1
                cur_npoints.append(p)
            else:
                if n > 0:
                    nvalues.append(n)
                    npoints.append(cur_npoints)
                    dcount = 0
                    n = 0
                    cur_npoints = []
                if ch == "*":
                    symbols.append(p)

            p = p.W
        p = p.S
        p.col = max_col
    
    ans = 0
    for symbol in symbols:
        indices = set() 
        for i in range(len(npoints)):
            if set(npoints[i]) & set(symbol.adjacent_points):
                indices.add(i)

        if len(indices) >= 2:
            prod = 1
            for i in indices:
                prod *= nvalues[i]
            ans += prod

    return ans