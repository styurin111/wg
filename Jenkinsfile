pipeline {
    agent any
    stages {
        stage('Запуск скрипта') {
            steps {
                sh "python3 make_config.py tyurin fd42:1001::28/128"
            }
        }
    }
}