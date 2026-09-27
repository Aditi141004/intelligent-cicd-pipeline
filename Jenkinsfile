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
                sh 'python3 --version'
                sh 'python3 -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest --junitxml=test-results.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t intelligent-cicd-flask . > build.log 2>&1
                    build_status=$?
                    cat build.log
                    exit $build_status
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test-results.xml,build.log', allowEmptyArchive: true, fingerprint: true
        }
    }
}
