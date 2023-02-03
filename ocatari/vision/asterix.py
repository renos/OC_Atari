from .utils import find_objects, find_mc_objects
from .game_objects import GameObject

objects_colors = {'player': [187, 187, 53],
                  'enemy': [[228, 111, 111], [184, 50, 50]],
                  'score': [187, 187, 53],
                  'lives': [187, 187, 53],

                  # next color is inner one
                  'reward_50': [[198, 89, 179], [127, 92, 213], [170, 170, 170]],
                  'reward_100': [[135, 183, 84], [213, 130, 74], [170, 170, 170]],  # helmet
                  'reward_200': [[195, 144, 61], [84, 138, 210], [170, 170, 170]],  # shield
                  'reward_300': [[213, 130, 74], [84, 92, 214], [170, 170, 170]],  # lamp
                  'reward_400': [[135, 183, 84], [214, 92, 92], [170, 170, 170]],  # apple
                  'reward_500': [[163, 57, 21], [164, 89, 208], [170, 170, 170]],  # fish, meat and mug

                  # next objects are which meant with reward
                  'cauldron': [[167, 26, 26], [184, 50, 50]],
                  'helmet': [[240, 128, 128], [236, 236, 236], [214, 214, 214], [192, 192, 192], [170, 170, 170]],
                  'shield': [214, 214, 214],
                  'lamp': [[187, 53, 53], [214, 214, 214]],
                  'apple': [[184, 50, 50], [110, 156, 66]],  # red and green. 110, 156, 66 is for green
                  'fish': [198, 89, 179],
                  'meat': [[184, 50, 50], [214, 214, 214]],  # 214, 214, 214 for small white part
                  'mug': [[184, 50, 50], [214, 214, 214]]  # like meat. how to differ?

                  # multicolor objects. should we give all contained colores or just what makes obj unique
                  # '50_reward': [[170, 170, 170], [127, 92, 213], [198, 89, 179]]
                  }


class Player(GameObject):  # player could be shown over all enemies/other objects (see Figure_4.png)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 187, 187, 53


# code for not much classes reward
# cause they are not important for the agent
# class Reward(GameObject):
#     def __init__(self, num, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.rgb = [
#             (198, 89, 179),  # , [127, 92, 213]],
#             (135, 183, 84),  # , [213, 130, 74]],
#             (195, 144, 61),  # [84, 138, 210]],
#             (213, 130, 74),  # [84, 92, 214]],
#             (135, 183, 84),  # [214, 92, 92]],
#             (163, 57, 21)  # [164, 89, 208]]
#         ][num - 1]
#         # self.value = num


