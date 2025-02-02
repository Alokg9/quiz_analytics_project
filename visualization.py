import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_quiz_insights(quiz_data):
    df = pd.DataFrame(quiz_data)
    
    plt.style.use('seaborn-v0_8')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # Topic Performance Bar Plot
    sns.barplot(data=df, x='Topic', y='Accuracy', ax=ax1)
    ax1.set_title('Performance by Topic')
    ax1.set_ylabel('Accuracy (%)')
    ax1.tick_params(axis='x', rotation=45)

    # Difficulty Distribution Pie Chart
    difficulty_counts = df['Difficulty'].value_counts()
    ax2.pie(difficulty_counts, labels=difficulty_counts.index, autopct='%1.1f%%')
    ax2.set_title('Distribution of Question Difficulty')

    # Topic vs Difficulty Heatmap
    topic_diff_matrix = pd.crosstab(df['Topic'], df['Difficulty'])
    sns.heatmap(topic_diff_matrix, annot=True, cmap='YlOrRd', ax=ax3)
    ax3.set_title('Topic vs Difficulty Distribution')

    # Performance Trend
    sns.lineplot(data=df, x='Topic', y='Accuracy', markers='o', ax=ax4)
    ax4.set_title('Performance Trend Across Topics')
    ax4.set_ylabel('Accuracy (%)')
    ax4.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()