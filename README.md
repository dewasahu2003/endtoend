# End-to-End Machine Learning Project

## 📊 Project Overview
A comprehensive machine learning project with a complete pipeline from data ingestion to model deployment, featuring modular architecture, MLflow tracking, and Flask web application.

## 🚀 Project Architecture

### Workflow Stages
1. Data Ingestion
2. Data Validation
3. Data Transformation
   - Feature engineering
   - Data preprocessing
   - Feature selection
4. Model Training
5. Model Evaluation

## 🛠 Technologies & Tools
- Python
- MLflow
- DagsHub
- Scikit-learn
- DVC (Data Version Control)
- Flask
- Joblib
- PythonBox

## 📦 Project Structure
```
├── artifacts/             # Output files from pipeline stages
├── logs/                  # Logging directory
├── research/              # Experimental notebooks
├── src/
│   ├── components/        # Workflow components
│   ├── config/            # Configuration management
│   ├── constants/         # Project constants
│   ├── entity/            # Workflow configuration classes
│   ├── pipeline/          # Pipeline implementations
│   └── utils/             # Utility functions
├── templates/             # HTML templates for Flask app
├── app.py                 # Main Flask application
├── config.yaml            # Project configuration
├── params.yaml            # Model parameters
└── schema.yaml            # Data schema
```

## 🔧 Configuration Management
The project uses a centralized configuration approach:
- `config.yaml`: Main configuration file
- Configuration manager creates configurations for all workflows
- Pipelines are dynamically created and run based on these configurations

## 💻 Setup & Installation

### Prerequisites
- Python 3.8+
- Git

### Installation Steps
1. Clone the repository
```bash
git clone https://github.com/dewasahu2003/endtoend.git
cd endtoend
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Update DagsHub Tracking
- Open `src/components/model_evaluation.py`
- Replace DagsHub tracking URI, username, and password

### Running the Application
```bash
python app.py
```

## 🖼 Project Visualization

### Last Experiment on DagsHub
![Last Experiment](https://github.com/user-attachments/assets/fe632241-079c-473d-ba1d-23a8fa692288)

### All Experiments on DagsHub
![All Experiments](https://github.com/user-attachments/assets/e99234fb-8aa0-4c24-81ad-9df6a3a7f5ad)

### Running Prediction on Localhost
![Localhost Running Prediction](https://github.com/user-attachments/assets/f1259b03-9846-41f9-b16a-8b852c1f272e)

### Prediction Results
![Prediction Results](https://github.com/user-attachments/assets/0dac2a1e-62d8-4b9e-9c29-de3618c8f6db)

### Training from Localhost API
![Training from Localhost API](https://github.com/user-attachments/assets/85975ac4-21dd-4dad-92c2-9a1571365e9b)

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact
Your Name - dewasahu200@gmail.com

Project Link: [https://github.com/dewasahu2003/endtoend](https://github.com/dewasahu2003/endtoend)
