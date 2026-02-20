/*
 * Pipeline Jenkins - Calculadora Python
 * Projeto: Segurança e Auditoria de Sistemas
 *
 * Stages:
 *   1. Checkout do código
 *   2. Instalar dependências
 *   3. Rodar testes unitários
 *   4. Build do executável (PyInstaller)
 *   5. Gerar instalador (Inno Setup)
 *   6. Arquivar artefatos
 */

pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo '📥 Fazendo checkout do código...'
                checkout scm
            }
        }

        stage('Instalar Dependências') {
            steps {
                echo '📦 Instalando dependências do projeto...'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Testes Unitários') {
            steps {
                echo '🧪 Executando testes unitários...'
                bat 'python -m pytest test_calculadora.py -v --tb=short'
            }
        }

        stage('Build Executável') {
            steps {
                echo '🔨 Gerando executável com PyInstaller...'
                bat 'python -m PyInstaller --onefile --windowed --name Calculadora --clean calculadora.py'
            }
        }

        stage('Gerar Instalador') {
            steps {
                echo '📀 Gerando instalador com Inno Setup...'
                bat '"C:\\Program Files (x86)\\Inno Setup 6\\ISCC.exe" instalador.iss'
            }
        }

        stage('Arquivar Artefatos') {
            steps {
                echo '📁 Arquivando instalador gerado...'
                archiveArtifacts artifacts: 'Output/CalculadoraSetup.exe', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline concluído com sucesso! Instalador gerado.'
        }
        failure {
            echo '❌ Pipeline falhou. Verifique os logs acima.'
        }
        always {
            echo '🧹 Limpeza pós-build...'
            cleanWs(cleanWhenNotBuilt: false)
        }
    }
}
