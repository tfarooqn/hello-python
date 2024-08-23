pipeline {
    agent any
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
                    env.VERSION="1.0.1"
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
                container('dind') {
                    echo "Building Docker Image"
                    script {
                        // sh 'docker build -t localhost:32000/espadin_tfarooqn_python_prueba .'
                        // sh 'docker build -t localhost:32000/'+ ${SERVICE_NAME}+':'+${VERSION} + ' .'
                        sh 'ls -la /var/run/'
                        // sh 'sleep 120' //seconds
                        sh 'docker images'
                        docker.withRegistry("http://192.168.48.1:32000") {
                            def app
                            app = docker.build("192.168.48.1:32000/${SERVICE_NAME}:${VERSION}" + env.TAG_SUFIX ,  "--build-arg MS_PORT="+ env.MS_PORT+" .")
                            // sh 'sleep 600' //seconds
                            app.push()
                        }
                        echo "Finished build images"
                    }
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
