# main.py

import gym
import env  # Custom environment
from agent import QLearningAgent  # Import the QLearningAgent class

# Create the environment
env = gym.make("AppleOfFortune-v0")

# Create the Q-learning agent
num_states = env.observation_space.n  # Ensure you have the correct state space size
num_actions = env.action_space.n

agent = QLearningAgent(num_states, num_actions)

# Training loop
num_episodes = 100

for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        total_reward += reward
        state = next_state

    # Print episode information
    print(f"Episode {episode + 1}/{num_episodes}")
    print(f"Total Reward: {total_reward}")

    # Render the environment in 'ansi' mode
    rendered_env = env.render(mode='ansi')
    print(rendered_env)
