🎮 **Free Fire Performance Analytics**  
A data analysis project focused on understanding **match-level performance trends** in Free Fire using Python and Excel. This project analyzes gameplay statistics such as **kills, wins, K/D ratio, time played, and game modes** to uncover performance patterns and overall insights.  

🛠 **Tools & Technologies Used**  
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Excel  

📊 **Dataset**  
The dataset contains match-level Free Fire performance data stored in Excel format. Fields included:  
- Date  
- Game Mode  
- Matches Played  
- Wins  
- Kills  
- Deaths  
- Headshots  
- Damage  
- Time Played (Hours)  
- K/D Ratio  
- Win Percentage  
- Headshot Percentage  
- Average Damage  
> ⚠️ **Note:** The dataset does not contain usernames, player IDs, or any personal information and is safe to include in this repository.  

📈 **Analysis Performed**  
The following analyses are performed using Python:  
- 🔹 Scatter plot: Time Played vs Kills  
- 🔹 Scatter plot: Time Played vs Wins  
- 🔹 Histogram: K/D Ratio distribution with KDE  
- 🔹 Bar plot: Average K/D Ratio by Game Mode  
- 🔹 Bar plot: Overall Average Performance Metrics (Kills, Wins, K/D Ratio, Win Percentage)  
> All visualizations are generated using Matplotlib and Seaborn.  

▶️ **How to Run the Project**  
- Install Python (version 3.9 or above recommended)  
- Install required libraries: `pip install pandas numpy matplotlib seaborn`  
- Ensure folder structure:
  repo_root/
├─ Data/
│ └─ free_fire_clean_data.xlsx
├─ analysis.py

✅ Make sure the Excel file is placed inside the Data folder in the root of the repository.  
- Run the analysis script: `python analysis.py`  
- Output: Plots will appear sequentially for each analysis, cleaned column names and data info will print in the console. If the Excel file or required columns are missing, the script will show a friendly error message.  

✅ This setup ensures that the code runs smoothly and safely for anyone cloning the repository.

