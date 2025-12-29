pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/pavan1613/selenium-ci-cd.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv %VENV%'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '%VENV%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '%VENV%\\Scripts\\pytest --html=reports/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Test Report'
            ])
        }
    }
}
