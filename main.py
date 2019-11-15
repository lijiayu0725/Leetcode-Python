def dfs(nums, deep, cur, res, used):
    if deep == len(nums):
        res.append(cur.copy())
        return
    for i, n in enumerate(nums):
        if used[i]:
            continue
        used[i] = True
        cur.append(n)
        dfs(nums, deep + 1, cur, res, used)
        cur.pop()
        used[i] = False

def permu(nums):
    res = []
    dfs(nums, 0, [], res, [False] * 3)
    return res


if __name__ == '__main__':
    print(permu([1,2,3]))