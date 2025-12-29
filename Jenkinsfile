pipeline {
    agent any

    tools {
        python 'Python39'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat',
                    url: 'https://github.com/pavan1613/selenium-ci-cd.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '.venv\\Scripts\\pytest --html=reports/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Test Report'
            ])
        }
    }
}
