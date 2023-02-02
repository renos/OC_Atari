# appends parent path to syspath to make ocatari importable
# like it would have been installed as a package
import sys
import random
import matplotlib.pyplot as plt
sys.path.insert(0, '../../') # noqa

from ocatari.core import OCAtari
from ocatari.vision.utils import mark_bb, make_darker

game_name = "Kangaroo"
MODE = "vision"
# MODE = "revised"
HUD = True
env = OCAtari(game_name, mode=MODE, hud=HUD, render_mode='rgb_array')
observation, info = env.reset()
# env._env.unwrapped.ale.setRAM(36, 2)

for i in range(1000):
    # if i < 105:
    #     obs, reward, terminated, truncated, info = env.step(3)
    # else:
    obs, reward, terminated, truncated, info = env.step(0)  # env.step(6) for easy movement
    # env._env.unwrapped.ale.setRAM(43, 6)
    # env._env.unwrapped.ale.setRAM(11, 10)
    if i % 10 == 0 and i > 100:
        # obse2 = deepcopy(obse)
        print(env.objects)
        for obj in env.objects:
            x, y = obj.xy
            if x < 160 and y < 210 and obj.visible:
                opos = obj.xywh
                ocol = obj.rgb
                sur_col = make_darker(ocol)
                mark_bb(obs, opos, color=sur_col)
            # mark_point(obs, *opos[:2], color=(255, 255, 0))

        plt.imshow(obs)
        plt.show()

    if terminated or truncated:
        observation, info = env.reset()
    # modify and display render
env.close()
