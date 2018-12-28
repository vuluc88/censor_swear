from censor_app.dialog import models as dialog_models
from rest_framework import serializers


class RawDialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = dialog_models.RawDialog
        fields = '__all__'


class CensoredDialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = dialog_models.CensoredDialog
        fields = '__all__'


class CensorDialogSerializer(serializers.Serializer):
    list_id = serializers.ListField(child=serializers.IntegerField(), required=True)

    def censor_dialog(self):
        list_id = self.validated_data.get('list_id')
        print(list_id)

        raw_dialogs = dialog_models.RawDialog.objects.filter(pk__in=list_id)
        censored_dialogs = []
        for d in raw_dialogs:
            censored_dialog = d.censored_dialogs.filter().first()
            if censored_dialog:
                censored_dialog.content_text = "****"
            else:
                censored_dialog = dialog_models.CensoredDialog(raw_dialog=d, content_text="*")
            censored_dialog.save()
            censored_dialogs.append(censored_dialog)

        serializer = CensoredDialogSerializer(censored_dialogs, many=True)
        return serializer.data
