from pygame import *

SPEED = 4
FPS = 60
WIDTH = 700
HEIGHT = 500

window = display.set_mode((WIDTH, HEIGHT))
logo = image.load('images/ufo.png')
display.set_icon(logo)
display.set_caption('ping-pong')

back_fon = transform.scale(
    image.load('images/galaxy.jpg'),
    (WIDTH, HEIGHT)
)

font.init()
final_font = font.SysFont("Arial", 60)


class GameSprite(sprite.Sprite):
    def __init__(
            self,
            player_image: str,
            x: int,
            y: int,
            speed: int,
            width: int,
            height: int
    ) -> None:
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.width = width
        self.height = height

    def reset(self) -> None:
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self) -> None:
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < HEIGHT - (self.height + 5):
            self.rect.y += self.speed

    def update_l(self) -> None:
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < HEIGHT - (self.height + 5):
            self.rect.y += self.speed


ball = GameSprite(
    player_image='images/asteroid.png',
    x=int(WIDTH / 2),
    y=int(HEIGHT / 2),
    speed=0,
    width=50,
    height=50
)

player_r = Player(
    player_image='images/rocket.png',
    x=615,
    y=200,
    speed=SPEED,
    width=50,
    height=150
)

player_l = Player(
    player_image='images/rocket.png',
    x=30,
    y=200,
    speed=SPEED,
    width=50,
    height=150
)

ball_speed_x = 3
ball_speed_y = 3
timer = time.Clock()
finish = False
game = True

while game:
    for current_event in event.get():
        if current_event.type == QUIT:
            game = False

    if not finish:
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        if ball.rect.y <= 0 or ball.rect.y >= HEIGHT - 50:
            ball_speed_y *= -1
        if sprite.collide_rect(ball, player_l) or sprite.collide_rect(ball, player_r):
            ball_speed_x *= -1

        player_l.update_l()
        player_r.update_r()

        window.blit(back_fon, (0, 0))

        if ball.rect.x <= 0:
            lose_text = final_font.render('LEFT PLAYER LOSE', True, (180, 0, 0))
            window.blit(lose_text, (110, 210))
            finish = True
        if ball.rect.x >= WIDTH - 50:
            lose_text = final_font.render('RIGHT PLAYER LOSE', True, (180, 0, 0))
            window.blit(lose_text, (110, 210))
            finish = True

        player_l.reset()
        ball.reset()
        player_r.reset()

    display.update()
    timer.tick(FPS)
