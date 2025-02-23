from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Crear el chatbot sin modelo de idioma
emotional_bot = ChatBot(
    'EmotionalAssistant',
    tagger_language=None
)

trainer = ChatterBotCorpusTrainer(emotional_bot)
trainer.train('chatterbot.corpus.spanish')
trainer.train( "C:/Users/lvila/OneDrive - Universidade da Coruña/HackUDC/chatbot/src/training_chatbot.yml")

# Interfaz de línea de comandos (CLI)
def conver(entrada):


    while True:
        user_message = entrada
        if user_message.lower() == 'chao':
            return '¡Hasta luego! Cuídate mucho. 💙'
        response = emotional_bot.get_response(user_message)

        return response