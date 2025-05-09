import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set the style for the plot
# plt.style.use('seaborn-whitegrid')
# sns.set_palette("pastel")

# Data from the tables
minimax_data = [
    {'depth': 2, 'human': 21, 'bot': 27, 'winner': 'bot'},
    {'depth': 3, 'human': 16, 'bot': 32, 'winner': 'bot'},
    {'depth': 4, 'human': 15, 'bot': 33, 'winner': 'bot'}
]

alpha_beta_data = [
    {'depth': 2, 'human': 26, 'bot': 22, 'winner': 'human'},
    {'depth': 3, 'human': 17, 'bot': 31, 'winner': 'bot'},
    {'depth': 4, 'human': 16, 'bot': 32, 'winner': 'bot'}
]

expectimax_data = [
    {'depth': 2, 'human': 32, 'bot': 16, 'winner': 'human'},
    {'depth': 3, 'human': 25, 'bot': 23, 'winner': 'human'},
    {'depth': 4, 'human': 23, 'bot': 25, 'winner': 'bot'}
]

# Create dataframes
minimax_df = pd.DataFrame(minimax_data)
alpha_beta_df = pd.DataFrame(alpha_beta_data)
expectimax_df = pd.DataFrame(expectimax_data)

# Calculate score differences
minimax_df['diff'] = minimax_df['bot'] - minimax_df['human']
alpha_beta_df['diff'] = alpha_beta_df['bot'] - alpha_beta_df['human']
expectimax_df['diff'] = expectimax_df['bot'] - expectimax_df['human']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors
# minimax_color = '#9b8ee0'      # Purple
# alpha_beta_color = '#8fd1a8'    # Green
# expectimax_color = '#ffd373'    # Yellow

# Plot Minimax (circles)
ax.scatter(minimax_df['depth'], minimax_df['bot'], 
          #  color=minimax_color, 
           marker='o', 
           label='Minimax', 
           alpha=0.8, 
           edgecolor='white',
           linewidth=1)
ax.plot(minimax_df['depth'], minimax_df['bot'], 
        # color=minimax_color, 
        linewidth=2, 
        alpha=0.7)

# Plot Alpha-Beta Pruning (squares)
ax.scatter(alpha_beta_df['depth'], alpha_beta_df['bot'], 
          #  color=alpha_beta_color, 
           marker='s', 
           label='Alpha-Beta Pruning', 
           alpha=0.8, 
           edgecolor='white',
           linewidth=1)
ax.plot(alpha_beta_df['depth'], alpha_beta_df['bot'], 
        # color=alpha_beta_color, 
        linewidth=2, 
        alpha=0.7)

# Plot Expectimax (diamonds)
ax.scatter(expectimax_df['depth'], expectimax_df['bot'], 
          #  color=expectimax_color, 
           marker='D', 
           label='Expectimax', 
           alpha=0.8, 
           edgecolor='white',
           linewidth=1)
ax.plot(expectimax_df['depth'], expectimax_df['bot'], 
        # color=expectimax_color, 
        linewidth=2, 
        alpha=0.7)

# Set y-axis limits to match the image
ax.set_ylim(10, 35)
ax.set_xlim(1.5, 4.5)

# Set the ticks
ax.set_xticks([2, 3, 4])
ax.set_yticks([10, 17, 24, 35])

# Add labels and title
ax.set_xlabel('Max Search Depth', fontsize=14)
ax.set_ylabel('Bot Score', fontsize=14)
ax.set_title('Bot Performance by Algorithm and Search Depth', fontsize=16)

# Customize the legend
ax.legend(fontsize=14, 
          title='', 
          frameon=False, 
          loc='lower center', 
          ncol=3, 
          bbox_to_anchor=(0.5, -0.13))

# Add grid lines
ax.grid(True, linestyle='--', alpha=0.7)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Save and show the plot
plt.tight_layout()
plt.savefig('mancala_algorithm_performance.png', dpi=300, bbox_inches='tight')
plt.show()