# Personalized Student Recommendations
![Screenshot 2025-02-02 220128](https://github.com/user-attachments/assets/cb9e551a-5355-4fc7-8807-cdb713c044be)

https://github.com/user-attachments/assets/8a024cd8-8ac2-45d8-99d6-ffa60fda2de6

## Overview
The Personalized Student Recommendations project leverages quiz performance data to generate insightful feedback and tailored study recommendations for students preparing for competitive exams. By analyzing both recent and historical quiz attempts, the system identifies performance gaps, tracks improvement trends, and provides actionable suggestions to enhance student learning outcomes.

## Features
- **Performance Analysis**: Evaluates quiz responses to identify strengths and weaknesses.
- **Personalized Insights**: Highlights improvement trends and knowledge gaps.
- **Recommendation Engine**: Suggests topics, question types, and difficulty levels for focused study.
- **Visual Reports**: Generates insightful charts and summaries.
- **Predictive Modeling (Bonus)**: Estimates potential NEET exam rank based on historical data.

## Data Sources
The system processes two key datasets:
1. **Current Quiz Data**: Contains details of a student's most recent quiz submission.
2. **Historical Quiz Data**: Aggregates performance data from the last five quizzes for each student.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Git

### Steps to Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the setup script:
   ```bash
   bash setup.sh
   ```
4. Execute the main script:
   ```bash
   python main.py
   ```

## Methodology
1. **Data Processing**: 
   - Load and preprocess quiz data.
   - Perform statistical analysis on student performance.
2. **Insight Generation**:
   - Detect weak areas and knowledge gaps.
   - Track improvement trends over time.
3. **Personalized Recommendations**:
   - Suggest study materials and topic-wise improvements.
   - (Optional) Predict NEET rank based on historical performance.

## Usage
To analyze a specific student's performance, run:
```bash
python main.py 
```

## Expected Outputs
- **Visual Reports**: Charts highlighting student performance.
- **Text-Based Insights**: Actionable study recommendations.
- **Predictive Analysis**: Estimated ranking based on past trends (if enabled).

## License
This project is licensed under the MIT License.

## Contact
For any queries or contributions, please reach out via [GitHub Issues](https://github.com/quiz_analytics_project/issues).

