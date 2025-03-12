<img width="989" alt="image" src="https://github.com/user-attachments/assets/8d596811-2a2e-4b42-bb4c-94a218d6af98" />

# LangChain e Python: criando ferramentas com a LLM OpenAI

## ⚙️ Guia de Configuração

Siga os passos abaixo para configurar seu ambiente e utilizar os scripts do projeto.

### 1. Criar e Ativar Ambiente Virtual

**Windows:**
```bash
python -m venv langchain
langchain\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv langchain
source langchain/bin/activate
```

### 2. Instalar Dependências

Utilize o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Configurar Chave da OpenAI

Crie ou edite o arquivo `.env` adicionando sua chave de API da OpenAI:
```bash
OPENAI_API_KEY="SUA_CHAVE_DE_API"
```

### Observação Importante

Os scripts `main.py` e `openai_simples.py` atualmente não estão configurados para ler automaticamente as variáveis do arquivo `.env`. Você precisará ajustar manualmente esses scripts caso deseje utilizar variáveis de ambiente.
