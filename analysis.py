import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# =========================
# 1. LOAD EXCEL DATA
# =========================
df = pd.read_excel("data/free_fire_clean_data.xlsx")

print("Original columns:")
print(df.columns.tolist())

# =========================
# 2. CLEAN COLUMN NAMES (FULLY)
# =========================
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("/", "", regex=False)
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("%", "percent", regex=False)
    .str.replace(".", "", regex=False)
)

print("\nCleaned columns:")
print(df.columns.tolist())

# =========================
# 3. BASIC CHECK
# =========================
print("\nData Info:")
print(df.info())

# =========================
# 4. VISUAL SETTINGS
# =========================
sns.set_theme(style="darkgrid")

# =========================
# 5. TIME PLAYED vs KILLS
# =========================
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="time_playedhrs",
    y="kills"
)
plt.title("Time Played vs Kills")
plt.xlabel("Time Played (Hours)")
plt.ylabel("Kills")
plt.tight_layout()
plt.show()

# =========================
# 6. TIME PLAYED vs WINS
# =========================
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="time_playedhrs",
    y="wins"
)
plt.title("Time Played vs Wins")
plt.xlabel("Time Played (Hours)")
plt.ylabel("Wins")
plt.tight_layout()
plt.show()

# =========================
# 7. KD RATIO DISTRIBUTION
# =========================
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="kd_ratio",
    bins=10,
    kde=True
)
plt.title("KD Ratio Distribution")
plt.xlabel("K/D Ratio")
plt.tight_layout()
plt.show()

# =========================
# 8. MODE vs AVG KD RATIO
# =========================
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="mode",
    y="kd_ratio",
    estimator=np.mean
)
plt.title("Average K/D Ratio by Game Mode")
plt.xlabel("Game Mode")
plt.ylabel("Average K/D Ratio")
plt.tight_layout()
plt.show()

# =========================
# 9. OVERALL PERFORMANCE
# =========================
metrics = ["kills", "wins", "kd_ratio", "winpercent"]
overall_avg = df[metrics].mean()

plt.figure(figsize=(8, 5))
overall_avg.plot(kind="bar")
plt.title("Overall Average Performance")
plt.ylabel("Average Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n✅ Analysis completed successfully.")
