# 🎰 Statistical Slot Machine

**Português | English**

---

# 🇧🇷 Português

## Sobre o projeto

O **Statistical Slot Machine** é um projeto acadêmico desenvolvido para a disciplina de **Probabilidade e Estatística**, do curso de Sistemas de Informação do Instituto Federal do Espírito Santo (IFES).

O projeto consiste em um simulador de máquina caça-níqueis (*slot machine*), desenvolvido para explorar conceitos de probabilidade, aleatoriedade e estatística por meio de simulações computacionais.

A aplicação utiliza exclusivamente créditos fictícios e possui finalidade educacional.

**Desenvolvedor:** João Victor Nascimento

## Objetivo

O objetivo principal é desenvolver um sistema de simulação probabilística que permita compreender o comportamento de eventos aleatórios ao longo de múltiplas rodadas.

O projeto busca:

- Simular uma máquina caça-níqueis com três rolos.
- Comparar probabilidades teóricas e experimentais.
- Analisar ganhos, perdas e retorno esperado.
- Investigar o comportamento de eventos independentes.
- Demonstrar conceitos estatísticos por meio de experimentos e visualizações.

## Tecnologias

- **Python:** implementação dos algoritmos e simulações.
- **FastAPI:** desenvolvimento da API.
- **React + TypeScript:** interface interativa.
- **Vite:** ambiente de desenvolvimento do frontend.
- **Jupyter Notebook:** execução e análise dos experimentos.
- **Pandas, NumPy, Matplotlib e SciPy:** processamento de dados, cálculos e visualizações estatísticas.

## Estrutura do projeto

```text
statistical-slot-machine/
│
├── backend/
│   ├── app/
│   │   ├── core/          # Lógica da máquina
│   │   ├── experiments/   # Experimentos estatísticos
│   │   └── api/           # Rotas da API
│   │
│   ├── tests/             # Testes automatizados
│   ├── main.py            # Aplicação FastAPI
│   ├── requirements.txt   # Dependências Python
│   └── README.md          # Documentação do backend
│
├── frontend/              # Aplicação React + TypeScript
├── notebooks/             # Notebooks Jupyter
├── resultados/            # Dados e gráficos gerados
├── relatorio/             # Relatório acadêmico
└── README.md
```

A estrutura separa a lógica da máquina, os experimentos estatísticos e a comunicação com o frontend, permitindo reutilizar os algoritmos Python em diferentes partes da aplicação.

## Como executar

As instruções abaixo consideram um ambiente Linux ou WSL.

### Backend

Na raiz do projeto, crie e ative o ambiente virtual:

```bash
python3 -m venv backend/venv
source backend/venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r backend/requirements.txt
```

Inicie o servidor:

```bash
cd backend
fastapi dev main.py
```

A API estará disponível em:

- API: `http://localhost:8000`
- Documentação: `http://localhost:8000/docs`

### Frontend

Após a inicialização do projeto React:

```bash
cd frontend
npm install
npm run dev
```

Por padrão, o frontend estará disponível em `http://localhost:5173`.

## Experimentos estatísticos

O projeto contempla cinco experimentos:

| Experimento | Descrição |
|---|---|
| **1. Frequências e RTP** | Comparação entre frequências teóricas e observadas em 10.000 rodadas. |
| **2. Convergência das médias** | Análise do comportamento da média amostral conforme aumenta o número de rodadas. |
| **3. Simulação de jogadores** | Estudo da evolução do saldo de jogadores virtuais. |
| **4. Independência** | Análise de resultados consecutivos e probabilidades condicionais. |
| **5. Alteração dos pagamentos** | Investigação dos efeitos de um aumento de 10% nos pagamentos. |

Os experimentos serão desenvolvidos em Python e analisados por meio de notebooks Jupyter.

## Reprodutibilidade

As simulações utilizarão geradores de números pseudoaleatórios com sementes (*seeds*) predefinidas.

Isso permitirá reproduzir os resultados dos experimentos sob as mesmas condições de execução.

Cada experimento terá seus parâmetros, sementes e resultados documentados.

