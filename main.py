from causal_world.envs import CausalWorld
from causal_world.task_generators import generate_task
task = generate_task(task_generator_id='general')
env = CausalWorld(task=task, enable_visualization=False)
for _ in range(10):
  env.reset()
  for _ in range(100):
      obs, reward, done, info = env.step(env.action_space.sample())
env.close()

