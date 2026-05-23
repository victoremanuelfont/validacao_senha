
```markdown
# Atividade Prática - API de Senhas com Docker & GitHub Actions

Este repositório contém a entrega da atividade prática de criação de uma aplicação Web para validação e geração de senhas seguras, estruturada em ambiente multicontainer e integrada a um pipeline de Integração Contínua (CI).

## 📋 Requisitos da Atividade Atendidos

- [x] **Aplicação Web:** Desenvolvida em Python utilizando o framework Flask.
- [x] **Mecanismo de Validação:** Verifica se a senha cumpre os requisitos de segurança (mínimo de 12 caracteres, maiúsculas, minúsculas, números e caracteres especiais).
- [x] **Gerador Automático:** Cria senhas que atendem obrigatoriamente a todos os critérios de força exigidos.
- [x] **Ambiente Dockerizado:** Configuração de dois containers independentes e isolados via Docker Compose:
  - `app`: Container responsável por executar a API Flask.
  - `tests`: Container responsável por rodar a suite de testes automatizados (`pytest`).
- [x] **Pipeline CI/CD:** Automação via GitHub Actions para execução dos testes a cada commit.

---

## 📁 Estrutura de Pastas

```text
PASSWORD-VAULT/
├── .github/workflows/
│   └── ci.yml             # Pipeline do GitHub Actions
├── app/
│   ├── app.py                 # Código da API Flask
│   └── requirements.txt       # Dependências do backend
├── tests/
│   ├── test_app.py            # Testes automatizados (Pytest)
│   └── requirements.txt       # Dependências dos testes
└── docker-compose.yml         # Orquestração dos 2 containers

```

---

## 🛠️ Como Executar e Testar o Projeto

Para rodar a aplicação e disparar a suite de testes exatamente como ocorre no servidor do GitHub Actions, execute o comando abaixo no terminal da raiz do seu projeto:

```bash
docker-compose up --build --exit-code-from tests

```

### O que acontece ao rodar este comando?

1. O Docker cria a rede isolada e baixa as imagens do Python.
2. O container `app` inicia o servidor Flask na porta `5000`.
3. O container `tests` aguarda a API Flask ficar online e dispara os testes automatizados do `pytest`.
4. Os testes verificam se o gerador entrega senhas seguras e se a validação barra senhas fracas.
5. Assim que os testes finalizam, **todos os containers são derrubados automaticamente**, replicando o comportamento de uma esteira de produção.

```

```
