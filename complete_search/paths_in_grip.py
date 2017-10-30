from copy import deepcopy
import time


def out_of_bounds(i, j, n):
    return i < 0 or j < 0 or i >= n or j >= n


def bottom_right_corner(i, j, n):
    return i == n - 1 and j == n - 1


def top_right_corner(i, j):
    return i == 0 and 0


def is_visited(i, j, visited):
    if not out_of_bounds(i, j, len(visited)):
        return visited[i, j]
    else:
        return 0


def search_no_opt(i, j, visited):
    if out_of_bounds(i, j, len(visited)) or visited[i][j]:
        return 0
    elif bottom_right_corner(i, j, len(visited)):
        return 1
    else:
        visited[i][j] = 1
        return search_no_opt(i + 1, j, deepcopy(visited)) + \
            search_no_opt(i - 1, j, deepcopy(visited)) + \
            search_no_opt(i, j + 1, deepcopy(visited)) + \
            search_no_opt(i, j - 1, deepcopy(visited))


def search_opt_1(i, j, visited):
    if out_of_bounds(i, j, len(visited)) or visited[i][j]:
        return 0
    elif bottom_right_corner(i, j, len(visited)):
        return 1
    else:
        visited[i][j] = 1

        # For the first step either go down or right. I've chose down
        # This is because routes around the diagonal are symmetric
        # Notice how the final solution is multiplied by 2
        if i == 0 and j == 0:
            return search_opt_1(i + 1, j, deepcopy(visited))

        return search_opt_1(i + 1, j, deepcopy(visited)) + \
            search_opt_1(i - 1, j, deepcopy(visited)) + \
            search_opt_1(i, j + 1, deepcopy(visited)) + \
            search_opt_1(i, j - 1, deepcopy(visited))


# Checks if the forward square has already been visited and
# both the left and right squares are not visited.
# This results in a grid split and the bottom right corner
# can never be reached
def cannot_reach_bottom_right(i, j, visited):
    n = len(visited)
    return (is_visited(i, j + 1, visited) and not is_visited(i - 1, j + 1, visited) and not is_visited(i + 1, j + 1, visited)) or \
        (is_visited(i + 1, j, visited) and not is_visited(i + 1, j + 1, visited) and not is_visited(i + 1, j - 1, visited)) or \
        (is_visited(i, j - 1, visited) and not is_visited(i + 1, j - 1, visited) and not is_visited(i - 1, j - 1, visited)) or \
        (is_visited(i - 1, j, visited) and not is_visited(i - 1, j + 1, visited) and not is_visited(i - 1, j - 1, visited))


def search_opt_2(i, j, visited):
    if out_of_bounds(i, j, len(visited)) or visited[i][j]:
        return 0
    elif bottom_right_corner(i, j, len(visited)):
        return 1
    else:
        visited[i][j] = 1

        # For the first step either go down or right. I've chose down
        # This is because routes around the diagonal are symmetric
        # Notice how the final solution is multiplied by 2
        if i == 0 and j == 0:
            return search_opt_2(i + 1, j, deepcopy(visited))

        if cannot_reach_bottom_right(i, j, visited):
            return 0

        return search_opt_2(i + 1, j, deepcopy(visited)) + \
            search_opt_2(i - 1, j, deepcopy(visited)) + \
            search_opt_2(i, j + 1, deepcopy(visited)) + \
            search_opt_2(i, j - 1, deepcopy(visited))


def main():
    start_time = time.time()
    n = 3

    visited = [[0] * n for x in range(n)]
    # No optimizations
    print(search_no_opt(0, 0, visited))
    print("No Optimization: \nTime of execution: {} secs\n".format(
    time.time() - start_time))

    # Optimization 1
    visited = [[0] * n for x in range(n)]
    print(2 * search_opt_1(0, 0, visited))
    print("Optimization 1: \nTime of execution: {} secs\n".format(
    time.time() - start_time))

    # Optimization 2:
    visited = [[0] * n for x in range(n)]
    print(2 * search_opt_2(0, 0, visited))
    print("Optimization 2: \nTime of execution: {} secs\n".format(
        time.time() - start_time))


if __name__ == '__main__':
    main()
