import pygame
import math
import random


class Pong:
    PLAYER_WIDTH = 10
    PLAYER_HEIGHT = 40
    PLAYER_VEL = 4

    MAX_BOUNCE_ANGLE = 1  # ~60 degrees

    BALL_SIZE = 10
    BALL_SPEED = 3

    def __init__(self):
        self.p1_pos = 250
        self.p2_pos = 250

        self.p1_score = 0
        self.p2_score = 0

        self.ball_pos = (250, 250)
        self.ball_vx = random.choice([1, -1]) * Pong.BALL_SPEED / 2
        self.ball_vy = 0

    @staticmethod
    def start():
        pong = Pong()
        pong.run()

    def run(self):
        pygame.init()
        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Pong")

        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 60)

        run = True
        while run:
            pygame.time.delay(10)  # pause for 10ms (~100fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] and (self.p1_pos > 0):
                self.p1_pos -= self.PLAYER_VEL
            if keys[pygame.K_s] and (self.p1_pos < 499 - Pong.PLAYER_HEIGHT):
                self.p1_pos += self.PLAYER_VEL
            if keys[pygame.K_UP] and(self.p2_pos > 0):
                self.p2_pos -= self.PLAYER_VEL
            if keys[pygame.K_DOWN] and (self.p2_pos < 499 - Pong.PLAYER_HEIGHT):
                self.p2_pos += self.PLAYER_VEL

            self.ball_pos = (
                self.ball_pos[0] + self.ball_vx, 
                self.ball_pos[1] + self.ball_vy)

            # ball bounces off top or bottom of screen
            if (self.ball_pos[1] <= 0) or (self.ball_pos[1] >= 499):
                self.ball_vy = -self.ball_vy

            # ball bounces off players
            if ((30 <= self.ball_pos[0] <= 40)
                    and (self.p1_pos <= self.ball_pos[1] <= self.p1_pos + Pong.PLAYER_HEIGHT)):
                relative_intersect = (
                    self.p1_pos + Pong.PLAYER_HEIGHT/2) - self.ball_pos[1]
                normalised_relative_intersect = relative_intersect / \
                    (Pong.PLAYER_HEIGHT / 2)
                bounce_angle = normalised_relative_intersect * Pong.MAX_BOUNCE_ANGLE
                self.ball_vx = Pong.BALL_SPEED * math.cos(bounce_angle)
                self.ball_vy = - Pong.BALL_SPEED * math.sin(bounce_angle)

            elif (460 <= self.ball_pos[0] <= 470
                    and (self.p2_pos <= self.ball_pos[1] <= self.p2_pos + Pong.PLAYER_HEIGHT)):
                relative_intersect = (
                    self.p2_pos + Pong.PLAYER_HEIGHT/2) - self.ball_pos[1]
                normalised_relative_intersect = relative_intersect / \
                    (Pong.PLAYER_HEIGHT / 2)
                bounce_angle = normalised_relative_intersect * Pong.MAX_BOUNCE_ANGLE
                self.ball_vx = - Pong.BALL_SPEED * math.cos(bounce_angle)
                self.ball_vy = - Pong.BALL_SPEED * math.sin(bounce_angle)

            # if ball off screen reset and update score
            if (self.ball_pos[0] <= 0):
                self.ball_pos = (250, 250)
                self.ball_vx = self.BALL_SPEED / 2
                self.ball_vy = 0
                self.p2_score += 1
            elif (self.ball_pos[0] >= 499):
                self.ball_pos = (250, 250)
                self.ball_vx = -self.BALL_SPEED / 2
                self.ball_vy = 0
                self.p1_score += 1

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
                (int(self.ball_pos[0] - Pong.BALL_SIZE/2),
                    int(self.ball_pos[1] - Pong.BALL_SIZE/2),
                    Pong.BALL_SIZE,
                    Pong.BALL_SIZE)
            )
            pygame.draw.rect(
                win,
                (255, 255, 255),
                (30, self.p1_pos, Pong.PLAYER_WIDTH, Pong.PLAYER_HEIGHT))
            pygame.draw.rect(
                win,
                (255, 255, 255),
                (460, self.p2_pos, Pong.PLAYER_WIDTH, Pong.PLAYER_HEIGHT))

            p1_text = font.render(str(self.p1_score), True, (255, 255, 255))
            p2_text = font.render(str(self.p2_score), True, (255, 255, 255))
            win.blit(p1_text, (int(200 - p1_text.get_rect().width/2), 20))
            win.blit(p2_text, (int(300 - p2_text.get_rect().width/2), 20))

            pygame.display.update()

        pygame.font.quit()
        pygame.quit()


if __name__ == "__main__":
    Pong.start()
