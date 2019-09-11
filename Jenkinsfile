pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo $mytest success'
      }
    }
  }
  environment {
    mytest = 'pipeline'
  }
}