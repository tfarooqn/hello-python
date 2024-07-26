pipeline {
    agent {
      docker {
        image 'python' 
        label 'built-in'
      }
    }
    // tools {
    //     maven 'jnlp-agent-maven'
    // }
    // agent {
    //     label 'kubelet_new_cluster'
    // }
    // agent { any { image 'python' } }
    stages {
        stage('Preparation') {
            steps {
                script {
                    env.SERVICE_NAME = "hello-world"
                    env.VERSION="1.0.0"
                    env.TAG_SUFIX=""
                    env.MS_PORT = 41786
                }
            }
        }
        stage("Build Docker Images Docker Registry"){
            when {
                anyOf { 
                    branch 'master'; branch 'develop'; branch 'external'; branch 'external-securized'; branch 'Pre-security'; branch 'external-securized-reroute'; branch 'external-securized-oidc'
                }
            }
            steps {
                echo "Building Docker Image"
                script {
                    sh 'docker build -t localhost:32000/espadin_tfarooqn_python_prueba .'
                    // sh 'docker build -t localhost:32000/'+ ${SERVICE_NAME}+':'+${VERSION} + ' .'
                    // def app
                    // app = docker.build("localhost:32000/${SERVICE_NAME}:${VERSION}" + env.TAG_SUFIX ,  "--build-arg MS_PORT="+ env.MS_PORT+" .")
                    // echo "Finished build images"
                    // app.push()
                }
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
