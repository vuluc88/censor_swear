from django.db import models

class RawDialog(models.Model):

    id = models.AutoField(primary_key=True)
    content_text = models.CharField(blank=False, null=False, max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'raw_dialogs'

class CensoredDialog(models.Model):

    id = models.AutoField(primary_key=True)
    raw_dialog = models.ForeignKey(RawDialog, db_column='raw_dialog_id', on_delete=models.CASCADE, null=False, related_name='censored_dialogs')
    content_text = models.CharField(blank=False, null=False, max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'censored_dialogs'
