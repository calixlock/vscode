import pygame 
#####################################################################################
#<0> 기본 초기화 (반듯이 해야하는 것들)
pygame.init() # (반드시) 초기화 

# 화면크기
screen_w = 480 # 가로
screen_h = 640 # 세로
screen = pygame.display.set_mode((screen_w,screen_h)) #(가로,세로)

# 화면 타이틀
pygame.display.set_caption("test") # 게임 이름

##### FPS 프레임 설정 
clock = pygame.time.Clock()

#####################################################################################


#####################################################################################
#<1> 사용자 게임 초기화 (배경화면, 게임이미지, 좌표. 속도, 폰트 등) 
## 배경이미지 
background = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/background_test.png")

### 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/character.png")
character_size = character.get_rect().size # 이미지 크기 구해
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_w / 2)- (character_width / 2) # 화면 가로의 절반 크기 해당하는 곳 위치 (위치)
character_y_pos = screen_h -character_height

#### 이동 좌표 설정
to_x = 0
to_y = 0

#캐릭터 속도
character_speed = 0.6

###### 적

enemy = pygame.image.load("C:/Users/amj41/OneDrive/바탕 화면/git/vscode/py_game/enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기 구해
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

# enemy의 초기위치
enemy_x_pos = (screen_w / 2)- (enemy_width / 2) # 화면 가로의 절반 크기 해당하는 곳 위치 (위치)
enemy_y_pos = (screen_h / 2)- (enemy_height / 2)

####### 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 시간 
total_time = 3
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴




# 이벤트 루프 
running = 1 # ture(진행) 게임 진행중인가? 플래그 세우기
while running:
    
    #5> fps 설정
    dt = clock.tick(120) # 게임화면의 초당 프레임 수 설정
    # print("fps : " + str(clock.get_fps()))
    
#<2> 이벤트 처리 (키보드, 마우스, 경계, 충돌, 등)
    for event in pygame.event.get():  # 어떤 이벤트 발생했는가 ?
        if event.type == pygame.QUIT: # 창 닫히는 이벤트 발생했는가 ?
            running = 0 # false // 종료
    #4> 키보드 입력에 대한 실행        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_w - character_width):
        character_x_pos = (screen_w - character_width)
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > (screen_h - character_height):
        character_y_pos = (screen_h - character_height)

    
    ###### 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    ###### 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("crash!") 
        running = 0   


    #1> 배경 채우기
    
    #1-1> 색상값으로 넣을 수 있음
    screen.fill((0,0,255)) # (R,G,B) 색상값으로 넣을 수 있음
    
    #1-2> 이미지 불러와 넣기
    # screen.blit(background, (0,0)) # 배경이미지 위치설정 및 그리기
    
    #2> 캐릭터 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 위치설정 및 그리기
    
    #3> 적 그리기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 위치설정 및 그리기
    
    #7> 타이머 넣기 / 경과시간 계산

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #  현재시간 - 시작시간    초단위 환산

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255) ) # (출력 글자, True, 글자색상(RGB))
    screen.blit(timer, (10,10)) # 시간위치 조정
    if total_time - elapsed_time <= 0:
        print("time out")
        running = 0


    pygame.display.update() # 게임화면을 계속 불러와 그려짐

# 잠시대기
pygame.time.delay(2000)




# 종료
pygame.quit()