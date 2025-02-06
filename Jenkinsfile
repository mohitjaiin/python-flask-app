pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/<your-username>/python-flask-app.git'
        BRANCH = 'master'
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
                    echo "Building the application..."
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    // Add test command here (e.g., pytest)
                    sh 'pytest tests/'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                    // Docker deployment or cloud deployment command
                    sh 'docker build -t python-flask-app .'
                    sh 'docker run -d -p 5000:5000 python-flask-app'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    echo "Running the application..."
                    // Command to ensure the app is running
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
