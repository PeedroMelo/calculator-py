pipeline {
  agent { docker { image 'python:latest' } }

  triggers {
    pollSCM('* * * * *')
  }

  stages {
    stage("Compile") {
      steps {
        echo "Compiled"
      }
    }
    stage("Unit test") {
      steps {
        sh "python -m unittest calculator-test.SimpleTest.test"
      }
    }
  }
}