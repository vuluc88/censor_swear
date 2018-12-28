from censor_app.dialog import models as dialog_models
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from censor_app.dialog import serializers as dialog_serializers


class RawDialogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows raw dialog to be viewed or edited.
    """
    queryset = dialog_models.RawDialog.objects.all()

    def get_serializer_class(self):
        if self.action == 'censoring':
            return dialog_serializers.CensorDialogSerializer
        else:
            return dialog_serializers.RawDialogSerializer

    @action(detail=False, methods=['post'])
    def censoring(self, request):
        serializer = dialog_serializers.CensorDialogSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.censor_dialog()
            return Response({'status': 'success', 'censored_dialogs': result})
        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CensoredDialogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows censored dialog to be viewed or edited.
    """
    queryset = dialog_models.CensoredDialog.objects.all()
    serializer_class = dialog_serializers.CensoredDialogSerializer
