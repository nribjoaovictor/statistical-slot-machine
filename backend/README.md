# Backend — Statistical Slot Machine

O backend do projeto **Statistical Slot Machine** é desenvolvido em **Python**, utilizando o framework **FastAPI** para disponibilizar as funcionalidades da aplicação por meio de uma API REST.

O sistema é responsável pela implementação da lógica probabilística da máquina, execução dos experimentos estatísticos e comunicação com o frontend desenvolvido em React e TypeScript.

A arquitetura foi organizada para separar as responsabilidades de cada módulo, facilitando a manutenção, os testes e a reutilização do código.

## 1. Estrutura de diretórios

```text
backend/
│
├── venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── slot_machine.py
│   │
│   ├── experiments/
│   │   └── __init__.py
│   │
│   └── api/
│       ├── __init__.py
│       └── routes.py
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

## 2. Organização do backend

### `venv/` — Ambiente virtual

Diretório que contém o ambiente virtual Python utilizado pelo projeto.

Sua finalidade é isolar as dependências do backend, evitando conflitos com bibliotecas instaladas em outros projetos.

O ambiente virtual não deve ser versionado no Git, pois pode ser recriado utilizando o arquivo `requirements.txt`.

### `app/` — Aplicação principal

Pacote responsável por organizar os módulos que compõem o backend.

Está dividido em três partes principais: `core`, `experiments` e `api`.

#### `app/core/` — Lógica da máquina

Contém a implementação das regras matemáticas e probabilísticas da máquina estatística.

Suas principais responsabilidades são:

- Representar os três rolos e os cinco símbolos disponíveis.
- Realizar os sorteios pseudoaleatórios.
- Construir as combinações exibidas nos rolos.
- Identificar combinações premiadas na linha central.
- Calcular os pagamentos e o lucro líquido de cada rodada.
- Disponibilizar funções reutilizáveis para os experimentos e a API.

**Arquivo principal: `slot_machine.py`**

Será responsável pela implementação do algoritmo da máquina.

A lógica desse módulo será independente do FastAPI, permitindo sua utilização tanto pela API quanto pelos notebooks Jupyter.

#### `app/experiments/` — Experimentos estatísticos

Contém os módulos responsáveis pela execução dos cinco experimentos estatísticos definidos no projeto.

| Experimento | Objetivo |
|---|---|
| **1 — Frequências e RTP** | Executar 10.000 rodadas e comparar os resultados observados com os valores teóricos. |
| **2 — Convergência das médias** | Investigar o comportamento da média amostral conforme aumenta a quantidade de rodadas. |
| **3 — Simulação de jogadores** | Analisar a evolução do saldo de jogadores com capital inicial e limite de rodadas. |
| **4 — Independência** | Investigar a relação entre os resultados de rodadas consecutivas. |
| **5 — Alteração dos pagamentos** | Avaliar como mudanças na tabela de pagamentos afetam o RTP e o lucro esperado. |

Os experimentos utilizarão as funções implementadas em `core/`, evitando duplicação de código e garantindo consistência entre as simulações.

#### `app/api/` — Rotas da API

Contém os módulos responsáveis pela comunicação entre o backend e o frontend.

**Arquivo principal: `routes.py`**

Será utilizado para definir os endpoints HTTP por meio do `APIRouter` do FastAPI.

As rotas terão como responsabilidades:

- Receber requisições do frontend.
- Validar os parâmetros recebidos.
- Acionar as funções da máquina e dos experimentos.
- Retornar os resultados em formato JSON.

A lógica matemática será mantida separada das rotas HTTP.

### `tests/` — Testes automatizados

Diretório destinado aos testes do backend.

Os testes serão utilizados para verificar o funcionamento dos algoritmos e identificar possíveis inconsistências.

Entre as verificações previstas estão:

- Validação das posições sorteadas.
- Conferência das combinações premiadas.
- Verificação dos valores de pagamento.
- Cálculo correto do lucro líquido.
- Reprodutibilidade dos sorteios com sementes fixas.
- Validação das probabilidades e dos resultados teóricos.

A biblioteca **pytest** será utilizada para a execução dos testes automatizados.

## 3. Arquivos principais

### `main.py` — Inicialização da API

Arquivo responsável por criar e configurar a aplicação FastAPI.

Suas principais funções são:

- Inicializar a aplicação.
- Registrar as rotas da API.
- Configurar o CORS para comunicação com o frontend.
- Centralizar as configurações gerais do servidor.

O arquivo não será responsável pela implementação dos algoritmos estatísticos.

### `requirements.txt` — Dependências Python

Arquivo que registra as bibliotecas Python utilizadas pelo backend.

Permite reproduzir o ambiente de desenvolvimento em outros computadores.

Para instalar as dependências:

```bash
python -m pip install -r requirements.txt
```

### `__init__.py` — Inicialização de pacotes

Arquivo especial do Python utilizado para identificar diretórios como pacotes tradicionais.

Facilita a organização e a importação dos módulos da aplicação.

Inicialmente, os arquivos `__init__.py` permanecerão vazios.

## 4. Configuração do ambiente

Os comandos abaixo consideram um ambiente Linux ou WSL.

### 4.1. Criar o ambiente virtual

A partir da pasta `backend/`:

```bash
python3 -m venv venv
```

### 4.2. Ativar o ambiente virtual

```bash
source venv/bin/activate
```

### 4.3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4.4. Executar o servidor

```bash
fastapi dev main.py
```

Por padrão, a API estará disponível em:

- **API:** `http://localhost:8000`
- **Documentação interativa:** `http://localhost:8000/docs`
- **Especificação OpenAPI:** `http://localhost:8000/openapi.json`

