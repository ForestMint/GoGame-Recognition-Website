pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app:latest'
        DEPLOY_SERVER = 'user@your-server-ip'
        DEPLOY_PATH = '/var/www/my-python-app'
        APP_PORT = '8000'  // Change based on your app
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/my-python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m unittest discover tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag $DOCKER_IMAGE $DOCKER_USER/my-python-app:latest
                        docker push $DOCKER_USER/my-python-app:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sshagent(['ssh-deploy-key']) {
                    sh '''
                        ssh $DEPLOY_SERVER '
                            docker pull $DOCKER_USER/my-python-app:latest &&
                            docker stop my-python-app || true &&
                            docker rm my-python-app || true &&
                            docker run -d --name my-python-app -p 80:$APP_PORT $DOCKER_USER/my-python-app:latest
                        '
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Python app deployed successfully!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
