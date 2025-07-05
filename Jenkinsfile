pipeline {
    agent any

    environment {
        IMAGE_NAME = 'ajay502/login-web-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/AjayKumarBadhan/login-web-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}").run('-p 5000:5000')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    script {
                        docker.image("${IMAGE_NAME}").push('latest')
                    }
                }
            }
        }

        stage('Success') {
            steps {
                echo "✅ Login Application deployed successfully!"
            }
        }
    }
}
