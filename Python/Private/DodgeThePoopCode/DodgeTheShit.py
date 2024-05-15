import datetime
import sys
import os
# import pkgutil
from collections import Counter
from math import atan2, sin, cos
from random import randint, uniform
import pygame
import pygame.freetype

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
mixer = pygame.mixer
mixer.music.set_volume(1)

# game directory - save files
# save_info_dir = r"C:\Users\Dupamin\PycharmProjects\CaltexAdventures\save_info.py"
# save_stats_dir = r"C:\Users\Dupamin\PycharmProjects\CaltexAdventures\save_stats.txt"
curr_dir = os.path.dirname(os.path.abspath("__init__.py"))

# sounds - S = Sound
SBackButton = mixer.Sound("Sounds\BackButton.wav")  # used
SButton = mixer.Sound("Sounds\Button.wav")  # used
SBeforeMC = [mixer.Sound("Sounds\BeforeMC1.wav"),  # used
             mixer.Sound("Sounds\BeforeMC2.wav")]  # used
SBGMusicMe = mixer.Sound("Sounds\BGMusicMe.wav")  # used
SCoinPickup = mixer.Sound("Sounds\CoinPickup.wav")  # used
SHugPickup = mixer.Sound("Sounds\HugPickup.wav")  # used
SSoulHugPickup = mixer.Sound("Sounds\SoulHugPickup.wav")  # used
SCoSiDam = mixer.Sound("Sounds\CoSiDam.wav")  # used
SGothit = [mixer.Sound("Sounds\Gothit1.wav"),  # used
           mixer.Sound("Sounds\Gothit2.wav"),  # used
           mixer.Sound("Sounds\Gothit3.wav"),  # used
           mixer.Sound("Sounds\Gothit4.wav"),  # used
           mixer.Sound("Sounds\Gothit5.wav"),  # used
           mixer.Sound("Sounds\Gothit6.wav")]  # used
SGothitMC = [mixer.Sound("Sounds\GothitMC1.wav"),  # used
             mixer.Sound("Sounds\GothitMC2.wav"),  # used
             mixer.Sound("Sounds\GothitMC3.wav")]  # used
SCharChooseDoge = mixer.Sound("Sounds\CharChooseDoge.wav")  # used
SCharChooseJarek = [mixer.Sound("Sounds\CharChooseJarek1.wav"),  # used
                    mixer.Sound("Sounds\CharChooseJarek2.wav"),  # used
                    mixer.Sound("Sounds\CharChooseJarek3.wav"),  # used
                    mixer.Sound("Sounds\CharChooseJarek4.wav")]  # used
SChooseProduct = mixer.Sound("Sounds\ChooseProduct1.wav")  # used
# mixer.Sound("Sounds\ChooseProduct2.wav"),
# mixer.Sound("Sounds\ChooseProduct3.wav")]
SChooseProductThanks = mixer.Sound("Sounds\ChooseProductThanks.wav")  # used
SMyStudents = [mixer.Sound("Sounds\MyStudents1.wav"),  # used
               mixer.Sound("Sounds\MyStudents2.wav"),  # used
               mixer.Sound("Sounds\MyStudents3.wav"),  # used
               mixer.Sound("Sounds\MyStudents4.wav")]  # used
SScoreMenu = mixer.Sound("Sounds\ScoreMenu.wav")  # used
SShopEntry = mixer.Sound("Sounds\ShopEntry.wav")  # used

# default game variables
window_size = screen_width, screen_height = 800, 533
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Dodge the shit")

# fonts
game_font = pygame.freetype.SysFont("comicsans", 30, bold=True)
shop_font = pygame.freetype.SysFont("comicsans", 18, bold=True)
settings_font = pygame.freetype.SysFont("comicsans", 24, bold=True)
desc_font = pygame.freetype.SysFont("comicsans", 12)
lb_header_font = pygame.freetype.SysFont("comicsans", 30, bold=True)
lb_font = pygame.freetype.SysFont("comicsans", 30, italic=True)
lb_font_small = pygame.freetype.SysFont("comicsans", 18, italic=True)
lb_comment_font = pygame.freetype.SysFont("comicsans", 24, bold=True)

# colors
green_scheme = ((151, 225, 5), (135, 200, 4), (118, 175, 4))
orange_scheme = ((227, 224, 52), (201, 199, 46), (181, 179, 42))
red_scheme = ((222, 31, 18), (176, 25, 14), (105, 15, 8))
grey_scheme = ((50, 50, 50), (30, 30, 30), (30, 30, 30))

# backgrounds
game_bg = pygame.image.load("Gamefiles\caltex.jpg")
game_hell_bg = pygame.image.load("Gamefiles\caltex_hell.jpg")
menu_bg = pygame.image.load("Gamefiles\caltexmenu.jpg")
shop_bg = pygame.image.load("Gamefiles\shop.png")

# background images
fire_low_img = [pygame.image.load(r"Gamefiles\fire_low_1.png"), pygame.image.load(r"Gamefiles\fire_low_2.png"),
                pygame.image.load(r"Gamefiles\fire_low_3.png"), pygame.image.load(r"Gamefiles\fire_low_4.png")]

# player and player related images
# doge
doge_walkright_img = [pygame.image.load("Gamefiles\doge_lookingright.png"),
                      pygame.image.load("Gamefiles\doge_lookingatyou_right.png"),
                      pygame.image.load("Gamefiles\ohmygod_transparent_smol.png")]
doge_walkleft_img = [pygame.image.load("Gamefiles\doge_lookingleft.png"),
                     pygame.image.load("Gamefiles\doge_lookingatyou_left.png"),
                     pygame.image.load("Gamefiles\ohmygod_transparent_smol.png")]
doge_hit_img = [pygame.image.load("Gamefiles\doge_gothit.png"), pygame.image.load("Gamefiles\doge_gothit2.png")]
doge_chad_img = pygame.image.load("Gamefiles\doge_ischad.png")
# jarek
jarek_walkright_img = [pygame.image.load("Gamefiles\jarek_walks.png"), pygame.image.load("Gamefiles\jarek_stands.png"),
                       pygame.image.load("Gamefiles\jarek_default.png")]
jarek_walkleft_img = [pygame.transform.flip(pygame.image.load("Gamefiles\jarek_walks.png"), True, False),
                      pygame.transform.flip(pygame.image.load("Gamefiles\jarek_stands.png"), True, False),
                      pygame.image.load("Gamefiles\jarek_default.png")]
