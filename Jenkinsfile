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
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo "Testing the API with curl..."
                    // Make a GET request to the /status/operation endpoint
                    def response = sh(script: 'curl -s http://localhost:5000/status/operation', returnStdout: true).trim()
                    echo "API Response: ${response}"
                    
                    // Check if the response matches expected output
                    if (response == '{"health": "All systems operational"}') {
                        echo "Test Passed"
                    } else {
                        error "Test Failed: Unexpected response"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                    // Build the Docker image and run it
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
