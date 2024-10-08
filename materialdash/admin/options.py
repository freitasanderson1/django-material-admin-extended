from django.conf import settings
from django.db import models
from django.forms import SplitDateTimeField, forms

from materialdash.admin import widgets

FORMFIELD_FOR_DBFIELD_MATERIALDASH = {
    models.DateField: {'widget': widgets.MaterialDashAdminDateWidget},
    models.DateTimeField: {
        'form_class': SplitDateTimeField,
        'widget': widgets.MaterialDashAdminSplitDateTime
    },
    models.TimeField: {'widget': widgets.MaterialDashAdminTimeWidget},
    models.TextField: {'widget': widgets.MaterialDashAdminTextareaWidget},
}


class MaterialDashModelAdminMixin:
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.formfield_overrides.update(FORMFIELD_FOR_DBFIELD_MATERIALDASH)

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        js = [
            'vendor/jquery/jquery%s.js' % extra,
            'jquery.init.js',
            'core.js',
            'actions%s.js' % extra,
            'urlify.js',
            'prepopulate%s.js' % extra,
            'vendor/xregexp/xregexp%s.js' % extra,
        ]
        material_js = [
            'materialdash/admin/js/RelatedObjectLookups.min.js',
        ]
        return super().media + forms.Media(js=['admin/js/%s' % url for url in js] + material_js)