jarek_hit_img = [pygame.image.load("Gamefiles\jarek_gothit.png"), pygame.image.load("Gamefiles\jarek_gothit2.png")]
jarek_chad_img = pygame.transform.flip(pygame.image.load("Gamefiles\jarek_smooch.png"), True, False)
# other
hearts_img = [pygame.image.load(r"Gamefiles\blank_heart.png"), pygame.image.load(r"Gamefiles\blank_heart.png"),
              pygame.image.load(r"Gamefiles\blank_heart.png"), pygame.image.load(r"Gamefiles\full_heart.png"),
              pygame.image.load(r"Gamefiles\full_heart.png"), pygame.image.load(r"Gamefiles\full_heart.png")]
soul_heart_img = pygame.image.load("Gamefiles\soul_heart.png")  # also shop image

# enemies images
poop_img = pygame.image.load("Gamefiles\poop.png")
paper_img = pygame.image.load("Gamefiles\papers.png")

# currency images
dogecoin_img = pygame.image.load("Gamefiles\dogecoin.png")
czk_img = pygame.image.load("Gamefiles\stokorun.png")

# pickupable images
hug_img = pygame.image.load("Gamefiles\hug.png")
soul_hug_img = pygame.image.load("Gamefiles\soul_hug.png")

# shop images
add_surv_img = pygame.image.load("Gamefiles\plus_surv.png")

# other random shit images
placeholder_img = pygame.image.load(r"Gamefiles\borealis_logo.png")
oogway_img = pygame.image.load("Gamefiles\MrOogway.png")

warning_true = False  # bool to ask if I want hard reset
rand01 = 0
fire_i = 0
fire_score = 0
score_color = "black"
SShopEntryPlayed = False

# death variables
poops = []
papers = []
coins = []
hugs = []
soul_hugs = []
poop_timer = 0
paper_timer = 0
coin_timer = 0
hug_timer = 0
soul_hug_timer = 0
hp_timer = 0
chad_timer = 0
shot_speed_modifier = 0.5


