import pygame
########################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (pygame 사용시 반드시 실행해줄것)

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz") # 게임 이름

# FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load("/Users/kimminjae/BJOJ_KIM/Practice Projects/pygame_basic/background.png")

# 캐릭터 만들기
character = pygame.image.load("/Users/kimminjae/BJOJ_KIM/Practice Projects/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
charcater_y_pos = screen_height - character_height
running = True 
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님 
            
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    # 5. 화면 그리기
    screen.blit(background, (0, 0))
    pygame.display.update() # 게임화면 계속 그리기
    
    
# pygame 종료
pygame.quit()