import requests
import pandas as pd
import json

class QuizAnalytics:
    def __init__(self):
        self.current_quiz_endpoint = "https://jsonkeeper.com/b/LLQT"
        self.historical_endpoint = "https://api.jsonserve.com/XgAgFJ"
        
    def get_current_quiz_data(self, user_id):
        # Simulated response
        return {
            'user_id': user_id,
            'questions': [
                {
                    'question_id': 1,
                    'topic': 'Physics',
                    'difficulty': 'Medium',
                    'selected_option': 'A',
                    'correct_option': 'B'
                },
                {
                    'question_id': 2,
                    'topic': 'Math',
                    'difficulty': 'Hard',
                    'selected_option': 'C',
                    'correct_option': 'C'
                },
                {
                    'question_id': 3,
                    'topic': 'Chemistry',
                    'difficulty': 'Easy',
                    'selected_option': 'B',
                    'correct_option': 'B'
                },
                {
                    'question_id': 4,
                    'topic': 'Biology',
                    'difficulty': 'Medium',
                    'selected_option': 'A',
                    'correct_option': 'D'
                }
            ]
        }
    
    def get_historical_data(self, user_id):
        return {
            'user_id': user_id,
            'quiz_history': [
                {
                    'quiz_id': 1,
                    'score': 75.0,
                    'topics': ['Physics', 'Math', 'Chemistry', 'Biology'],
                    'response_map': {'1': 'A', '2': 'B', '3': 'B', '4': 'A'}
                }
            ]
        }
    
    def analyze_performance(self, user_id):
        current_data = self.get_current_quiz_data(user_id)
        historical_data = self.get_historical_data(user_id)
        
        current_accuracy = sum(
            1 for q in current_data['questions'] 
            if q['selected_option'] == q['correct_option']
        ) / len(current_data['questions'])
        
        historical_scores = [quiz['score'] for quiz in historical_data['quiz_history']]
        avg_historical_score = sum(historical_scores) / len(historical_scores)
        
        return {
            'current_accuracy': current_accuracy,
            'historical_avg': avg_historical_score,
            'weak_topics': self.identify_weak_topics(current_data),
            'recommendations': self.generate_recommendations(current_data, historical_data)
        }
    
    def identify_weak_topics(self, current_data):
        topic_performance = {}
        for question in current_data['questions']:
            topic = question['topic']
            is_correct = question['selected_option'] == question['correct_option']
            if topic not in topic_performance:
                topic_performance[topic] = {'correct': 0, 'total': 0}
            topic_performance[topic]['total'] += 1
            if is_correct:
                topic_performance[topic]['correct'] += 1
        
        weak_topics = [
            topic for topic, perf in topic_performance.items()
            if (perf['correct'] / perf['total']) < 0.6
        ]
        return weak_topics
    
    def generate_recommendations(self, current_data, historical_data):
        recommendations = []
        weak_topics = self.identify_weak_topics(current_data)
        
        for topic in weak_topics:
            recommendations.append(f"Focus on improving {topic} with additional practice")
            
        avg_score = sum(quiz['score'] for quiz in historical_data['quiz_history']) / len(historical_data['quiz_history'])
        if avg_score < 60:
            recommendations.append("Consider seeking additional help through tutoring")
            
        return recommendations