## Conceitos estatísticos

Os principais conceitos abordados são:

- Espaço amostral e distribuições de probabilidade.
- Probabilidade teórica e experimental.
- Esperança matemática.
- Variância e desvio-padrão.
- Retorno ao jogador (*Return to Player — RTP*).
- Lei dos Grandes Números.
- Probabilidade condicional.
- Independência de eventos.
- Simulação de Monte Carlo.
- Reprodutibilidade estatística.

---

# 🇺🇸 English

## About the Project

**Statistical Slot Machine** is an academic project developed for the **Probability and Statistics** course in the Information Systems undergraduate program at the Federal Institute of Espírito Santo (IFES), Brazil.

The project consists of a slot machine simulator designed to explore probability, randomness, and statistical concepts through computational simulations.

The application uses fictitious credits exclusively and is intended for educational purposes.

**Developer:** João Victor Nascimento

## Objective

The main objective is to develop a probabilistic simulation system that helps users understand how random events behave over repeated trials.

The project aims to:

- Simulate a three-reel slot machine.
- Compare theoretical and experimental probabilities.
- Analyze gains, losses, and expected returns.
- Investigate the behavior of independent events.
- Demonstrate statistical concepts through experiments and visualizations.

## Technologies

- **Python:** algorithms and simulations.
- **FastAPI:** backend API development.
- **React + TypeScript:** interactive user interface.
- **Vite:** frontend development environment.
- **Jupyter Notebook:** statistical experiments and analysis.
- **Pandas, NumPy, Matplotlib, and SciPy:** data processing, numerical calculations, and statistical visualization.

## Project Structure

```text
statistical-slot-machine/
│
├── backend/
│   ├── app/
│   │   ├── core/          # Slot machine logic
│   │   ├── experiments/   # Statistical experiments
│   │   └── api/           # API endpoints
│   │
│   ├── tests/             # Automated tests
│   ├── main.py            # FastAPI application
│   ├── requirements.txt   # Python dependencies
│   └── README.md          # Backend documentation
│
├── frontend/              # React + TypeScript application
├── notebooks/             # Jupyter notebooks
├── resultados/            # Generated data and charts
├── relatorio/             # Academic report
└── README.md
```

The architecture separates the slot machine logic, statistical experiments, and frontend communication, allowing Python algorithms to be reused across different components.

## Getting Started

The following instructions are intended for Linux or WSL environments.

### Backend

From the project root, create and activate the virtual environment:

```bash
python3 -m venv backend/venv
source backend/venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r backend/requirements.txt
```

Start the server:

```bash
cd backend
fastapi dev main.py
```

The API will be available at:

- API: `http://localhost:8000`
- Documentation: `http://localhost:8000/docs`

### Frontend

Once the React application has been initialized:

```bash
cd frontend
npm install
npm run dev
```

By default, the frontend will be available at `http://localhost:5173`.

## Statistical Experiments

The project includes five statistical experiments:

| Experiment | Description |
|---|---|
| **1. Frequencies and RTP** | Comparison between theoretical and observed frequencies over 10,000 spins. |
| **2. Mean Convergence** | Analysis of sample mean behavior as the number of spins increases. |
| **3. Player Simulation** | Investigation of virtual players' balance evolution. |
| **4. Independence** | Analysis of consecutive outcomes and conditional probabilities. |
| **5. Payout Adjustment** | Investigation of the effects of increasing payouts by 10%. |

The experiments will be implemented in Python and analyzed using Jupyter Notebook.

## Reproducibility

The simulations will use pseudorandom number generators with predefined seeds.

This will allow experimental results to be reproduced under the same execution conditions.

Each experiment will document its parameters, seeds, and results.

## Statistical Concepts

The main concepts explored in this project include:

- Sample spaces and probability distributions.
- Theoretical and experimental probability.
- Expected value.
- Variance and standard deviation.
- Return to Player (RTP).
- Law of Large Numbers.
- Conditional probability.
- Independence of events.
- Monte Carlo simulation.
- Statistical reproducibility.

---
