pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jagadeeshballajb/ecommerce-python.git'
            }
        }
        stage ('Build') {
            steps {
                sh 'docker build -t pythonimagetest1 .'
            }
        }
        stage ('Run') {
            steps {
                sh 'docker rm -f python02121 || true'
                sh 'docker run -itd --name python02121 -p 1170:5000 pythonimagetest1'
            }
        }
    }
}
