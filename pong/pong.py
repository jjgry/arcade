import pygame
import math


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Pong")

    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 60)

    p1_pos = 250
    p2_pos = 250

    p1_score = 0
    p2_score = 0

    PLAYER_WIDTH = 10
    PLAYER_HEIGHT = 40
    PLAYER_VEL = 4

    MAX_BOUNCE_ANGLE = 1  # ~60 degrees

    ball_pos = (250, 250)
    BALL_SIZE = 10
    BALL_SPEED = 3
    ball_vx = - BALL_SPEED
    ball_vy = 0

    run = True
    while run:
        pygame.time.delay(10)  # pause for 10ms (~100fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and (p1_pos > 0):
            p1_pos -= PLAYER_VEL
        if keys[pygame.K_s] and (p1_pos < 499 - PLAYER_HEIGHT):
            p1_pos += PLAYER_VEL
        if keys[pygame.K_UP] and(p2_pos > 0):
            p2_pos -= PLAYER_VEL
        if keys[pygame.K_DOWN] and (p2_pos < 499 - PLAYER_HEIGHT):
            p2_pos += PLAYER_VEL

        ball_pos = (ball_pos[0] + ball_vx, ball_pos[1] + ball_vy)

        # ball bounces off top or bottom of screen
        if (ball_pos[1] <= 0) or (ball_pos[1] >= 499):
            ball_vy = -ball_vy

        # ball bounces off players
        if ((30 <= ball_pos[0] <= 40)
                and (p1_pos <= ball_pos[1] <= p1_pos + PLAYER_HEIGHT)):
            relative_intersect = (p1_pos + PLAYER_HEIGHT/2) - ball_pos[1]
            normalised_relative_intersect = relative_intersect / \
                (PLAYER_HEIGHT / 2)
            bounce_angle = normalised_relative_intersect * MAX_BOUNCE_ANGLE
            ball_vx = BALL_SPEED * math.cos(bounce_angle)
            ball_vy = - BALL_SPEED * math.sin(bounce_angle)

        elif (460 <= ball_pos[0] <= 470
                and (p2_pos <= ball_pos[1] <= p2_pos + PLAYER_HEIGHT)):
            relative_intersect = (p2_pos + PLAYER_HEIGHT/2) - ball_pos[1]
            normalised_relative_intersect = relative_intersect / \
                (PLAYER_HEIGHT / 2)
            bounce_angle = normalised_relative_intersect * MAX_BOUNCE_ANGLE
            ball_vx = - BALL_SPEED * math.cos(bounce_angle)
            ball_vy = - BALL_SPEED * math.sin(bounce_angle)

        # if ball off screen reset and update score
        if (ball_pos[0] <= 0):
            ball_pos = (250, 250)
            ball_vx *= -1
            ball_vy = 0
            p2_score += 1
        elif (ball_pos[0] >= 499):
            ball_pos = (250, 250)
            ball_vx *= -1
            ball_vy = 0
            p1_score += 1

        # draw screen
        win.fill((0, 0, 0))
        dashes = 25
        dash_length = (500//dashes)

        for i in range(dashes):
            pygame.draw.line(
                win,
                (255, 255, 255),
                (250, i*(dash_length) + 10),
                (250, i*(dash_length) + dash_length//2 + 10),
                2)

        pygame.draw.rect(
            win,
            (255, 255, 255),
            (int(ball_pos[0] - BALL_SIZE/2),
                int(ball_pos[1] - BALL_SIZE/2),
                BALL_SIZE,
                BALL_SIZE)
        )
        pygame.draw.rect(
            win,
            (255, 255, 255),
            (30, p1_pos, PLAYER_WIDTH, PLAYER_HEIGHT))
        pygame.draw.rect(
            win,
            (255, 255, 255),
            (460, p2_pos, PLAYER_WIDTH, PLAYER_HEIGHT))

        p1_text = font.render(str(p1_score), True, (255, 255, 255))
        p2_text = font.render(str(p2_score), True, (255, 255, 255))
        win.blit(p1_text, (int(200 - p1_text.get_rect().width/2), 20))
        win.blit(p2_text, (int(300 - p2_text.get_rect().width/2), 20))

        pygame.display.update()

    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
