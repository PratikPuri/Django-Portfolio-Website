from rest_framework.response import Response
from rest_framework.decorators import api_view 
from base.models import Feedback
from .serializers import FeedbackSerializer

@api_view(['GET'])
def getData(request):
    Feedbacks = Feedback.objects.all()
    serializer = FeedbackSerializer(Feedbacks,many=True)
    return Response(serializer.data);   

@api_view(['POST'])
def addFeedback(request):
    serializer = FeedbackSerializer(data=request.data);
    print (serializer);
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data);