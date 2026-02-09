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
                sh 'docker build -t pythonimagetest .'
            }
        }
        stage ('Run') {
            steps {
                sh 'docker run -itd --name python0212 -p 1169:5000 pythonimagetest'
            }
        }
    }
}
