from pygame import *

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
    def update(self) -> None:
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < WIDTH - (self.width + 5):
            self.rect.x += self.speed


timer = time.Clock()
finish = False
game = True

while game:
    for current_event in event.get():
        if current_event.type == QUIT:
            game = False

    window.blit(back_fon, (0, 0))

    display.update()
    timer.tick(FPS)
