pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    if (fileExists('Jenkinsfile')) {
                        echo '✅ Code Checkout Done!'
                    } else {
                        error '❌ Jenkinsfile not found!'
                    }
                }
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                [ ! -d venv ] && echo "Creating virtual environment..." && python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Security Analysis') {
            steps {
                sh '''
                . venv/bin/activate
                python3 security_analysis.py
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed!'
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
    }
}
