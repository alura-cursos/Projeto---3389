from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.globals import set_debug
from langchain.memory import ConversationBufferMemory
import os
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()
set_debug(True)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY"))

mensagens = [
        "Quero visitar um lugar no Brasil famoso por suas praias e cultura. Pode me recomendar?",
        "Qual é o melhor período do ano para visitar em termos de clima?",
        "Quais tipos de atividades ao ar livre estão disponíveis?",
        "Alguma sugestão de acomodação eco-friendly por lá?",
        "Cite outras 20 cidades com características semelhantes as que descrevemos até agora. Rankeie por mais interessante, incluindo no meio ai a que você já sugeriu.",
        "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]

"""
Este código é uma alternativa à classe ConversationChain, que será depreciadas.  
Ele utiliza a estrutura de RunnableWithMessageHistory para armazenar mensagens. 
O código está comentado por padrão para evitar execução automática, mas pode ser descomentado conforme necessário.

Para testar, basta remover os comentários da seção correspondente. E comentar o codigo depreciado que começa na linha 80.
"""

''' # Remova este comentário para ativar o código

# Importação das classes necessárias para lidar com histórico de mensagens e execução de modelos de linguagem
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Dicionário para armazenar os históricos de conversa por sessão
armazenamento = {}

# Configuração utilizada para definir a sessão de mensagens
config = {"configurable": {"session_id": "id_aula_aleatorio"}}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """
    Função para recuperar ou criar um histórico de mensagens para uma determinada sessão.

    Parâmetros:
    - session_id (str): Identificador único da sessão.

    Retorno:
    - Instância de InMemoryChatMessageHistory associada à sessão.
    """
    if session_id not in armazenamento:
        # Se a sessão não existir, cria um novo histórico em memória
        armazenamento[session_id] = InMemoryChatMessageHistory()
    
    return armazenamento[session_id]

# Criando um objeto de conversa que mantém histórico
# Aqui, `llm` representa um modelo de linguagem previamente definido
conversa_com_historico = RunnableWithMessageHistory(llm, get_session_history, config=config)

# Iterando sobre a lista de mensagens para processar cada uma com o modelo de IA
for mensagem in mensagens:
    resposta = conversa_com_historico.invoke(mensagem)

# Exibindo o histórico de mensagens da sessão "id_aula_aleatorio"
print("Histórico: \n\n", armazenamento["id_aula_aleatorio"].messages)

''' # Remova esta linha de comentários para ativar o código

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm,
                                 verbose=True,
                                 memory=memory)

for mensagem in mensagens:
    resposta = conversation.predict(input=mensagem)
    print(resposta)

print(memory.load_memory_variables({}))
