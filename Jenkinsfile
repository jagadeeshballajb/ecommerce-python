pipeline {
    agent any
    environment {
        IMAGE_NAME = "jagadeeshballajb/pythonimagetest1"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        FULL_IMAGE = "${IMAGE_NAME}:${IMAGE_TAG}"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jagadeeshballajb/ecommerce-python.git'
            }
        }
        stage ('Docker Image Build') {
            steps {
                sh 'docker build -t ${FULL_IMAGE} .'
                
            }
        }
        stage ('Log In to Doceker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credls',
                    usernameVariable: 'DOCKER_USER' ,
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    //sh """
                    //echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    //"""
                }
            }

        }
        stage ('Push Image') {
            steps {
                sh "docker push ${FULL_IMAGE}"
                sh "docker tag ${FULL_IMAGE} ${IMAGE_NAME}:latest"
                sh "docker push ${IMAGE_NAME}:latest"
            }

        }
        stage ('deploy'){
            steps {
                sh 'docker rm -f python02121 || true'
                sh 'docker run -itd --name python02121 -p 5000:5000 ${IMAGE_NAME}:latest'
                sh "echo ${env.BUILD_NUMBER}"
                sh "echo ${FULL_IMAGE}"
                sh "echo ${IMAGE_NAME}"
                sh "echo ${env.BUILD_NUMBER}"

            }
        }
    }
}
