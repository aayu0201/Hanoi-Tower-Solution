def hanoi(tile,start,middle,destination):
    if tile == 1:
        print("moving",tile, "from",start, "to", destination)
        return 0
    hanoi(tile-1,start,destination,middle)
    print("moving",tile, "from",start, "to", destination)
    hanoi(tile-1,middle,start,destination)
    return 0
if __name__ =="__main__":
    hanoi(3,"A","B","C")
    
    