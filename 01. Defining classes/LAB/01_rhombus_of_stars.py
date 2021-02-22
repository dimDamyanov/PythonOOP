def draw_line(count, offset):
    print(offset * ' ' + ' '.join(['*'] * count))


def rhombus(n: int):
    for i in range(n):
        draw_line(i + 1, n - i - 1)
    for i in range(n - 2, -1, -1):
        draw_line(i + 1, n - i - 1)


n = int(input())
rhombus(n)
