pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh "pwd "
                sh "touch abc.txt"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.txt', fingerprint: true
        }
    }
}
