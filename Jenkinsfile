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
                sh 'docker build -t pythonimage201 .'
            }
        }
        stage ('Run') {
            steps {
                sh 'docker run -itd --name python021 -p 1161:5000 pythonimage201'
            }
        }
    }
}
