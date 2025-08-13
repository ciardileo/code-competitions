import bisect

def main():
    n, x = map(int, input().split())
    titans = input()
    p, m, g = map(int, input().split())
    
    sizes = {'P': p, 'M': m, 'G': g}
    walls = []  # sorted list of wall heights
    total_walls = 0
    
    for titan in titans:
        hp = sizes[titan]
        
        # Find the smallest wall >= hp
        idx = bisect.bisect_left(walls, hp)
        
        if idx < len(walls):
            # Use this wall
            wall_height = walls.pop(idx)
            new_height = wall_height - hp
            if new_height > 0:
                bisect.insort(walls, new_height)
        else:
            # Need new wall
            total_walls += 1
            new_height = x - hp
            if new_height > 0:
                bisect.insort(walls, new_height)
    
    print(total_walls)

if __name__ == "__main__":
    main()