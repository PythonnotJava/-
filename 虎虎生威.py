import sys
import pygame
from fireworks import let_it_go
import random
import math
from configobj import ConfigObj

init_con = ConfigObj('init.ini', encoding='utf-8')
init_con_values = list(init_con.values())

# print(init_con)
pygame.init()
pygame.font.init()
size = width, height = 1800, 900
screen = pygame.display.set_mode(size, pygame.NOFRAME)
myfont = pygame.font.Font('STXINGKA.TTF', 72)
file = pygame.image.load(init_con_values[0])
clock = pygame.time.Clock()
pygame.mixer.init()
music = pygame.mixer.Sound(init_con_values[2])
music.play(-1)
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

moods = ['这一年','就这么快过去了', '我知道很多事', '让人久久不能释怀', '也有很多', '令你骄傲的时光', '新的一年即将到来',
         '祝你', '新的一年', '新的成就', '怀揣憧憬之心',  '在这里', '还是想在对你说一句', '新年快乐——']
mod_x = -100
mood = []
font = pygame.font.Font('STXINGKA.TTF', 48)
for i in moods:
    font_text = font.render(i, True, (255, 0, 0))
    mood.append(font_text)

DJS = ['5', '4', '3', '2', '1']
djs = []
font_ = pygame.font.Font('swissek.ttf', 108*2)
for j in DJS:
    f_t = font_.render(j, True, (255, 0, 0))
    djs.append(f_t)

# 晃动图片
mouse_cursor = pygame.image.load(init_con_values[3]).convert_alpha()
rect_width = mouse_cursor.get_width()
rect_height = mouse_cursor.get_height()
# print(rect_width, rect_height)

# 老虎图片
tiger = pygame.image.load('tiger.png').convert_alpha()
target_width, target_height = tiger.get_width(), tiger.get_height()
positions = [random.randint(1500, 1800 - target_width),random.randint(0, 900 - target_height)]

sen = pygame.image.load('sentence/1643082607697-ckt-抠图.png').convert_alpha()
sen_w, sen_h = sen.get_width(), sen.get_height()
local_run = 0
local_speed = 2

# 老虎心情
# 触碰老虎次数决定放烟花的时刻
mood_tiger = random.randint(5, 16)
print(mood_tiger)
all_time = []

