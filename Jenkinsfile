pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/mohitjaiin/python-flask-app.git' // Change this to your repository URL
        BRANCH = 'main'
    }
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out the repository..."
                git branch: "${BRANCH}", url: "${GIT_REPO}"
            }
        }
        stage('Build') {
            steps {
                echo "Setting up virtual environment..."
                script {
                    // Create virtual environment
                    sh 'python3 -m venv venv'

                    // Install dependencies
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                echo "Testing the API with curl..."
                script {
                    // Run the Flask app in the background
                    sh 'nohup ./venv/bin/python app.py &'
                    
                    // Wait for the server to start (add some sleep if necessary)
                    sleep 30
                    
                    // Perform the curl test
                    def response = sh(script: 'curl -s http://localhost:5000/status/operation', returnStdout: true).trim()
                    echo "API Response: ${response}"
                    
                    // Validate the response
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
                echo "Deploying the application..."
                script {
                    // Build Docker image
                    sh 'docker build -t python-flask-app .'
                    
                    // Run the Docker container
                    sh 'docker run -d -p 5000:5000 python-flask-app'
                }
            }
        }
        stage('Run Application') {
            steps {
                echo "Running the application..."
                script {
                    // Verify the application is running with curl
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
