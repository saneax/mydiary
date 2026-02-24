pipeline {
    agent any

    environment {
        IMAGE_NAME = "quay.io/saneax/mydiary-ci"
        TAG = "latest"
    }

    stages {
        stage('Prepare CI Image') {
            agent {
                docker {
                    image 'gcr.io/kaniko-project/executor:debug'
                    reuseNode true
                    args '--entrypoint=""'
                }
            }
            environment {
                QUAY_CREDS = credentials('pi-sanjayu-quay-login')
            }
            steps {
                script {
                    // Check if image exists, if not or if Dockerfile changed, we build
                    // For now, we always build if this is the first time setup, 
                    // or you can keep the 'when' block if you prefer.
                    sh """
                    mkdir -p /kaniko/.docker
                    AUTH=\$(echo -n "\${QUAY_CREDS_USR}:\${QUAY_CREDS_PSW}" | base64 | tr -d '\\n')
                    echo "{\\"auths\\":{\\"quay.io\\":{\\"auth\\":\\"\${AUTH}\\"}}}" > /kaniko/.docker/config.json
                    
                    /kaniko/executor \
                        --context "${WORKSPACE}" \
                        --dockerfile "${WORKSPACE}/Dockerfile" \
                        --destination "${IMAGE_NAME}:${TAG}"
                    """
                }
            }
        }

        stage('Run CI') {
            agent {
                docker {
                    image "quay.io/saneax/mydiary-ci:latest"
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
        }
    }
}