def initWarningRect():
    warning1 = settings_font.render("This will delete all your progress!", "White")
    warning2 = settings_font.render("Do you want to continue?", "White")
    warning1_rect = warning1[0].get_rect(centerx=screen_width // 2, centery=screen_height // 2 + 75)
    warning2_rect = warning2[0].get_rect(centerx=screen_width // 2, centery=screen_height // 2 + 105)
    warning_bg = pygame.Rect(warning1_rect.x - 10, warning1_rect.y - 10, warning1_rect.width + 20,
                             warning1_rect.height + 100)
    pygame.draw.rect(screen, red_scheme[2], warning_bg, border_radius=10)
    screen.blit(warning1[0], warning1_rect)
    screen.blit(warning2[0], warning2_rect)
    return warning1_rect.centerx, warning1_rect.centery


class Doge(object):
    def __init__(self, doge_x, doge_y):
        self.doge_x = doge_x
        self.doge_y = doge_y
        self.hitbox = char_walkright_img[2].get_rect()
        self.vel = 5
        self.left = self.left2 = False
        self.right = self.right2 = False
        self.walkCount = 0
        self.hitpoints = 3
        self.soulheart = 0
        self.score = 0
        self.czk = 0
        self.hit = False
        self.chad = False

    def draw(self, f_screen):
        if self.hit:
            if hp_timer // 20 % 2 == 0:
                if self.left or self.left2:
                    f_screen.blit(char_hit_img[rand01], (self.doge_x, self.doge_y))
                else:
                    f_screen.blit(pygame.transform.flip(char_hit_img[rand01], True, False), (self.doge_x, self.doge_y))
            self.hitbox = char_hit_img[rand01].get_rect()
        elif self.chad:
            if self.right or self.right2:
                f_screen.blit(char_chad_img, (self.doge_x, self.doge_y))
            else:
                f_screen.blit(pygame.transform.flip(char_chad_img, True, False), (self.doge_x, self.doge_y))
            self.hitbox = char_chad_img.get_rect()
        else:
            if self.left:
                f_screen.blit(char_walkleft_img[0], (self.doge_x, self.doge_y))
                self.hitbox = char_walkleft_img[0].get_rect()
            elif self.right:
                f_screen.blit(char_walkright_img[0], (self.doge_x, self.doge_y))
                self.hitbox = char_walkright_img[0].get_rect()
            else:
                if self.left2:
                    f_screen.blit(char_walkleft_img[self.walkCount // 270], (self.doge_x, self.doge_y))
                    self.hitbox = char_walkleft_img[self.walkCount // 270].get_rect()
                elif self.right2:
                    f_screen.blit(char_walkright_img[self.walkCount // 270], (self.doge_x, self.doge_y))
                    self.hitbox = char_walkright_img[self.walkCount // 270].get_rect()
                else:
                    f_screen.blit(char_walkright_img[2], (self.doge_x, self.doge_y))
                    self.hitbox = char_walkright_img[2].get_rect()
                if self.walkCount < 270:
                    self.walkCount += 4
                elif self.walkCount < 541:
                    self.walkCount += 1
        self.hitbox.x = self.doge_x
        self.hitbox.y = self.doge_y
        self.hitbox.inflate_ip(-20, -20)
        self.czk = (self.score * 5.71 * (1 + survived)) // 100


class PoopEnemy(object):
    def __init__(self, x, y, targetx, targety):
        self.x = x
        self.y = y
        self.immunity = 0
        self.targetx = targetx
        self.targety = targety
        angle = atan2(self.targety - randy, self.targetx - randx)
        self.velx = cos(angle) * (1 + 0.01 * int(survived))
        self.vely = sin(angle) * (1 + 0.01 * int(survived))
        self.rotation = uniform(-0.8, 0.8)
        self.rot_angle = 0
        self.hitbox = poop_img.get_rect()
        self.rotated_img = poop_img

    def draw(self, f_screen):
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        self.rotated_img = pygame.transform.rotate(poop_img, self.rot_angle)
        if self.rot_angle < 360 or self.rot_angle > -360:
            self.rot_angle += self.rotation
        else:
            self.rotation = 0
        f_screen.blit(self.rotated_img, (self.x, self.y))


class PaperEnemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.immunity = 0
        self.rotation = uniform(-0.5, 0.5)
        self.rot_angle = 0
        self.hitbox = paper_img.get_rect()
        self.rotated_img = paper_img

    def draw(self, f_screen):
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        self.rotated_img = pygame.transform.rotate(paper_img, self.rot_angle)
        if self.rot_angle < 360 or self.rot_angle > -360:
            self.rot_angle += self.rotation
        else:
            self.rotation = 0
        f_screen.blit(self.rotated_img, (self.x, self.y))


class Dogecoin(object):
    def __init__(self, x, y):
        self.hitbox = dogecoin_img.get_rect()
        self.hitbox.inflate_ip(8, 8)
        self.hitbox.centerx = x
        self.hitbox.centery = y
        self.livespan = 800

    def draw(self, f_screen):
        f_screen.blit(dogecoin_img, (self.hitbox.x + 4, self.hitbox.y + 4))


class Hugs(object):
    def __init__(self, x, y):
        self.hitbox = hug_img.get_rect()
        self.hitbox.inflate_ip(6, 6)
        self.hitbox.centerx = x
        self.hitbox.centery = y
        self.livespan = 900

    def draw(self, f_screen):
        f_screen.blit(hug_img, (self.hitbox.x + 3, self.hitbox.y + 3))


class SoulHugs(object):
    def __init__(self, x, y):
        self.hitbox = soul_hug_img.get_rect()
        self.hitbox.inflate_ip(6, 6)
        self.hitbox.centerx = x
        self.hitbox.centery = y
        self.livespan = 900

    def draw(self, f_screen):
        f_screen.blit(soul_hug_img, (self.hitbox.x + 3, self.hitbox.y + 3))


class MenuButton(object):
    def __init__(self, x, y, w, h, color="black"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text_color = color
        self.rect = pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)

    def draw(self, f_screen, rounding=0, text="", shortcut=""):
        button_text = game_font.render(text, self.text_color)
        button_text_rect = button_text[0].get_rect(center=self.rect.center)
        sc = desc_font.render(shortcut, self.text_color)
        sc_rect = sc[0].get_rect(center=button_text_rect.center)
        pygame.draw.rect(f_screen, self.color, self.rect, border_radius=rounding)
        f_screen.blit(button_text[0], (button_text_rect.x, button_text_rect.y))
        f_screen.blit(sc[0], (sc_rect.x, sc_rect.y + 24))


def checkMenuMouseOver(obj, color=green_scheme):
    mouse_pos = pygame.mouse.get_pos()
    if obj.rect.collidepoint(mouse_pos):
        obj.color = color[0]
        if pygame.mouse.get_pressed() == (1, 0, 0):
            obj.color = color[2]
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
            if obj.w == 120:
                SBackButton.play()
            else:
                SButton.play()
            return True
    else:
        obj.color = color[1]


def checkVolumeMouseOver(obj, vol):
    mouse_pos = pygame.mouse.get_pos()
    if obj.rect.collidepoint(mouse_pos):
        obj.color = orange_scheme[0]
        if pygame.mouse.get_pressed() == (1, 0, 0):
            obj.color = orange_scheme[2]
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
            return float(int(vol) ^ 1)
    else:
        obj.color = orange_scheme[1]
    return vol


class ShopItem(object):
    def __init__(self, x, y, img, price, bought, item_id):
        self.x = x
        self.y = y
        self.mouseover = False
        self.bought = bought
        self.dc_price = price
        self.czk_price = price
        self.id = item_id
        if self.id == 5:
            self.price = self.dc_price
        else:
            self.price = self.czk_price
        self.color = (234, 22, 11)
        self.img = img
        self.hitbox = img.get_rect()
        self.hitbox.height = 40
        self.hitbox.width = 40
        self.rect = pygame.Rect(self.x, self.y,
                                self.hitbox.width, self.hitbox.height)
        self.rect.inflate_ip(70, 70)
        #  self.rect.height = self.rect.height + 20
        self.hitbox.inflate_ip(10, 10)

    def itemDescription(self, mouse, text):
        if self.mouseover:
            desc_text = shop_font.render(text, "white")
            desc_text_rect = desc_text[0].get_rect()
            rect_around = desc_text_rect.inflate(20, 20)
            rect_around.x = mouse[0]
            rect_around.y = mouse[1]
            desc_text_rect.center = rect_around.center
            box_height = wordWrap(mouse, screen, text,
                                  shop_font)  # box_height = by how many pixels should desc box increase in height
            while rect_around.right >= screen_width:
                rect_around.width -= 2
            rect_around.height += box_height
            #  new_desc_text = shop_font.render(new_desc, "white")
            #  shop_font.render_to(screen, (50, 50), f"{box_height}", "white")
            pygame.draw.rect(screen, "white", rect_around, 2, border_radius=5)

    def checkShopMouseOver(self):
        self.bought = readSaveInfo()[self.id]
        mouse_pos = pygame.mouse.get_pos()
        if not self.bought:
            if self.id == 5:
                currency = readSaveInfo()[1]  # currency = Dogecoins
                self.czk_price = 0
            else:
                currency = readSaveInfo()[0]  # currency = CZK
                self.dc_price = 0
            if self.rect.collidepoint(mouse_pos):
                self.mouseover = True
                if currency >= self.price:
                    self.color = (151, 225, 5)
                else:
                    self.color = (195, 18, 9)
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if currency >= self.price:
                        self.color = (118, 175, 4)
                    else:
                        self.color = (117, 11, 6)
                if event.type == pygame.MOUSEBUTTONUP:
                    if not self.bought and self.price <= currency:
                        self.bought = True
                        SChooseProductThanks.play()
                        writeSaveInfo(self.czk_price, self.dc_price, self.id)
                        self.color = (135, 200, 4)
                    else:
                        self.color = (157, 14, 7)
            else:
                self.mouseover = False
                if currency >= self.price:
                    self.color = (135, 200, 4)
                else:
                    self.color = (157, 14, 7)
        else:
            if self.rect.collidepoint(mouse_pos):
                self.mouseover = True
                self.color = (50, 50, 50)
            else:
                self.mouseover = False
                self.color = (30, 30, 30)

    def draw(self, f_screen, text, desc_text, curr=" CZK", rounding=10):
        self.checkShopMouseOver()
        button_text = shop_font.render(text, "white")
        price_text = shop_font.render(str(self.price) + curr, "white")
        button_text_rect = button_text[0].get_rect(center=self.rect.center)
        price_text_rect = price_text[0].get_rect(center=self.rect.center)
        pygame.draw.rect(f_screen, self.color, self.rect, border_radius=rounding)
        f_screen.blit(self.img, (self.x, self.y))
        f_screen.blit(button_text[0], (button_text_rect.x, self.rect.bottom - 20))
        f_screen.blit(price_text[0], (price_text_rect.x, self.rect.top + 5))
        self.itemDescription(pygame.mouse.get_pos(), desc_text)


#  taken from https://www.pygame.org/docs/ref/freetype.html?highlight=render_to#pygame.freetype.Font.render_to
def wordWrap(mouse, surf, text, font, color="white"):
    font.origin = True
    words = text.split(' ')
    count = [False] * len(words)
    line_spacing = font.get_sized_height() + 2
    x, y = mouse[0] + 10, mouse[1] + line_spacing - 2
    space = font.get_rect(' ')
    for word in words:
        bounds = font.get_rect(word)
        if x + bounds.x + bounds.width >= screen_width - 10:
            x, y = mouse[0] + 10, y + line_spacing
            count[words.index(word)] = True
        font.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return Counter(count)[True] * line_spacing


class CharItem(object):
    def __init__(self, x, y, img, chosen, name, sound, scheme=orange_scheme):
        self.x = x
        self.y = y
        self.chosen = chosen
        self.name = name
        self.w = 100
        self.h = 100
        self.scheme = scheme
        self.color = orange_scheme[0]
        # self.text_color = color
        self.img = img
        self.hitbox = img.get_rect()
        self.rect = pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)
        self.hitbox.center = self.rect.center
        self.sound = sound

    def draw(self, rounding=0):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=rounding)
        screen.blit(self.img, self.hitbox)
        if self.chosen:
            char_name = game_font.render(self.name, "white")
            char_name_rect = char_name[0].get_rect()
            char_name_rect.center = (screen_width // 2, screen_height // 2 + 150)
            screen.blit(char_name[0], char_name_rect)


def checkCharMouseOver(obj, scheme=orange_scheme):
    if obj.chosen:
        obj.scheme = green_scheme
    elif obj.name != "Doge" and not readSaveInfo()[5]:
        obj.scheme = grey_scheme
    else:
        obj.scheme = scheme
    mouse_pos = pygame.mouse.get_pos()
    if obj.rect.collidepoint(mouse_pos):
        obj.color = obj.scheme[0]
        if pygame.mouse.get_pressed() == (1, 0, 0):
            obj.color = obj.scheme[2]
        if event.type == pygame.MOUSEBUTTONUP and obj.scheme != grey_scheme:
            pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
            writeSaveInfo(0, 0, 11)
            if readSaveInfo()[5]:
                writeSaveInfo(0, 0, 12)
            if obj.name == "Doge":
                obj.sound.play()
            else:
                obj.sound[randint(0, 3)].play()
            obj.chosen = True
            return True
    else:
        obj.color = obj.scheme[1]


def blitDogeDead():
    dead_text = game_font.render("Doge is fired", score_color)
    dead_text_rect = dead_text[0].get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    screen.blit(dead_text[0], (dead_text_rect.x, dead_text_rect.y))


def textDogecoins():
    game_font.render_to(screen, (66, screen_height - 54), f": {doge.score}", "white")
    screen.blit(pygame.transform.scale(dogecoin_img, (40, 40)), (20, screen_height - 60))


def textCzk():
    game_font.render_to(screen, (screen_width - 114, screen_height - 54), f": {int(doge.czk)}", "white")
    screen.blit(pygame.transform.scale(czk_img, (80, 40)), (screen_width - 200, screen_height - 60))


def textRect(string, x, y, color="orange"):
    text = shop_font.render(string, "black")
    text_rect = text[0].get_rect(x=x, y=y)
    bg_rect = text_rect.inflate(12, 12)
    pygame.draw.rect(screen, color, bg_rect, border_radius=5)
    screen.blit(text[0], text_rect)


def oogwaySound():
    oogway_rect = pygame.Rect(20, 463, oogway_img.get_width(), oogway_img.get_height())
    screen.blit(oogway_img, (20, 463))
    if oogway_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP \
            and not mixer.Channel(5).get_busy():
        pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
        mixer.Channel(5).play(SMyStudents[randint(0, 3)])


def changeSaveBoolValue(my_bool):
    if not my_bool:
        my_bool = True
        return my_bool
    else:
        my_bool = False
        return my_bool


def saveGameStats():
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    with open("save_stats.txt", "a") as f:
        f.write(f"Dogecoins: {doge.score}; Money: {int(doge.czk)}; Survived: {int(survived)}; "
                f"Date: {d:02d}-{m:02d}-{y}\n")


def readSaveStats():
    part = {}
    with open("save_stats.txt", "r") as f:
        for i, stats in enumerate(f):
            part[i] = dict(item.split(": ") for item in stats.split("; "))
    part_sorted = {k: v for k, v in sorted(part.items(), key=lambda item: int(item[1]['Survived']), reverse=True)}
    return part_sorted


def writeSaveInfo(it_price=0, it_dc_price=0, index=None):
    read_info = readSaveInfo()
    if index is not None:
        read_info_list = list(read_info)
        read_info_list[index] = changeSaveBoolValue(read_info[index])
        read_info = tuple(read_info_list)
    with open("save_info.py", "w") as f:
        f.write(f"Money = {read_info[0] + int(doge.czk) - it_price}\n"
                f"Dogecoins = {read_info[1] + doge.score - it_dc_price}\n"
                f"TotalPlaytime = {read_info[2] + int(survived)}\n"
                f"it_shop_soulheart = {read_info[3]}\nit_shop_add_surv = {read_info[4]}\n"
                f"it_shop_jarek = {read_info[5]}\n"
                f"it_shop_ph3 = {read_info[6]}\nit_shop_ph4 = {read_info[7]}\nit_shop_ph5 = {read_info[8]}\n"
                f"it_shop_ph6 = {read_info[9]}\nit_shop_ph7 = {read_info[10]}\ndoge_chosen = {read_info[11]}\n"
                f"jarek_chosen = {read_info[12]}\n")


def readSaveInfo():
    sys.path.append(curr_dir)
    try:
        # save_bin = pkgutil.get_data("helpmod", "save_info.py")
        # save_utf = pkgutil.
        import save_info
    except ModuleNotFoundError:
        with open("save_info.py", "w") as f:
            f.write(f"Money = 0\nDogecoins = 0\n"f"TotalPlaytime = 0\n"
                    f"it_shop_soulheart = False\nit_shop_add_surv = False\nit_shop_jarek = False\n"
                    f"it_shop_ph3 = False\nit_shop_ph4 = False\nit_shop_ph5 = False\n"
                    f"it_shop_ph6 = False\nit_shop_ph7 = False\ndoge_chosen = True\njarek_chosen = False\n")
    finally:
        import save_info
    del sys.modules["save_info"]
    return save_info.Money, save_info.Dogecoins, save_info.TotalPlaytime, save_info.it_shop_soulheart, \
        save_info.it_shop_add_surv, save_info.it_shop_jarek, save_info.it_shop_ph3, save_info.it_shop_ph4, \
        save_info.it_shop_ph5, save_info.it_shop_ph6, save_info.it_shop_ph7, save_info.doge_chosen, \
        save_info.jarek_chosen


def gamePause():
    pause_text = game_font.render("Game paused", score_color)
    screen.blit(pause_text[0], (screen_width // 2 - pause_text[0].get_width() // 2, screen_height // 2 - 100))
    pygame.display.update()
    pygame.time.delay(200)
    while True:
        clock.tick(100)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                if menu_played or shop_played:
                    writeSaveInfo()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE]:
            break
        pygame.display.update()


def redrawGameWindow(fire_index):
    if survived > 90:
        screen.blit(game_hell_bg, (0, 0))
        screen.blit(fire_low_img[fire_index//10], (0, 500))
    else:
        screen.blit(game_bg, (0, 0))
    if shop_item_add_surv.bought:
        game_font.render_to(screen, (30, 30), f"Seconds survived: {int(survived)-60} (+60)", score_color)
    else:
        game_font.render_to(screen, (30, 30), f"Seconds survived: {int(survived)}", score_color)
    #  game_font.render_to(screen, (30, 60), f"Hitpoints: {doge.hitpoints}", (40, 40, 40))
    textDogecoins()
    textCzk()
    for c in coins:
        c.draw(screen)
        #  pygame.draw.rect(screen, "red", c.hitbox, 2)
        c.livespan -= 1
    for h in hugs:
        h.draw(screen)
        #  pygame.draw.rect(screen, "red", h.hitbox, 2)
        h.livespan -= 1
    for sh in soul_hugs:
        sh.draw(screen)
        #  pygame.draw.rect(screen, "red", sh.hitbox, 2)
        sh.livespan -= 1
    doge.draw(screen)
    #  pygame.draw.rect(screen, "red", doge.hitbox, 2)
    for pap in papers:
        pap.draw(screen)
        #  pygame.draw.rect(screen, "red", pap.hitbox, 2)
    for p in poops:
        p.draw(screen)
        #  pygame.draw.rect(screen, "red", p.hitbox, 2)
    for n in range(3):
        screen.blit(hearts_img[n + doge.hitpoints], (screen_width - 160 + 50 * n, 20))
    if doge.soulheart == 1:
        screen.blit(soul_heart_img, (screen_width - 210, 20))
    if doge.hitpoints <= 0:
        blitDogeDead()
    pygame.display.update()


def redrawMenuWindow():
    screen.blit(menu_bg, (0, 0))
    play_button.draw(screen, 20, "Work", "(enter)")
    shop_button.draw(screen, 20, "Shop", "('s')")
    lb_button.draw(screen, 20, "Leaderboards", "('l')")
    settings_button.draw(screen, 20, "Settings")
    charmenu_button.draw(screen, 20, "Characters")
    exit_button.draw(screen, 20, "Quit", "(esc)")
    oogwaySound()
    pygame.display.update()


def redrawSettingsWindow():
    def drawResetWarning():
        global survived
        global warning_true
        global char_walkright_img, char_walkleft_img, char_hit_img, char_chad_img
        initWarningRect()
        yes_button.draw(screen, 5, "Yep")
        no_button.draw(screen, 5, "WTF NO")
        is_yes = checkMenuMouseOver(yes_button, red_scheme)
        is_no = checkMenuMouseOver(no_button, red_scheme)
        if is_yes:
            if os.path.exists("save_info.py"):
                os.remove("save_info.py")
            if os.path.exists("save_stats.txt"):
                os.remove("save_stats.txt")
            choose_char_jarek.chosen = False
            choose_char_doge.chosen = True
            survived = 0
            char_walkright_img = doge_walkright_img
            char_walkleft_img = doge_walkleft_img
            char_hit_img = doge_hit_img
            char_chad_img = doge_chad_img
            warning_true = False
        if is_no:
            warning_true = False

    global warning_true
    screen.blit(menu_bg, (0, 0))
    back_button.draw(screen, 10, "Back")
    set_music_volume.draw(screen, 20, f"Music {music_set_text}")
    # set_sound_volume.draw(screen, 20, f"Sound {sound_set_text}")
    reset_save_button.draw(screen, 20, "Hard reset")
    if warning_true:
        drawResetWarning()
    pygame.display.update()


def redrawScoreWindow(fire_index, fire_surv):
    if fire_surv > 90:
        screen.blit(game_hell_bg, (0, 0))
        screen.blit(fire_low_img[fire_index // 10], (0, 500))
    else:
        screen.blit(game_bg, (0, 0))
    screen.blit(score_label_survived[0], (screen_width // 2 - score_label_survived[0].get_width() // 2, 100))
    screen.blit(score_label_score[0], (screen_width // 2 - score_label_score[0].get_width() // 2, 135))
    screen.blit(score_label_money[0], (screen_width // 2 - score_label_money[0].get_width() // 2, 170))
    screen.blit(score_label_continue[0],
                (screen_width // 2 - score_label_continue[0].get_width() // 2, screen_height // 2 - 50))
    pygame.display.update()


def redrawShopWindow():
    screen.blit(shop_bg, (0, 0))
    back_button.draw(screen, 10, "Back")
    # pygame.draw.rect(screen, "orange", (120, 120, 200, 200), border_radius=5)
    textRect(f"CZK: {readSaveInfo()[0]}", 130, 160)
    textRect(f"Dogecoins: {readSaveInfo()[1]}", 130, 135)
    # screen.blit(shop_font.render(f"CZK: {readSaveInfo()[0]}", "white")[0], (130, 160))
    # screen.blit(shop_font.render(f"Dogecoins: {readSaveInfo()[1]}", "white")[0], (130, 135))

    shop_item_ph7.draw(screen, "Borealis",
                       "I mean... Han said that I did it, so it must be true, right? :)", " EUR")
    shop_item_ph4.draw(screen, "Borealis",
                       "Seriously, you won't find anything :)", " EUR")
    shop_item_add_surv.draw(screen, "+time",
                            "Increases the starting time so you can listen to Doom OST sooner... "
                            "Or whatever other reason you might have, idk.", " CZK")
    shop_item_soul_hug.draw(screen, "Soul Hearts",
                            "Soul hugs start spawning, allowing you to have one additional heart.")
    shop_item_ph6.draw(screen, "Borealis",
                       "Ok maybe it is. And maybe according to him I was the one who did it:)", " EUR")
    shop_item_ph3.draw(screen, "Borealis",
                       "This is nothing :)", " EUR")
    shop_item_ph5.draw(screen, "Borealis",
                       "It really is not a reference to the 22 million EUR that Sungjin inputted :)", " EUR")
    shop_item_jarek.draw(screen, "Jarek", "Unlocks Jarek, Master Oogway's novice.", " DC")
    pygame.display.update()


def redrawLBWindow():
    def drawLBData(data):
        i = 150
        cnt = 0
        color = "black"
        for v in data.values():
            lb_font_small.render_to(screen, (170, i+5), f"#{cnt+1}", color)
            lb_font.render_to(screen, (250, i), v['Dogecoins'], color)
            lb_font.render_to(screen, (350, i), v['Money'], color)
            lb_font.render_to(screen, (450, i), v['Survived'], color)
            lb_font.render_to(screen, (550, i), v['Date'][:10], color)
            i += 35
            cnt += 1
            if cnt > 9:
                break

    def drawLBTable():
        lb_rect_border = pygame.Rect(147, 47, 606, 466)
        lb_rect = pygame.Rect(150, 50, 600, 460)
        lb_rect_upper = pygame.Rect(155, 55, 590, 75)
        lb_rect_bottom = pygame.Rect(155, 140, 590, 365)
        # rectangles
        pygame.draw.rect(screen, (190, 240, 121), lb_rect_border, border_radius=10)
        pygame.draw.rect(screen, (84, 125, 2), lb_rect, border_radius=10)
        pygame.draw.rect(screen, (135, 200, 4), lb_rect_upper, border_radius=10)
        pygame.draw.rect(screen, (135, 200, 4), lb_rect_bottom, border_radius=10)
        # lines upper
        pygame.draw.line(screen, "black", (lb_rect.x + 165, lb_rect.y + 10), (lb_rect.x + 165, lb_rect.y + 75), width=4)
        pygame.draw.line(screen, "black", (lb_rect.x + 275, lb_rect.y + 10), (lb_rect.x + 275, lb_rect.y + 75), width=4)
        pygame.draw.line(screen, "black", (lb_rect.x + 375, lb_rect.y + 10), (lb_rect.x + 375, lb_rect.y + 75), width=4)
        # lines bottom
        pygame.draw.line(screen, "black", (lb_rect.x + 165, lb_rect.y + 95), (lb_rect.x + 165, lb_rect.y + 440),
                         width=4)
        pygame.draw.line(screen, "black", (lb_rect.x + 275, lb_rect.y + 95), (lb_rect.x + 275, lb_rect.y + 440),
                         width=4)
        pygame.draw.line(screen, "black", (lb_rect.x + 375, lb_rect.y + 95), (lb_rect.x + 375, lb_rect.y + 440),
                         width=4)
        # line upper/bottom
        pygame.draw.line(screen, "black", (lb_rect.x + 10, lb_rect.y + 85), (lb_rect.x + 590, lb_rect.y + 85), width=4)
        lb_header_font.render_to(screen, (lb_rect.x + 100, lb_rect.y + 35), "DC")
        lb_header_font.render_to(screen, (lb_rect.x + 190, lb_rect.y + 35), "CZK")
        lb_header_font.render_to(screen, (lb_rect.x + 290, lb_rect.y + 35), "Surv")
        lb_header_font.render_to(screen, (lb_rect.x + 440, lb_rect.y + 35), "Date")

    def drawTopComment():
        rect_border = pygame.Rect(20, 47, 110, 100)
        rect = pygame.Rect(23, 50, 104, 94)
        pygame.draw.rect(screen, (84, 125, 2), rect_border, border_radius=10)
        pygame.draw.rect(screen, (135, 200, 4), rect, border_radius=10)
        first = lb_comment_font.render("Top 10")
        second = lb_comment_font.render("sorted")
        third = lb_comment_font.render("by Surv")
        first_rect = first[0].get_rect(centerx=rect.centerx, centery=rect.centery - 30)
        second_rect = second[0].get_rect(centerx=rect.centerx, centery=rect.centery)
        third_rect = third[0].get_rect(centerx=rect.centerx, centery=rect.centery + 30)
        screen.blit(first[0], first_rect)
        screen.blit(second[0], second_rect)
        screen.blit(third[0], third_rect)

    screen.blit(menu_bg, (0, 0))
    drawLBTable()
    if os.path.exists("save_stats.txt"):
        drawLBData(readSaveStats())
    drawTopComment()
    back_button.draw(screen, 10, "Back")
    pygame.display.update()


def redrawCharMenu():
    screen.blit(menu_bg, (0, 0))
    back_button.draw(screen, 10, "Back")
    choose_char_doge.draw(10)
    choose_char_jarek.draw(10)
    pygame.display.update()


# setting the game bools
game_played = False
menu_played = True
shop_played = False
settings_played = False
lb_played = False  # leaderboards
charmenu_played = False
# chosen character
if readSaveInfo()[11]:
    char_walkright_img = doge_walkright_img
    char_walkleft_img = doge_walkleft_img
    char_hit_img = doge_hit_img
    char_chad_img = doge_chad_img
else:
    char_walkright_img = jarek_walkright_img
    char_walkleft_img = jarek_walkleft_img
    char_hit_img = jarek_hit_img
    char_chad_img = jarek_chad_img
# inicializing character
doge = Doge(screen_width // 2 - 25, screen_height // 2 - 34)
# buttons
play_button = MenuButton(screen_width // 2, screen_height // 2 - 50, 200, 70)
shop_button = MenuButton(screen_width // 2 - 105, screen_height // 2 + 30, 200, 70)
lb_button = MenuButton(screen_width // 2 + 105, screen_height // 2 + 30, 200, 70)
settings_button = MenuButton(screen_width // 2 - 105, screen_height // 2 + 110, 200, 70)
charmenu_button = MenuButton(screen_width // 2 + 105, screen_height // 2 + 110, 200, 70)
exit_button = MenuButton(screen_width // 2, screen_height // 2 + 190, 200, 70)
back_button = MenuButton(70, screen_height - 50, 120, 40)
# settings
set_music_volume = MenuButton(screen_width // 2, screen_height // 2 - 50, 200, 70)
# set_sound_volume = MenuButton(screen_width // 2 + 105, screen_height // 2 - 50, 200, 70)
reset_save_button = MenuButton(screen_width // 2, screen_height // 2 + 30, 200, 70)
# shop items
shop_item_soul_hug = ShopItem(400, 130, soul_heart_img, 350, readSaveInfo()[3], 3)
shop_item_add_surv = ShopItem(560, 130, add_surv_img, 500, readSaveInfo()[4], 4)
shop_item_jarek = ShopItem(240, 260, jarek_chad_img, 150, readSaveInfo()[5], 5)
shop_item_ph3 = ShopItem(400, 260, placeholder_img, 22000000, readSaveInfo()[6], 6)
shop_item_ph4 = ShopItem(560, 260, placeholder_img, 22000000, readSaveInfo()[7], 7)
shop_item_ph5 = ShopItem(240, 390, placeholder_img, 22000000, readSaveInfo()[8], 8)
shop_item_ph6 = ShopItem(400, 390, placeholder_img, 22000000, readSaveInfo()[9], 9)
shop_item_ph7 = ShopItem(560, 390, placeholder_img, 22000000, readSaveInfo()[10], 10)
# characters
choose_char_doge = CharItem(150, 250, doge_walkright_img[2], readSaveInfo()[11], "Doge", SCharChooseDoge)
choose_char_jarek = CharItem(300, 250, jarek_walkright_img[2], readSaveInfo()[12], "Jarek párek, dám mu dárek",
                             SCharChooseJarek)
initWarningRect()
yes_button = MenuButton(initWarningRect()[0] - 100, initWarningRect()[1] + 75, 150, 50, "White")
no_button = MenuButton(initWarningRect()[0] + 100, initWarningRect()[1] + 75, 150, 50, "White")

if readSaveInfo()[4]:  # if add_surv is bought
    survived = 60
else:
    survived = 0

key_timer = 0

while 1:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if menu_played or shop_played:
                writeSaveInfo()
            sys.exit()
    if game_played:
        pygame.mouse.set_visible(False)
        if not mixer.music.get_busy() and survived < 70:
            mixer.music.load("Sounds\smb_overworld.mp3")
            mixer.music.play()
        elif mixer.music.get_busy() and 70 < survived < 75:
            mixer.music.fadeout(10000)
            if 72 <= survived <= 73 and not mixer.Channel(1).get_busy():
                mixer.Channel(1).play(SBeforeMC[0])
                mixer.Channel(1).queue(SBeforeMC[1])
        if not mixer.music.get_busy() and survived >= 80.8:
            mixer.music.load("Sounds\doom_long.mp3")
            mixer.music.play()
        if survived > 90:
            score_color = "white"
        else:
            score_color = "black"
        if doge.hitpoints <= 0:
            game_played = False
            menu_played = False
            SScoreMenu.play()
            pygame.time.delay(2000)
            survived = int(survived)
            fire_score = survived
            score_label_survived = game_font.render(f"Survived for: {survived}s", score_color)
            score_label_score = game_font.render(f"Dogecoins collected: {doge.score}", score_color)
            score_label_money = game_font.render(f"Money generated: {int(doge.czk)}", score_color)
            score_label_continue = game_font.render("Press enter for main menu...", score_color)
            saveGameStats()  # saves game stats into a txt file
            writeSaveInfo()  # saves game info and adds it to the previous info
            doge = Doge(screen_width // 2 - 25, screen_height // 2 - 34)
            # death variables
            poops = []
            papers = []
            coins = []
            hugs = []
            soul_hugs = []
            poop_timer = 0
            paper_timer = 0
            coin_timer = 0
            hug_timer = 0
            soul_hug_timer = 0
            hp_timer = 0
            chad_timer = 0
            survived = 60 if shop_item_add_surv.bought else 0
            # if shop_item_add_surv.bought:
            #     survived = 60
            # else:
            #     survived = 0
            continue
        rand_vel_x = rand_vel_y = 0

        while rand_vel_x == 0:
            rand_vel_x = randint(-5, 5)
            while rand_vel_y == 0:
                rand_vel_y = randint(-5, 5)

        for poop in poops:
            if not doge.hit:
                if poop.hitbox.colliderect(doge.hitbox):
                    poops.pop(poops.index(poop))
                    if survived < 90:
                        SGothit[randint(0, 5)].play()
                    else:
                        SGothitMC[randint(0, 2)].play()
                    doge.hit = True
                    if doge.soulheart == 0:
                        doge.hitpoints -= 1
                    else:
                        doge.soulheart -= 1
                    rand01 = randint(0, 1)
            if -25 < poop.x < screen_width+5 or poop.immunity < 50:
                if -25 < poop.y < screen_height+5 or poop.immunity < 50:
                    poop.x += poop.velx
                    poop.y += poop.vely
                else:
                    poops.pop(poops.index(poop))
            else:
                poops.pop(poops.index(poop))
            poop.immunity += 1

        for paper in papers:
            if not doge.hit:
                if paper.hitbox.colliderect(doge.hitbox):
                    papers.pop(papers.index(paper))
                    if survived < 90:
                        SGothit[randint(0, 5)].play()
                    else:
                        SGothitMC[randint(0, 2)].play()
                    doge.hit = True
                    if doge.soulheart == 0:
                        doge.hitpoints -= 1
                    else:
                        doge.soulheart -= 1
                    rand01 = randint(0, 1)
            if -25 < paper.y < screen_height+5 or paper.immunity < 50:
                paper.y += 2
            else:
                papers.pop(papers.index(paper))
            paper.immunity += 1

        for coin in coins:
            if coin.hitbox.colliderect(doge.hitbox):
                coins.pop(coins.index(coin))
                SCoinPickup.play()
                doge.score += 1
                doge.chad = True
            if coin.livespan <= 0:
                coins.pop(coins.index(coin))

        for hug in hugs:
            if hug.hitbox.colliderect(doge.hitbox):
                hugs.pop(hugs.index(hug))
                SHugPickup.play()
                if doge.hitpoints < 3:
                    doge.hitpoints += 1
            if hug.livespan <= 0:
                hugs.pop(hugs.index(hug))

        for soul_hug in soul_hugs:
            if soul_hug.hitbox.colliderect(doge.hitbox):
                soul_hugs.pop(soul_hugs.index(soul_hug))
                SSoulHugPickup.play()
                if doge.soulheart < 1:
                    doge.soulheart += 1
            if soul_hug.livespan <= 0:
                soul_hugs.pop(soul_hugs.index(soul_hug))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and doge.doge_x > doge.vel:
            doge.doge_x -= doge.vel
            doge.left = doge.left2 = True
            doge.right = doge.right2 = False
            doge.walkCount = 0
        elif keys[pygame.K_RIGHT] and doge.doge_x + doge.hitbox.width < screen_width - doge.vel:
            doge.doge_x += doge.vel
            doge.left = doge.left2 = False
            doge.right = doge.right2 = True
            doge.walkCount = 0
        else:
            doge.left = doge.right = False
        if keys[pygame.K_UP] and doge.doge_y > doge.vel:
            doge.doge_y -= doge.vel
            doge.left = doge.left2
            doge.right = doge.right2
            doge.walkCount = 0
        if keys[pygame.K_DOWN] and doge.doge_y + doge.hitbox.height < screen_height - doge.vel:
            doge.doge_y += doge.vel
            doge.left = doge.left2
            doge.right = doge.right2
            doge.walkCount = 0
        if keys[pygame.K_ESCAPE]:
            doge.hitpoints = 0
        if keys[pygame.K_BACKSPACE]:
            gamePause()
            pygame.time.delay(200)

        # modify to increase the poop rate of fire: up for slower (100 = 1/1s, 50 = 2/1s)
        if poop_timer >= 100 - shot_speed_modifier * int(survived):
            randx = randint(-45, screen_width+25)
            randy = randint(-45, screen_height+25)
            while not randx < -25 and not randx > screen_width + 5 and not randy < -25 and \
                    not randy > screen_height + 5:
                randx = randint(-45, screen_width+25)
                randy = randint(-45, screen_height+25)
            poops.append(PoopEnemy(randx, randy, round(doge.doge_x + doge.hitbox.width // 2),
                                   round(doge.doge_y + doge.hitbox.height // 2)))
            poop_timer = 0
            if survived >= 90:
                shot_speed_modifier = 0.32
            else:
                shot_speed_modifier = 0.25
        if survived >= 90:
            if paper_timer >= 100 - (int(survived) - 90)/2:
                randx = randint(100, screen_width - 100)
                randy = randint(-100, -50)
                papers.append(PaperEnemy(randx, randy))
                paper_timer = 0

        if len(coins) < 3:
            if coin_timer >= 300:
                rand_spawn_x = randint(120, screen_width - 120)
                rand_spawn_y = randint(120, screen_height - 120)
                while screen_width - 120 < rand_spawn_x < 120 and \
                        screen_height - 120 < rand_spawn_y < 120 or \
                        doge.hitbox.x - 120 < rand_spawn_x < doge.hitbox.x + doge.hitbox.width + 120 and \
                        doge.hitbox.y - 120 < rand_spawn_y < doge.hitbox.y + doge.hitbox.height + 120:
                    rand_spawn_x = randint(120, screen_width - 120)
                    rand_spawn_y = randint(120, screen_height - 120)
                coins.append(Dogecoin(rand_spawn_x, rand_spawn_y))
                coin_timer = 0

        if len(hugs) < 1:
            if hug_timer >= 5000:
                rand_spawn_x = randint(120, screen_width - 120)
                rand_spawn_y = randint(120, screen_height - 120)
                while screen_width - 120 < rand_spawn_x < 120 and \
                        screen_height - 120 < rand_spawn_y < 120 or \
                        doge.hitbox.x - 120 < rand_spawn_x < doge.hitbox.x + doge.hitbox.width + 120 and \
                        doge.hitbox.y - 120 < rand_spawn_y < doge.hitbox.y + doge.hitbox.height + 120:
                    rand_spawn_x = randint(120, screen_width - 120)
                    rand_spawn_y = randint(120, screen_height - 120)
                hugs.append(Hugs(rand_spawn_x, rand_spawn_y))
                hug_timer = 0

        if shop_item_soul_hug.bought:
            if len(soul_hugs) < 1:
                if soul_hug_timer >= 12000:
                    rand_spawn_x = randint(120, screen_width - 120)
                    rand_spawn_y = randint(120, screen_height - 120)
                    while screen_width - 120 < rand_spawn_x < 120 and \
                            screen_height - 120 < rand_spawn_y < 120 or \
                            doge.hitbox.x - 120 < rand_spawn_x < doge.hitbox.x + doge.hitbox.width + 120 and \
                            doge.hitbox.y - 120 < rand_spawn_y < doge.hitbox.y + doge.hitbox.height + 120:
                        rand_spawn_x = randint(120, screen_width - 120)
                        rand_spawn_y = randint(120, screen_height - 120)
                    soul_hugs.append(SoulHugs(rand_spawn_x, rand_spawn_y))
                    soul_hug_timer = 0

        if doge.hit:
            hp_timer += 1
            if hp_timer >= 100:
                doge.hit = False
                hp_timer = 0
        if doge.chad:
            chad_timer += 1
            if chad_timer >= 70:
                doge.chad = False
                chad_timer = 0
        survived += 0.01
        poop_timer += 1
        paper_timer += 1
        coin_timer += 1
        if doge.hitpoints == 3:
            hug_timer += 1
        else:
            hug_timer += 2
        if doge.soulheart == 1:
            soul_hug_timer += 1
        elif doge.hitpoints == 3:
            soul_hug_timer += 3
        else:
            soul_hug_timer += 2
        redrawGameWindow(fire_i)
        fire_i += 1
        if fire_i >= 40:
            fire_i = 0

    elif shop_played:
        if not mixer.music.get_busy():
            mixer.music.play()
        if randint(0, 2000) == 1 and not mixer.Channel(4).get_busy():
            mixer.Channel(4).play(SCoSiDam)
        elif randint(0, 2000) == 2 and not mixer.Channel(4).get_busy():
            mixer.Channel(4).play(SChooseProduct)
        if not SShopEntryPlayed:
            SShopEntry.play()
            SShopEntryPlayed = True
        redrawShopWindow()
        shop_played = not checkMenuMouseOver(back_button)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            shop_played = False

    elif lb_played:
        redrawLBWindow()
        lb_played = not checkMenuMouseOver(back_button)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            lb_played = False

    elif charmenu_played:
        charmenu_played = not checkMenuMouseOver(back_button)
        if checkCharMouseOver(choose_char_jarek):
            choose_char_doge.chosen = False
            char_walkright_img = jarek_walkright_img
            char_walkleft_img = jarek_walkleft_img
            char_hit_img = jarek_hit_img
            char_chad_img = jarek_chad_img
        if checkCharMouseOver(choose_char_doge):
            choose_char_jarek.chosen = False
            char_walkright_img = doge_walkright_img
            char_walkleft_img = doge_walkleft_img
            char_hit_img = doge_hit_img
            char_chad_img = doge_chad_img
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            charmenu_played = False
        redrawCharMenu()

    elif settings_played:
        mixer.music.set_volume(checkVolumeMouseOver(set_music_volume, mixer.music.get_volume()))
        if mixer.music.get_volume() == 1:
            music_set_text = "On"
        else:
            music_set_text = "Off"
        if not warning_true:
            warning_true = checkMenuMouseOver(reset_save_button, orange_scheme)
            settings_played = not checkMenuMouseOver(back_button)
        redrawSettingsWindow()

    elif menu_played:
        SShopEntryPlayed = False
        if not pygame.mouse.get_visible():
            pygame.mouse.set_visible(True)
        if not mixer.music.get_busy():
            if randint(0, 9) == 0:
                mixer.music.load("Sounds\BGMusicMe.wav")
                mixer.music.play()
            else:
                mixer.music.load(r"Sounds\flower_garden.mp3")
                mixer.music.play()
        game_played = checkMenuMouseOver(play_button)
        if game_played:
            mixer.music.unload()
            if shop_item_add_surv.bought:
                survived = 60
        shop_played = checkMenuMouseOver(shop_button)
        settings_played = checkMenuMouseOver(settings_button)
        lb_played = checkMenuMouseOver(lb_button)
        charmenu_played = checkMenuMouseOver(charmenu_button)
        if checkMenuMouseOver(exit_button):
            sys.exit()
        if key_timer < 30:
            key_timer += 1
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                key_timer = 0
                game_played = True
                mixer.music.unload()
            if keys[pygame.K_s]:
                shop_played = True
            if keys[pygame.K_l]:
                lb_played = True
            if keys[pygame.K_ESCAPE]:
                sys.exit()
        redrawMenuWindow()

    else:
        if not pygame.mouse.get_visible():
            pygame.mouse.set_visible(True)
        if key_timer < 30:
            key_timer += 1
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                key_timer = 0
                menu_played = True
                mixer.music.unload()
                SScoreMenu.stop()
        redrawScoreWindow(fire_i, fire_score)
        fire_i += 1
        if fire_i >= 40:
            fire_i = 0
