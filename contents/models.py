from django.db import models

'''
class Photo(WSModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=30, verbose_name=_('File Name'),
                                 help_text=_('File name'), blank=True)
    file = models.ImageField(upload_to=photo_upload_to, validators=[
        FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))
    ])

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    uploaded_by = models.ForeignKey(get_user_model(), verbose_name=_('Uploaded By'),
                                    help_text=_('Uploaded By'), on_delete=models.PROTECT)

    class Meta:
        unique_together = (('file_name', 'content_type', 'object_id'),)
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __str__(self):
        return self.file_name

    def save(self, args, *kwargs):
        if not self.file_name:
            self.file_name, extension = os.path.splitext(self.file.name)
        super(Photo, self).save(*args, **kwargs)


def photo_upload_to(instance, file_name):
    original_file_name, file_extension = os.path.splitext(file_name)
    base_path_name = 'photos'
    app_label = instance.content_type.app_label
    model_name = instance.content_type.model
    time = datetime.datetime.now()

    new_file_name = instance.file_name + file_extension

    return os.path.join(
        f'{base_path_name}/{app_label}/{model_name}/{time.year}/{time.month}/{time.day}/', new_file_name)

'''