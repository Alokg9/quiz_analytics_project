from quiz_analytics import QuizAnalytics
from visualization import plot_quiz_insights
import pandas as pd

def main():
    # Initialize analytics
    user_id = 123
    analytics = QuizAnalytics()
    results = analytics.analyze_performance(user_id)
    
    # Print analysis results
    print("Analysis Results:")
    print(f"Current Quiz Accuracy: {results['current_accuracy']:.2%}")
    print(f"Historical Average Score: {results['historical_avg']:.2%}")
    print("\nWeak Topics:", results['weak_topics'])
    print("\nRecommendations:")
    for rec in results['recommendations']:
        print(f"- {rec}")
    
    # Create sample data for visualization
    quiz_data = {
        'Topic': ['Physics', 'Math', 'Chemistry', 'Biology'],
        'Accuracy': [65, 78, 82, 71],
        'Difficulty': ['Medium', 'Hard', 'Easy', 'Medium']
    }
    
    # Plot insights
    plot_quiz_insights(quiz_data)

if __name__ == "__main__":
    main()