data = [int(x) for x in open("input.txt").readlines()]

ans = 0
old = set([ans])

found = False
iter = 0
while not found:
    for i in data:
      ans += i
      if ans in old:
          print("Part Two:", ans)
          found = True
          print("Number of iterations for part 2: " + str(iter+1))
          break
      else:
        old.add(ans)
    if iter == 0:
        print("Part One:", ans)
    iter += 1