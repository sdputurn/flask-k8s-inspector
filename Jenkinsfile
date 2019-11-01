pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh "pip install -r requirements.txt"
                sh "whoami"
                sh "echo $(pwd) +++++ ${BUILD_NUMBER} > ${BUILD_NUMBER}.txt"
                sh "ls -ltr"
                
            }
        }
    }
}
