pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: java
      image: maven:3.8.5-jdk-8
      resources:
        requests:
          memory: '512M'
          cpu: '250m'
        limits:
          memory: '1024M'
          cpu: '1000m'
      command:
        - sleep
      args:
        - 1d
    - name: kaniko
      image: gcr.io/kaniko-project/executor:debug
      resources:
        requests:
          memory: '512M'
          cpu: '250m'
        limits:
          memory: '2048M'
          cpu: '1000m'
      command:
        - /busybox/cat
      tty: true
    - name: helm
      image: alpine/helm
      resources:
        requests:
          memory: '256M'
          cpu: '250m'
        limits:
          memory: '1024M'
          cpu: '1000m'
      command:
        - sleep
      args:
        - 1d
      tty: true
"""
        }
    }
    stages {
        stage('Preparation') {
            steps {
                script {
                    env.SERVICE_NAME = "hello-world"
                    env.VERSION="1.0.1"
                    env.TAG_SUFIX=""
                    env.MS_PORT = 41786
                }
                echo "Starting CI/CD Pipeline name=${env.SERVICE_NAME}"
            }
        }
        stage("Build Docker Images Docker Registry"){
            when {
                anyOf { 
                    branch 'master'; branch 'develop'; branch 'external'; branch 'external-securized'; branch 'Pre-security'; branch 'external-securized-reroute'; branch 'external-securized-oidc'
                }
            }
            // steps {
            //     container('dind') {
            //         echo "Building Docker Image"
            //         script {
            //             // sh 'docker build -t localhost:32000/espadin_tfarooqn_python_prueba .'
            //             // sh 'docker build -t localhost:32000/'+ ${SERVICE_NAME}+':'+${VERSION} + ' .'
            //             sh 'ls -la /var/run/'
            //             // sh 'sleep 120' //seconds
            //             sh 'docker images'
            //             docker.withServer("http://192.168.48.1:32000") {
            //                 def app
            //                 app = docker.build("192.168.48.1:32000/${SERVICE_NAME}:${VERSION}" + env.TAG_SUFIX ,  "--build-arg MS_PORT="+ env.MS_PORT+" .")
            //                 // sh 'sleep 600' //seconds
            //                 app.push()
            //             }
            //             echo "Finished build images"
            //         }
            //     }
            // }

            steps {
                script {
                    container('kaniko') {                        
                        def destinationImage = "${SERVICE_NAME}:${VERSION}"
                        echo "Image will be built as ${destinationImage}"
                        sh "/kaniko/executor -f `pwd`/Dockerfile -c `pwd` --destination=${destinationImage} --build-arg MS_PORT=${env.MS_PORT}"
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
