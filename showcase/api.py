"""from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

chatterbot = ChatBot('Example ChatterBot')
trainer = ListTrainer(chatterbot)

trainer.train([
    "Hi",
    "Hello",
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])


class ChatterBotView(views.APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        data = {
            'error': 'You should make a POST request to this endpoint.'
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        input_statement = request.data.get('text')
        response_statement = chatterbot.get_response(input_statement)
        response_data = {
            'text': response_statement.text,
            'confidence': response_statement.confidence,
            # include all attributes that you want to serialize
        }
        return Response(response_data, status=status.HTTP_200_OK)
"""