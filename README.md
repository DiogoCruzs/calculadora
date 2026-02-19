# 🧮 Calculadora Python

**Projeto acadêmico** — Segurança e Auditoria de Sistemas (ADS)

Calculadora simples com interface gráfica, pipeline CI/CD com Jenkins e instalador Windows com Inno Setup.

---

## 📋 Estrutura do Projeto

```
├── calculadora.py          # Aplicação principal (Tkinter)
├── test_calculadora.py     # Testes unitários
├── Jenkinsfile             # Pipeline CI/CD
├── instalador.iss          # Script do instalador (Inno Setup)
├── requirements.txt        # Dependências Python
└── README.md               # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10+
- Inno Setup 6 (para gerar o instalador)
- Jenkins (para o pipeline)

### Rodar a calculadora
```bash
python calculadora.py
```

### Rodar os testes
```bash
python -m pytest test_calculadora.py -v
```

---

## ⚙️ Pipeline Jenkins

O `Jenkinsfile` define um pipeline com os seguintes estágios:

| Estágio | Descrição |
|---|---|
| **Checkout** | Clona o repositório |
| **Instalar Dependências** | Instala pacotes do `requirements.txt` |
| **Testes Unitários** | Executa todos os testes com `pytest` |
| **Build Executável** | Gera `.exe` com PyInstaller |
| **Gerar Instalador** | Compila o script Inno Setup |
| **Arquivar Artefatos** | Salva o instalador como artefato do Jenkins |

### Como configurar no Jenkins
1. Criar um novo item do tipo **Pipeline**
2. Em "Pipeline", selecionar **Pipeline script from SCM**
3. Configurar o repositório Git do projeto
4. O Jenkins irá detectar o `Jenkinsfile` automaticamente

---

## 📀 Instalador (Inno Setup)

### Gerar manualmente
1. Primeiro, gerar o executável:
   ```bash
   pyinstaller --onefile --windowed --name Calculadora calculadora.py
   ```
2. Abrir o `instalador.iss` no Inno Setup e compilar (Ctrl+F9)
3. O instalador será gerado em `Output/CalculadoraSetup.exe`

---

## 🧪 Testes

Testes unitários cobrem:
- ✅ Soma (positivos, negativos, zero, decimais)
- ✅ Subtração (positivos, resultado negativo, zero, decimais)
- ✅ Multiplicação (positivos, por zero, negativos, decimais)
- ✅ Divisão (exata, decimal, por um, por zero, negativos)
- ✅ Validação de segurança (tipos, mensagens de erro)

---

## 🛡️ Aspectos de Segurança

- **Validação de entrada**: Apenas caracteres matemáticos são permitidos no `eval()`
- **Tratamento de erros**: Divisão por zero é tratada com exceção descritiva
- **Testes automatizados**: Garantem que as operações funcionam corretamente
- **Pipeline CI/CD**: Automatiza verificação de qualidade a cada commit
- **Instalador assinável**: O Inno Setup permite assinar digitalmente o instalador
