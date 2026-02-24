pipeline {
    agent {
        docker {
            image 'quay.io/saneax/mydiary-ci:latest'
            reuseNode true
        }
    }

    stages {
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
        success {
            echo "Build successful! Voting +1"
            // If using GitHub: setGitHubPullRequestStatus(context: 'ci/tests', message: 'Passed')
        }
        failure {
            echo "Build failed! Voting -1"
            // If using GitHub: setGitHubPullRequestStatus(context: 'ci/tests', message: 'Failed')
        }
        always {
            deleteDir()
        }
    }
}
