pipeline {
    agent { any { image 'python' } }
    stages {
        stage('build') {
            steps {
                sh 'echo "build"'
            }
        }
        stage('test') {
            steps {
                sh 'echo "test"'
            }
        }
        stage('deploy') {
            steps {
                sh 'echo "deploy"'
            }
        }
    }
}