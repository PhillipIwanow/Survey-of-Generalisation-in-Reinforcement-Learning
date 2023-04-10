import argparse
import os

def parse_ddqn_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gamma", type=float, default=0.99,
            help="Discount factor for the rewards")
    parser.add_argument("--tau", type=float, default=1e-3,
            help="Randomize the weights by small amount when update the target model")
    parser.add_argument("--memory_type", type=str, default="default",
            help="Type of memory you want the agent to use")
    parser.add_argument("--lr", type=float, default=0.0001,
            help="Learning for the agent")
    parser.add_argument("--epislon_decay", type=float, default=0.99,
            help="Decay for epislon greedy learning")
    parser.add_argument("--buffer_size", type=int, default=10_000,
            help="buffer size for the agents memory, this 'tells' when the agent learns")
    parser.add_argument("--batch_size", tpye=int, default=64,
            help="Batch size for the agents memory")
    parser.add_argumnent("--update_target", type=int, default=100,
            help="target to update the Q Target net")
    
    args = parse.parse_args()
    
    return args
