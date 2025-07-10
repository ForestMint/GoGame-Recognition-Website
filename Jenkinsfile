pipeline {
    agent any
    environment {
        VM_HOST = 'your.vm.ip.address'
        VM_USER = 'your-username'
        SSH_CREDENTIALS = 'vm-ssh-key'
        IMAGE_NAME = 'flaskapp'
        IMAGE_TAG = "latest"
        DEPLOY_DIR = '/home/your-username'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'git@github.com:youruser/your-flask-repo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }
        stage('Deploy to VM') {
            steps {
                sshagent([SSH_CREDENTIALS]) {
                    // Save and copy image to VM or push to Docker registry (if any)
                    sh """
                    docker save ${IMAGE_NAME}:${IMAGE_TAG} -o ${IMAGE_NAME}.tar
                    scp -o StrictHostKeyChecking=no ${IMAGE_NAME}.tar ${VM_USER}@${VM_HOST}:${DEPLOY_DIR}
                    ssh -o StrictHostKeyChecking=no ${VM_USER}@${VM_HOST} '
                        docker load -i ${DEPLOY_DIR}/${IMAGE_NAME}.tar &&
                        docker stop ${IMAGE_NAME} || true &&
                        docker rm ${IMAGE_NAME} || true &&
                        docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                    '
                    """
                }
            }
        }
    }
}




