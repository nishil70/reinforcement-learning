# Reinforcement Learning
Learning from interaction is a foundational idea underlying nearly all theories of learning and intelligence.
Funadamental idea in reinforcement learning is:
- Learning what to do
  - how to map situations to actions so as to maximize a numerical reward
- Learner is not told which actions to take
  - must discover which actions yield the most reward by trying them


## Contributors
- Nishil Parmar

## Implementions
- Q-learning approach
- Treasure hunting

## Approach
- The reason i selected Q-learning algorithm is because it is one of the most popular approach in reinforcement learning
- The goal of Q-learning is to learn a policy, which tells an agent what action to take under what circumstances
- It can handle problems with stochastic transitions and rewards, without requiring adaptations.
- Q-learning finds a policy that is optimal in the sense that it maximizes the expected value of the total reward over any and all successive steps, starting from the current state
- "Q" names the function that returns the reward used to provide the reinforcement and can be said to stand for the "quality" of an action taken in a given state

## Project Files
- [Treasure hunting demonstration](https://github.com/nishil70/reinforcement-learning/blob/master/notebooks/treasure-hunting.ipynb)
- [Q-learning helper](https://github.com/nishil70/reinforcement-learning/blob/master/notebooks/qlearning.py)


## References
- Richard S. Sutton and Andrew G.Barto - Reinforcement Learning: An Introduction
- https://medium.freecodecamp.org/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc
- https://medium.com/@curiousily/solving-an-mdp-with-q-learning-from-scratch-deep-reinforcement-learning-for-hackers-part-1-45d1d360c120
