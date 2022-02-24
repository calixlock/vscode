import pygame 

pygame.init() # (반드시) 초기화 

# 화면크기
screen_w = 480 # 가로
screen_h = 640 # 세로
screen = pygame.display.set_mode((screen_w,screen_h)) #(가로,세로)

# 화면 타이틀
pygame.display.set_caption("test") # 게임 이름

## 배경이미지 
background = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/background_test.png")

### 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/character.png")
character_size = character.get_rect().size # 이미지 크기 구해
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_w / 2)- (character_width / 2) # 화면 가로의 절반 크기 해당하는 곳 위치 (위치)
character_y_pos = screen_h -character_height

# 이벤트 루프 
running = 1 # ture(진행) 게임 진행중인가? 플래그 세우기
while running:
    # pass
    for event in pygame.event.get():  # 어떤 이벤트 발생했는가 ?
        if event.type == pygame.QUIT: # 창 닫히는 이벤트 발생했는가 ?
            running = 0 # false


    # 배경 채우기
    #1> 색상값으로 넣을 수 있음
    screen.fill((0,0,255)) # (R,G,B) 색상값으로 넣을 수 있음
    
    #2> 이미지 불러와 넣기
    # screen.blit(background, (0,0)) # 배경이미지 위치설정 및 그리기
    

    #3> 캐릭터 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 배경이미지 위치설정 및 그리기
    

    pygame.display.update() # 게임화면을 계속 불러와 그려짐




# 종료
pygame.quit()