class Cauldron(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 167, 26, 26  # , [184, 50, 50]]


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


class Helmet(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 240, 128, 128  # [[240, 128, 128], [236, 236, 236]]


class Shield(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 214, 214, 214


class Lamp(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 187, 53, 53


class Apple(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 184, 50, 50  # [[184, 50, 50], [110, 156, 66]]


class Fish(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 198, 89, 179


class Meat(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 184, 50, 50  # [[184, 50, 50], [214, 214, 214]]


class Mug(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 184, 50, 50  # [[184, 50, 50], [214, 214, 214]]


class Reward50(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 198, 89, 179


class Reward100(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 135, 183, 84


class Reward200(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 195, 144, 61


class Reward300(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 213, 130, 74


class Reward400(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 135, 183, 84


class Reward500(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = 163, 57, 21


def _detect_objects_asterix(objects, obs, hud=False):
    objects.clear()

    player = find_objects(obs, objects_colors["player"], maxy=160, tol_p=20)
    for instance in player:
        objects.append(Player(*instance))

    cauldron = find_mc_objects(obs, objects_colors["cauldron"], closing_dist=2,
                               size=(7, 10),  # 7, 10, 3
                               tol_s=4)  # don't change size and tol_s! otherwise lines in enemy are cauldrons
    for instance in cauldron:
        objects.append(Cauldron(*instance))

    enemy = find_mc_objects(obs, objects_colors["enemy"], closing_dist=2)
    for instance in enemy:
        objects.append(Enemy(*instance))

    reward50 = find_mc_objects(obs, objects_colors["reward_50"], min_distance=3, closing_dist=3, miny=24, maxy=151,
                               size=(6, 11))  # , tol_s=3
    for instance in reward50:
        objects.append(Reward50(*instance))

    reward100 = find_mc_objects(obs, objects_colors["reward_100"], min_distance=3, closing_dist=3, miny=24, maxy=151,
                                size=(8, 11), )
    for instance in reward100:
        objects.append(Reward100(*instance))

    reward200 = find_mc_objects(obs, objects_colors["reward_200"], min_distance=3, closing_dist=3, miny=24, maxy=151,
                                size=(8, 11), )
    for instance in reward200:
        objects.append(Reward200(*instance))

    reward300 = find_mc_objects(obs, objects_colors["reward_300"], min_distance=3, closing_dist=3, miny=24, maxy=151,
                                size=(8, 11), )
    for instance in reward300:
        objects.append(Reward300(*instance))

    reward400 = find_mc_objects(obs, objects_colors["reward_400"], min_distance=3, closing_dist=3, miny=24, maxy=151,
                                size=(8, 11), )
    for instance in reward400:
        objects.append(Reward400(*instance))

    reward500 = find_mc_objects(obs, objects_colors["reward_500"], min_distance=3, closing_dist=3, miny=24, maxy=151,
                                size=(8, 11), )
    for instance in reward500:
        objects.append(Reward500(*instance))

    # code for not much classes from rewards
    # ctr = 1
    # for x in ["reward1", "reward2", "reward3", "reward4", "reward5", "reward6"]:
    #     reward = find_mc_objects(obs, objects_colors[x], min_distance=3, closing_dist=2, miny=24, maxy=151,  # )
    #                              size=(6, 11), tol_s=4)
    #     if reward is not None:
    #         for _ in range(1, 7):
    #             reward = find_mc_objects(obs, objects_colors[x], min_distance=3, closing_dist=2, miny=24, maxy=151,
    #                                      size=(6, 11), tol_s=5)
    #         for instance in reward:
    #             objects.append(Reward(ctr, *instance))
    #         break
    #     ctr += 1

    helmet = find_mc_objects(obs, objects_colors["helmet"], closing_dist=1, min_distance=1, size=(7, 11),
                             tol_s=2)
    for instance in helmet:
        objects.append(Helmet(*instance))

    shield = find_objects(obs, objects_colors["shield"], closing_dist=1, size=(5, 11), tol_s=1, min_distance=2)
    for instance in shield:  # specify size(make it work)
        objects.append(Shield(*instance))

    lamp = find_mc_objects(obs, objects_colors["lamp"], closing_dist=3, size=(8, 11))
    for instance in lamp:
        objects.append(Lamp(*instance))

    apple = find_mc_objects(obs, objects_colors["apple"], closing_dist=2, min_distance=2, size=(8, 11))
    for instance in apple:
        objects.append(Apple(*instance))

    fish = find_objects(obs, objects_colors["fish"], closing_dist=1, min_distance=1,
                        size=(8, 5), tol_s=2, )  # size=(8, 5), tol_s=2,  does it work?
    for instance in fish:
        objects.append(Fish(*instance))

    meat = find_mc_objects(obs, objects_colors["meat"], closing_dist=1, min_distance=1, size=(5, 11)
                           , tol_s=2)  # with size alone, two lines in enemy are meat
    for instance in meat:
        objects.append(Meat(*instance))

    mug = find_mc_objects(obs, objects_colors["mug"], closing_dist=2, min_distance=2, size=(7, 11)
                          , tol_s=2)  # # with size alone, two lines in enemy are
    for instance in mug:
        objects.append(Mug(*instance))

    if hud:
        lives = find_objects(obs, objects_colors["lives"], min_distance=1, miny=160, maxy=181)
        for instance in lives:
            objects.append(Lives(*instance))

        score = find_objects(obs, objects_colors["score"], closing_dist=4, miny=181)  # don't change closing_dist=4
        for instance in score:
            objects.append(Score(*instance))

    # do pars min max y for all
    # print("\nobjects:")
    print(*objects, sep="\n")
    print("\n")
