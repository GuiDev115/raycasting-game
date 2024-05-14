from sprite_object import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path='src/resourses/sprites/weapon/shotgun/0.png', scale=0.4, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.image = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale)) for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.image[0].get_width() / 2, HEIGHT - self.image[0].get_height())
        #self.weapon_pos = (WIDTH / 2 - self.image[0].get_width() / 2, HEIGHT / 2 - self.image[0].get_height() / 2)
        
    def draw(self):
        self.game.screen.blit(self.image[0], self.weapon_pos)    
        
    def update(self):
        pass