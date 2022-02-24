import pygame

pygame.init() # (반드시) 초기화 

# 화면크기
screen_w = 480 # 가로
screen_h = 640 # 세로
screen = pygame.display.set_mode((screen_w,screen_h)) #(가로,세로)

# 화면 타이틀
pygame.display.set_caption("test") # 게임 이름

# 이벤트 루프 

running = 1 # ture(진행) 게임 진행중인가

while running:
    # pass
    for event in pygame.event.get():  # 어떤 이벤트 발생했는가 ?
        if event.type == pygame.QUIT: # 창 닫히는 이벤트 발생했는가 ?
            running = 0 # false


# 종료
pygame.quit()