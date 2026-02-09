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
                sh 'docker build -t pythonimage120 .'
            }
        }
        stage ('Run') {
            steps {
                sh 'docker run -itd --name python4 -p 1160:5000 pythonimage120'
            }
        }
    }
}
