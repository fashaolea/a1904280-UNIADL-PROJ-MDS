import pandas as pd
import matplotlib.pyplot as plt

# Data without Samples column
data = {
    "Code": [0, 3, 4, 5, 6, 7, 8],
    "FSO RMSE": [1.228, 1.879, 1.344, 1.372, 1.621, 3.536, 1.317],
    "FSO R²": [0.878, 0.947, 0.884, 0.853, 0.859, 0.553, 0.890],
    "RF RMSE": [1.931, 1.344, 0.823, 1.255, 1.629, 0.717, 1.644],
    "RF R²": [0.429, 0.799, 0.756, 0.810, 0.838, 0.781, 0.714],
}

df = pd.DataFrame(data)

# Plotting a table
fig, ax = plt.subplots(figsize=(8, 2 + 0.4*len(df)))
ax.axis('off')
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

plt.tight_layout()
plt.savefig('/mnt/data/generic_model_performance.png', dpi=300, bbox_inches='tight')
plt.show()

