from django.core.exceptions import ValidationError
from django.db.models import FileField
from django.utils.translation import gettext_lazy as _


class FileFiledRestricted(FileField):
    """Set max size upload file on FileField"""

    def __init__(self, *args, **kwargs):
        print("size")
        self.max_upload_size = 2621440
        super(FileFiledRestricted, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(FileFiledRestricted, self).clean(*args, **kwargs)

        file = data.file
        try:
            if file._size > self.max_upload_size:
                raise ValidationError(
                    _("Please keep filesize under %s."), code="invalid size", params={"size": file._size}
                )
        except AttributeError:
            pass

        return data
