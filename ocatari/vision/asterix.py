from .utils import find_objects
from .game_objects import GameObject

objects_colors = {'player': [187, 187, 53],
                  'cauldron': [167, 26, 26],  # two colors: 167, 26, 26 / 184, 50, 50

                  'enemy': [228, 111, 111],
                  'score': [187, 187, 53],
                  'lives': [187, 187, 53],

                  # new not edited objects:
                  'bounty': [198, 89, 179],  # bounty or prize or bonus
                  # make min_distance for bounty bigger cause of more than one color in this and you are
                  # taking the borders, so you have all the object in the rectangle

                  }  # it still not all objects covered


class Player(GameObject):  # player could be shown over all enemies/other objects (see Figure_4.png)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 187, 187, 53


class Cauldron(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 184, 50, 50


class Enemy(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 228, 111, 111


class Score(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 187, 187, 53


class Lives(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 187, 187, 53


class Bounty(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 198, 89, 179


# initialize new classes for new covered objects


# TODO
def _detect_objects_asterix(objects, obs, hud=False):
    objects.clear()

    player = find_objects(obs, objects_colors["player"], maxy=160)  # enemy has same color
    #  if___:  # we need some if?
    for instance in player:
        objects.append(Player(*instance))
    # objects.append(player)

    cauldron = find_objects(obs, objects_colors["cauldron"], closing_dist=6)
    for instance in cauldron:
        objects.append(Cauldron(*instance))

    enemy = find_objects(obs, objects_colors["enemy"], closing_dist=6)
    for instance in enemy:
        objects.append(Enemy(*instance))

    if hud:
        score = find_objects(obs, objects_colors["score"], closing_dist=1, miny=160, maxy=181)  # min_distance=10) !!
        for instance in score:
            objects.append(Score(*instance))

        lives = find_objects(obs, objects_colors["lives"], min_distance=1, miny=181)
        for instance in lives:
            objects.append(Lives(*instance))

    bounty = find_objects(obs, objects_colors["bounty"], closing_dist=10)
    for instance in bounty:
        objects.append(Bounty(*instance))

    # print("\n", len(objects), "elements in objects:")
    # print(*objects, sep="\n")
    # print("\n\n")
