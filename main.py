# Project #6
# The program determines the smallest number of moves to solve the task
# with tower of Hanoi and illustrates the solution steps.


def hanoi_tower_count(n):
    """
    Function for calculating the smallest number of moves to solve the task.
    :param n: number of rings on the tower
    :return: the smallest number of moves
    """
    if n == 1:
        return 1
    return hanoi_tower_count(n - 1) + hanoi_tower_count(n - 1) + 1


def hanoi_tower_moves(n, tower, second_rod, third_rod):
    """
    Function for illustrating the solution steps.
    :param n: number of rings on the tower
    :param tower: the rod on which the rings were originally located
    :param second_rod: the rod to which the rings are transferred
    :param third_rod: additional rod
    :return: None
    """
    if n == 0:
        return
    hanoi_tower_moves(n - 1, tower, third_rod, second_rod)
    second_rod[1] = [tower[1][0]] + second_rod[1]
    tower[1].remove(tower[1][0])
    print(tower[0], '->', second_rod[0])
    print('RESULT: ', tower[0] + ':' + str(tower[1]), second_rod[0] + ':'
          + str(second_rod[1]), third_rod[0] + ':' + str(third_rod[1]))
    hanoi_tower_moves(n - 1, third_rod, second_rod, tower)


def main():
    n = int(input('Input number of rings on the tower: '))
    print('The smallest number of moves: ', hanoi_tower_count(n))
    hanoi_tower_moves(n, ['First rod', [i for i in range(1, n + 1)]],
                      ['Second rod', []], ['Third rod', []])


if __name__ == '__main__':
    main()
