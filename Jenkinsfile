pipeline {
    agent {
        docker { image 'node:20.15.1-alpine3.20' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}