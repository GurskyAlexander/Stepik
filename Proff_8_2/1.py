def traffic(n):
    def rec(m):
        if m < n:
            print('Не парковаться')
            rec(m + 1)

    rec(0)


traffic(7)
