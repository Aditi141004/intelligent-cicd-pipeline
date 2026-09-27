pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest --junitxml=test-results.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    docker build -t intelligent-cicd-flask . > build.log 2>&1
                    set "BUILD_STATUS=%ERRORLEVEL%"
                    type build.log
                    exit /b %BUILD_STATUS%
                '''
            }
        }
        stage('Generate Build Report') {
            steps {
                bat 'echo Build Successful > build-report.txt'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'build-report.txt', fingerprint: true
        }
    }
}
