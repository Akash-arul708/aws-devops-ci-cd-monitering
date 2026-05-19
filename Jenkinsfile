pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo 'Code pulled from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-flask-app ./app'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f flask-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-app devops-flask-app'
            }
        }
    }
}
