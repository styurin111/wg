pipeline {
    agent any
     
    stages {
        stage('Build') {
            steps {
                sh 'python3 make_config.py'
            }
        }
    }
}