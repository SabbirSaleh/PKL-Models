pipeline {
    agent any  // Run on any available agent (Jenkins node)

    environment {
        VENV_DIR = "venv"
        PYTHON = "python3"
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    if (!fileExists('security_analysis.py')) {
                        error('❌ Error: security_analysis.py not found!')
                    }
                }
                echo '✅ Code Checkout Done!'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                if [ ! -d "$VENV_DIR" ]; then
                    echo "Creating virtual environment..."
                    python3 -m venv $VENV_DIR
                fi

                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
                echo '✅ Virtual Environment Set Up!'
            }
        }

        stage('Run Security Analysis') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                python3 security_analysis.py
                '''
                echo '✅ Security Analysis Completed!'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
