def towerOfHanoi(n,fromRod,auxRod,toRod):
    if 1 == n:
        print("Move from ",fromRod,"to Rod ",toRod)
        return
    towerOfHanoi(n-1,fromRod,auxRod,toRod)
    print("Move from ",fromRod,"to Rod ",toRod)
    towerOfHanoi(n-1,auxRod,toRod,fromRod)

towerOfHanoi(3,"A","B","C")