while True:

    import os.path as path
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # 按q键退出
            if event.key == event.key == pygame.K_q:
                sys.exit()
            # 按s键截图
            if event.key == pygame.K_s:
                list_file = []
                list_ooo = list(range(1000))
                for num_in in list_ooo:
                    if path.isfile('picture/picture' + str(num_in) + '.jpg'):
                        continue
                    else:
                        list_file.append(num_in)
                pygame.image.save(screen, 'picture/picture' + str(list_file[0]) + '.jpg')
    screen.fill((0, 0, 0))
    # 星星漫步
    for l in range(nums):
        y1 = begin_y_list[l]
        begin_x_list[l] -= speed_final[l]
        pygame.draw.circle(screen, (
            random.choice(list(range(256))), random.choice(list(range(256))), random.choice(list(range(256))))
                           , (begin_x_list[l], y1), random.choice(r), 0)

    # 旋转行星
    roll_e += 0.01  # 假设每帧公转0.01pi
    pos_e_x = int(size[0] // 2 + size[0] // 6 * math.sin(roll_e))
    pos_e_y = int(size[1] // 2 + size[1] // 6 * math.cos(roll_e))
    pos_e1 = pos_e_x - 500
    pos_e2 = pos_e_y - 250
    pygame.draw.circle(screen, (0, 0, 255), (pos_e1, pos_e2), 15, 0)

    # 行星轨迹
    pos_e.append((pos_e1, pos_e2))
    if len(pos_e) > 150:
        pos_e.pop(0)
    for i in range(len(pos_e)):
        # 轨迹线为绿色=green=0,255,0
        pygame.draw.circle(screen, GREEN, pos_e[i], 1, 0)

    # 行星的卫星
    roll_m += 0.1  # 假设每帧公转0.1pi
    pos_m_x = int(pos_e1 + size[0] // 20 * math.sin(roll_m))
    pos_m_y = int(pos_e2 + size[1] // 20 * math.cos(roll_m))
    pygame.draw.circle(screen, (230, 230, 230), (pos_m_x, pos_m_y), 5, 0)

    # 卫星轨迹
    pos_mm.append((pos_m_x, pos_m_y))
    if len(pos_mm) > 100:
        pos_mm.pop(0)
    for i in range(len(pos_mm)):
        # 轨迹线为绿色=green=0,255,0
        pygame.draw.circle(screen, GREEN, pos_mm[i], 1, 0)
    # 鼠标的x,y坐标
    x, y = pygame.mouse.get_pos()

    # 变换字幕
    mod_x += 2
    if mod_x < 0:
        pass
    elif mod_x < 200:
        screen.blit(mood[0], (1400, 300))
        screen.blit(mood[1], (1300, 450))
    elif mod_x < 400:
        screen.blit(mood[2], (1400, 300))
    elif mod_x < 600:
        screen.blit(mood[3], (1400, 300))
    elif mod_x < 800:
        screen.blit(mood[4], (1400, 300))
    elif mod_x < 1000:
        screen.blit(mood[5], (1400, 300))
    elif mod_x < 1200:
        screen.blit(mood[6], (1400, 300))
    elif mod_x < 1400:
        screen.blit(mood[7], (1400, 300))
        screen.blit(mood[8], (1350, 450))
        screen.blit(mood[9], (1300, 600))
    elif mod_x < 1600:
        screen.blit(mood[10], (1400, 300))
    elif mod_x < 1800:
        screen.blit(mood[11], (1400, 300))
        screen.blit(mood[12], (1300, 450))
    elif mod_x < 2000:
        screen.blit(mood[13], (1400, 300))
    elif mod_x >= 2200:
        pass

    # 隐藏鼠标
    pygame.mouse.set_visible(False)
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 用其他图形代替鼠标
    screen.blit(mouse_cursor, (x, y))

    # 人物点燃烟花-> 放烟花
    screen.blit(tiger, positions)

    if positions[0]-target_width <= x <= positions[0]+target_width and positions[1]-target_height <= y <= positions[1]+target_height:
        all_time.append(1)
        print(len(all_time))
        if len(all_time) <= mood_tiger:
            positions = [random.randint(target_width,1800-target_width), random.randint(target_height,900-target_width)]
        else:
            positions = [-800, -800]
            # 这里开始做老虎说的话->‘我让你看烟花了’->然后切换屏幕放烟花
    if positions == [-800, -800]:
        local_run += local_speed
        if 0 <= local_run <= 200:
            screen.blit(sen, [width / 2 - sen_w / 2, height / 2 - sen_h / 2])
            screen.blit(sen, positions)
        elif 200 <= local_run <= 300:
            screen.blit(djs[0], [width / 2, height / 2])
        elif 300 <= local_run <= 400:
            screen.blit(djs[1], [width / 2, height / 2])
        elif 400 <= local_run <= 500:
            screen.blit(djs[2], [width / 2, height / 2])
        elif 500 <= local_run <= 600:
            screen.blit(djs[3], [width / 2, height / 2])
        elif 600 <= local_run <= 700:
            screen.blit(djs[4], [width / 2, height / 2])
        elif local_run >= 700:
            if eval(init_con_values[6]):
                let_it_go(screen=screen, file=file, font=myfont, choose=eval(init_con_values[1]))
                screen.blit(pygame.image.load(init_con_values[4]).convert_alpha(), [-0.5 * pygame.image.load(init_con_values[4]).convert_alpha().get_width(), 0])
                screen.blit(pygame.image.load(init_con_values[5]).convert_alpha(),
                        [width-0.5 * pygame.image.load(init_con_values[5]).convert_alpha().get_width(), height-pygame.image.load(init_con_values[5]).convert_alpha().get_height()])
            else:
                let_it_go(screen=screen, file=file, font=myfont, choose=eval(init_con_values[1]))
    pygame.display.update()
    clock.tick(50)
