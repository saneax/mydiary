pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install tox'
            }
        }
        stage('Lint') {
            steps {
                sh 'tox -e lint'
            }
        }
        stage('Test') {
            steps {
                sh 'tox -e py3'
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}
