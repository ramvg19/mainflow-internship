import random
from collections import deque

def generate_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    stack = [(1, 1)]
    maze[1][1] = ' '

    while stack:
        cx, cy = stack[-1]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[cy + dy][cx + dx] = ' '
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    maze[0][1] = ' '  
    maze[height - 1][width - 2] = ' '  
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def bfs_solve_maze(maze, start, end):
    queue = deque([start])
    came_from = {start: None}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor not in came_from and maze[neighbor[1]][neighbor[0]] == ' ':
                queue.append(neighbor)
                came_from[neighbor] = current

    path = []
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def mark_path(maze, path):
    for x, y in path:
        if maze[y][x] != 'S' and maze[y][x] != 'E':
            maze[y][x] = '.'

def main():
    width, height = 21, 21  
    maze = None

    while True:
        command = input("Enter 'create' to generate a maze or 'solve' to solve the maze or 'close' to close the program: ").strip().lower()

        if command == 'create':
            maze = generate_maze(width, height)
            print("Generated Maze:")
            print_maze(maze)

        elif command == 'solve' and maze is not None:
            start = (1, 0) 
            end = (19, 20)  
            path = bfs_solve_maze(maze, start, end)
            mark_path(maze, path)
            print("Solved Maze:")
            print_maze(maze)

        elif command == 'close':
            print("\nThank You for Playing")
            break

        else:
            print("Invalid command or maze not created yet. Please try again.")

if __name__ == "__main__":
    main()
