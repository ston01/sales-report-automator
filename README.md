# 📊 Sistema Automator - Relatórios de Vendas

Este é um sistema de **automação em Python** que lê planilhas de vendas, trata os dados e gera relatórios em PDF de forma prática e organizada.  
O projeto foi estruturado seguindo boas práticas de desenvolvimento, com modularização, manipulação de dados via Pandas e geração de relatórios automatizados.

---

## 🚀 Nota de evolução
Este projeto marca um avanço importante na minha jornada como desenvolvedor, consolidando conhecimentos em:
- Automação de processos
- Manipulação de dados com Pandas
- Geração de relatórios profissionais em PDF
- Estruturação de projetos para portfólio

---

## 🛠️ Funcionalidades
- **Leitura de planilha**: importa dados da pasta `data/entrada`.
- **Tratamento de dados**: organiza e padroniza informações.
- **Análise automática**: calcula métricas como total de vendas e ticket médio.
- **Relatório em PDF**: gera documento estruturado pronto para uso.
- **Exportação de planilha tratada**: salva versão limpa dos dados.

---

## 💻 Tecnologias e Conceitos Aplicados
- **Python 3**: linguagem base do projeto.
- **Pandas**: manipulação e análise de dados.
- **FPDF**: geração de relatórios em PDF.
- **Boas práticas de modularização**: separação de responsabilidades por arquivos.
- **Automação de fluxo**: entrada → processamento → saída.

---

## 📂 Estrutura do Projeto

```text
sales-report-automator/
├── data/
│   ├── entrada/          # Planilhas originais
│   └── saida/            # Relatórios e planilhas tratadas
├── lib/
│   ├── executor.py       # Função principal do programa
│   ├── leitor.py         # Funções de leitura da entrada da planilha
│   ├── tratamento.py     # Funções de tratamento de planilha
│   ├── analise.py        # Funções de análise de dados
│   ├── relatorio.py      # Geração de PDF
│   └── init.py
├── main.py               # Ponto de entrada do programa
├── LICENSE               # Licença de uso
└── README.md             # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto
Você pode rodar esta aplicação diretamente pelo código-fonte ou baixando a versão compilada para o seu sistema operacional.

Opção 1: Executando o Código-Fonte (Para Desenvolvedores)
Certifique-se de ter o Python 3 instalado em sua máquina.
Execute o bash

Clone o repositório:
```bash
git clone [https://github.com/ston01/sales-report-automator.git](https://github.com/ston01/sales-report-automator.git)
```
Acesse o diretório do projeto:
```bash
cd sales-report-automator
python -m pip install openpyxl
```
Inicie o programa:
```bash
python main.py
```

Opção 2: Executando como Aplicativo Nativo (.exe)
Se você deseja apenas testar ou utilizar o software no Windows sem precisar instalar o Python:

1. Acesse a aba Releases deste repositório.

2. Baixe o pacote compactado (.zip) contendo o executável.

3. Extraia o conteúdo e certifique-se de que o arquivo dados.db está localizado na mesma pasta que o main.exe.

4. Dê um duplo clique em main.exe para rodar.

---

🧠 Aprendizados Relevantes
- Automação de relatórios: eliminei tarefas manuais repetitivas.

- Manipulação de dados: domínio prático de Pandas.

- Modularização: código organizado em arquivos com responsabilidades claras.

- Documentação: criação de README e estrutura de projeto profissional.

- Portfólio: projeto pronto para mostrar habilidades em freelances e oportunidades.

👤 Autor
Desenvolvido com dedicação por Emanuel  
GitHub: @ston01
