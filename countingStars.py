def let_it_go(width, height):

    import pygame
    import sys
    import math
    import random
    import os

    pygame.init()


    info = pygame.display.Info()
    size = width, height
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    pygame.display.set_caption("Star Sky")

    # 创建时钟对象 (可以控制游戏循环频率)---必须要---
    clock = pygame.time.Clock()


    # begin_location--depending on nums
    nums = 500
    begin_x_list, begin_y_list = [], []
    for x in range(500):
        begin_x = random.choice(list(range(width * 10)))  # 实现星星从屏幕外飘过来的特效
        begin_x_list.append(begin_x)

    for y in range(500):
        begin_y = random.choice(list(range(int(math.ceil(height * 0.45)))))
        begin_y_list.append(begin_y)

    # different speeds
    speed_final = []
    speed_list = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                  0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                  0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
                  0.5, 0.5, 0.5, 0.5, 0.5]
    for k in range(10):
        speed_final.extend(speed_list)

    # different radius
    r = [1, 2, 3, 4]

    # 旋转星河
    roll_e, roll_m = 0, 0
    pos_e, pos_mm = [], []
    GREEN = (0, 255, 0)

    while True:
        # ---6-1---首先---
        # 背景颜色为黑色
        screen.fill((0,0,0))

        #星星漫步
        for l in range(nums):
            y1 = begin_y_list[l]
            begin_x_list[l] -= speed_final[l]
            pygame.draw.circle(screen, (
            random.choice(list(range(256))), random.choice(list(range(256))), random.choice(list(range(256))))
                                   , (begin_x_list[l],y1), random.choice(r), 0)


        #旋转行星
        roll_e += 0.01  # 假设每帧公转0.01pi
        pos_e_x = int(size[0] // 2 + size[0] // 6 * math.sin(roll_e))
        pos_e_y = int(size[1] // 2 + size[1] // 6 * math.cos(roll_e))
        pos_e1 = pos_e_x-500
        pos_e2= pos_e_y-250
        pygame.draw.circle(screen,(0,0,255), (pos_e1, pos_e2), 15, 0)

        #行星轨迹
        pos_e.append((pos_e1, pos_e2))
        if len(pos_e) > 150:
            pos_e.pop(0)
        for i in range(len(pos_e)):
            # 轨迹线为绿色=green=0,255,0
            pygame.draw.circle(screen, GREEN, pos_e[i], 1, 0)

        #行星的卫星
        roll_m += 0.1  # 假设每帧公转0.1pi
        pos_m_x = int(pos_e1 + size[0] // 20 * math.sin(roll_m))
        pos_m_y = int(pos_e2 + size[1] // 20 * math.cos(roll_m))
        pygame.draw.circle(screen,(230,230,230), (pos_m_x, pos_m_y), 5, 0)

        #卫星轨迹
        pos_mm.append((pos_m_x, pos_m_y))
        if len(pos_mm) > 100:
            pos_mm.pop(0)
        for i in range(len(pos_mm)):
            # 轨迹线为绿色=green=0,255,0
            pygame.draw.circle(screen, GREEN, pos_mm[i], 1, 0)

        pygame.display.update()
        pygame.display.flip()
        # 数值越大刷新越快，小球运动越快
        clock.tick(40)
        # 检测事件之退出游戏
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
