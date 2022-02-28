import numpy as np
import heapq
import pygame

pygame.init()
over = False
screen = pygame.display.set_mode((700,700))
size = 35
scale = 700/size
clock = pygame.time.Clock()

array = np.zeros((size,size))
click = 0
green = False





def H_value(a,b):
    return np.sqrt((b[1]-a[1])**2 + (b[0]-a[0])**2)

def astar(start,goal,array):
    # neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    close_set = set()
    came_from = {}
    g_value = {start: 0}
    f_value = {start: H_value(start, goal)}
    openset_fvalue = []

    heapq.heappush(openset_fvalue,(f_value[start],start))

    while openset_fvalue:

        heapq.heapify(openset_fvalue)
        current = heapq.heappop(openset_fvalue)[1]
        if current == goal:
            move = []
            while current in came_from:
                move.append(current)
                current = came_from[current]
            return move

        if current != start:
            array[current[0]][current[1]] = 5

        close_set.add(current)


        for x,y in neighbors:
            neighbor = current[0] + x, current[1] + y
            gvalue_sementara = g_value[current] + H_value(current,neighbor)
            if 0 <= neighbor[0] < len(array[1]):
                if 0 <= neighbor[1] < len(array):
                    if array[neighbor[0]][neighbor[1]] == 3:
                        continue

                else:
                    continue
            else:
                continue

            if neighbor in close_set and gvalue_sementara >= g_value.get(neighbor, 0):
                continue
            if gvalue_sementara < g_value.get(neighbor, 0) or neighbor not in [i[1] for i in openset_fvalue]:
                came_from[neighbor] = current
                g_value[neighbor] = gvalue_sementara
                f_value[neighbor] = gvalue_sementara + H_value(neighbor, goal)
                heapq.heappush(openset_fvalue, (f_value[neighbor], neighbor))

    return False

def start():
    for r in range(len(array)):
        for c in range(len(array[0])):
            if array[r][c] == 1:
                return (r,c)
def goal():
    for r in range(len(array)):
        for c in range(len(array[0])):
            if array[r][c] == 2:
                return (r,c)

            


def draw():
    screen.fill((255,255,255))

    for r in range(len(array)):
        for c in range(len(array[0])):
            if array[r][c] == 0:
                pygame.draw.rect(screen,(0,0,0),(c*scale,r*scale,scale,scale),1)
            if array[r][c] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (c * scale, r * scale, scale, scale))
            if array[r][c] == 2:
                pygame.draw.rect(screen, (255, 0, 0), (c * scale, r * scale, scale, scale))
            if array[r][c] == 3:
                pygame.draw.rect(screen, (0, 0, 0), (c * scale, r * scale, scale, scale))
            if array[r][c] == 4:
                pygame.draw.rect(screen, (0, 255, 255), (c * scale, r * scale, scale, scale))
            if array[r][c] == 5:
                pygame.draw.rect(screen, (255, 0, 255), (c * scale, r * scale, scale, scale))

            pygame.draw.rect(screen, (0, 0, 0), (c * scale, r * scale, scale, scale), 1)

    pygame.display.update()






while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click += 1
            if click == 1:
                array[int(event.pos[1]/scale)][int(event.pos[0]/scale)] = 1
            elif click == 2:
                array[int(event.pos[1] / scale)][int(event.pos[0] / scale)] = 2
            else:
                if green == False:
                    green = True
                elif green == True:
                    green = False
        if event.type == pygame.MOUSEMOTION and green:
            array[int(event.pos[1]/scale)][int(event.pos[0]/scale)] = 3

        key = pygame.key.get_pressed()

        if key[pygame.K_RETURN]:

            start = start()
            goal = goal()
            move = astar(start, goal, array)
            move = move[::-1]
            move.pop(len(move)-1)
            for x,y in move:
                array[x][y] = 4





    draw()




pygame.quit()