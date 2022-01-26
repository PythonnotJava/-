import sys
import pygame
import math
import random

width, height = 1920, 1080

# 定义时间、显示、频率
t1 = 0.18

show_n = 0

# 烟花绽放频率，数值越大频率越高
show_frequency = 0.001

# 烟花列表
color_list = []
for i in range(50):
    color_list.append([random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)])
# print(color_list)

# 游戏初始化
pygame.init()


# 烟花
class Fireworks:
    is_show = False
    x, y = 0, 0
    vy = 0
    p_list = []
    color = [0, 0, 0]
    v = 0

    def __init__(self, x, y, vy, n=300, color=(0, 255, 0), v=10):
        self.x = x
        self.y = y
        self.vy = vy
        self.color = color
        self.v = v
        for e in range(n):
            self.p_list.append([random.random() * 2 * math.pi, 0, v * math.pow(random.random(), 1 / 3)])

    def again(self):
        self.is_show = True
        self.x = random.randint(width // 2 - 350, width // 2 + 350)
        self.y = random.randint(int(height / 2), int(height * 3 / 5))
        self.vy = -40 * (random.random() * 0.4 + 0.8) - self.vy * 0.2
        self.color = color_list[random.randint(0, len(color_list) - 1)].copy()
        n = len(self.p_list)
        self.p_list = []
        for l in range(n):
            self.p_list.append([random.random() * 2 * math.pi, 0, self.v * math.pow(random.random(), 1 / 3)])

    def run(self):
        global show_n
        for p in self.p_list:
            p[1] = p[1] + (random.random() * 0.6 + 0.7) * p[2]
            p[2] = p[2] * 0.97
            if p[2] < 1.2:
                self.color[0] *= 0.9999
                self.color[1] *= 0.9999
                self.color[2] *= 0.9999

            if max(self.color) < 10 or self.y > height+p[1]:
                show_n -= 1
                self.is_show = False
                break
        self.vy += 10 * t1
        self.y += self.vy * t1

# 烟花列表
fk_list = [Fireworks(300, 300, -20, n=100, color=[0, 255, 0], v=10),Fireworks(300, 300, -20, n=200, color=[0, 0, 255], v=11),Fireworks(300, 300, -20, n=200, color=[0, 0, 255], v=12),Fireworks(300, 300, -20, n=500, color=[0, 0, 255], v=12),Fireworks(300, 300, -20, n=600, color=[0, 0, 255], v=13),Fireworks(300, 300, -20, n=700, color=[255, 0, 0], v=15),Fireworks(300, 300, -20, n=800, color=[255, 255, 0], v=18)]

# 游戏主循环
def let_it_go(screen, file, font, choose=False):
    """这里的choose表示是否选择背景图片"""
    if not choose:
        show_n = 0
        for event in pygame.event.get():
            # pygame这个不能少，否则退出还在循环
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(file, (0, 0))
        font_text = font.render("新年快乐!!!", True, (255, 215, 0))
        screen.blit(font_text, (0.234 * width, 0.416 * height))
        font_text1 = font.render("祝你——", True, (255, 215, 0))
        screen.blit(font_text1, (0.156 * width, 0.2777 * height))
        # 放烟花
        for d, fk in enumerate(fk_list):
            if not fk.is_show:
                fk.is_show = False
                if random.random() < show_frequency * (len(fk_list) - show_n):
                    show_n += 1
                    fk.again()
                continue
            fk.run()
            for p in fk.p_list:
                x, y = fk.x + p[1] * math.cos(p[0]), fk.y + p[1] * math.sin(p[0])
                if random.random() < 0.055:
                    screen.set_at((int(x), int(y)), (255, 255, 255))
                else:
                    screen.set_at((int(x), int(y)), (int(fk.color[0]), int(fk.color[1]), int(fk.color[2])))
    else:
        show_n = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        font_text = font.render("新年快乐!!!", True, (255, 215, 0))
        screen.blit(font_text, (0.234 * width, 0.416 * height))
        font_text1 = font.render("祝你——", True, (255, 215, 0))
        screen.blit(font_text1, (0.156 * width, 0.2777 * height))
        # 放烟花
        for d, fk in enumerate(fk_list):
            if not fk.is_show:
                fk.is_show = False
                if random.random() < show_frequency * (len(fk_list) - show_n):
                    show_n += 1
                    fk.again()
                continue
            fk.run()
            for p in fk.p_list:
                x, y = fk.x + p[1] * math.cos(p[0]), fk.y + p[1] * math.sin(p[0])
                if random.random() < 0.055:
                    screen.set_at((int(x), int(y)), (255, 255, 255))
                else:
                    screen.set_at((int(x), int(y)), (int(fk.color[0]), int(fk.color[1]), int(fk.color[2])))

