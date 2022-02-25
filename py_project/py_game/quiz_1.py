#똥피하기 게임
import pygame
import random

pygame.init()

screen_w = 480 # 가로
screen_h = 640 # 세로
screen = pygame.display.set_mode((screen_w,screen_h)) #(가로,세로)

pygame.display.set_caption("")

#FPS
clock = pygame.time.Clock()

# 480x640
background = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/background_test.png")
# 70x70
character = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/character.png")
character_size = character.get_rect().size
character_w = character_size[0]
character_h = character_size[1]
character_x = (screen_w - character_w) / 2 
character_y = screen_h - character_h
to_x = 0
character_speed = 0.5
# 70x70
enemy = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/enemy.png")
enemy_size = enemy.get_rect().size
enemy_w = enemy_size[0]
enemy_h = enemy_size[1]
enemy_x = random.randrange(0,screen_w - enemy_w)
enemy_y = 0
enemy_speed = 0.2


flag = 1
while flag:
    # FPS 설정
    dt = clock.tick(30)
    # 종료 이벤트 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = 0

    # 키보드 입력 설정    
        if event.type == pygame.KEYDOWN: # 눌리면 움직여라
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP: # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
           

    # 캐릭터 움직임 반영
    character_x += to_x

    # 경계값 처리
    if character_x <= 0:
        character_x = 0
    elif character_x >= screen_w - character_w:
        character_x = screen_w - character_w 

    # 적 움직임
    enemy_y += enemy_speed
    if enemy_y > screen_h - enemy_h:
        enemy_y = 0
        enemy_x = random.randrange(0,screen_w - enemy_w)

    ###### 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y

    ###### 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("crash!") 
        flag = 0   



    #화면에 띄우는 역할
    screen.blit(background, (0,0))
    screen.blit(character, (character_x,character_y))
    screen.blit(enemy, (enemy_x,enemy_y))
    
    pygame.display.update()


pygame.time.delay(500)
pygame.quit()