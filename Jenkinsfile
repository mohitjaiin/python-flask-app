pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/mohitjaiin/python-flask-app.git'
        BRANCH = 'main'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: "${BRANCH}", url: "${GIT_REPO}"
            }
        }
        stage('Build') {
            steps {
                script {
                    echo "Setting up virtual environment..."
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                    sh './venv/bin/pip install pytest'  // Install pytest in virtual environment
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    sh './venv/bin/pytest tests/'  // Run tests using virtual environment's pytest
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                    sh 'docker build -t python-flask-app .'
                    sh 'docker run -d -p 5000:5000 python-flask-app'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    echo "Running the application..."
                    sh 'curl http://localhost:5000/status/operation'
                }
            }
        }
    }
    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