## 5. Integração com o frontend

O frontend será desenvolvido utilizando **React, TypeScript e Vite**.

A comunicação ocorrerá por meio de requisições HTTP utilizando a API nativa `fetch()` do JavaScript.

O backend receberá as requisições, executará as operações necessárias e retornará respostas JSON.

Fluxo simplificado:

```text
React + TypeScript
        |
        | Requisição HTTP
        v
      FastAPI
        |
        v
   Rotas da API
        |
        v
  Lógica da máquina
        |
        v
 Resultados estatísticos
        |
        | Resposta JSON
        v
React apresenta os resultados
```

## 6. Integração com Jupyter Notebook

Os notebooks serão utilizados para executar e analisar os experimentos estatísticos.

A implementação principal da máquina permanecerá em `app/core/`, permitindo que os notebooks importem e reutilizem as mesmas funções utilizadas pelo FastAPI.

Essa abordagem evita a criação de algoritmos diferentes para a interface e para as análises estatísticas.

Os notebooks serão armazenados no diretório `notebooks/`, localizado na raiz do repositório.

## 7. Princípios de organização

O backend seguirá os seguintes princípios:

**Separação de responsabilidades:** cada módulo terá uma função específica dentro da aplicação.

**Reutilização de código:** a lógica da máquina será compartilhada entre a API, os experimentos e os notebooks.

**Reprodutibilidade:** as simulações utilizarão sementes pseudoaleatórias definidas, permitindo reproduzir os resultados dos experimentos.

**Testabilidade:** os algoritmos poderão ser testados independentemente do servidor FastAPI.

**Manutenibilidade:** a organização modular permitirá adicionar funcionalidades sem concentrar todo o código em um único arquivo.

---

## 8. Estado do desenvolvimento

O backend está em fase inicial de desenvolvimento.

A estrutura de diretórios foi definida, e a implementação das funcionalidades será realizada progressivamente.

As próximas etapas incluem:

1. Configuração e organização das rotas com `APIRouter`.
2. Implementação da lógica probabilística da máquina.
3. Desenvolvimento dos cinco experimentos estatísticos.
4. Criação dos testes automatizados.
5. Integração com o frontend React.
6. Validação dos resultados e documentação final.