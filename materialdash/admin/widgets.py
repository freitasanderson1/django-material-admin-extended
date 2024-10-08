from django.contrib.admin import widgets
from django import forms


class MaterialDashAdminDateWidget(widgets.AdminDateWidget):
    """Date widget with material specific styling"""
    template_name = 'materialdash/admin/widgets/date.html'

    def __init__(self, attrs=None, format=None):
        attrs = {'class': 'datepicker', 'size': '10', **(attrs or {})}
        super().__init__(attrs=attrs, format=format)

    @property
    def media(self):
        return forms.Media(
            js=['materialdash/admin/js/widgets/TimeServerDiff.js', 'materialdash/admin/js/widgets/DateInput.js'],
            css={'all': ('materialdash/admin/css/date-input.min.css',)}
        )


class MaterialDashAdminSplitDateTime(forms.SplitDateTimeWidget):
    """A SplitDateTime Widget with material specific styling"""
    template_name = 'materialdash/admin/widgets/split_datetime.html'

    class Media:
        js = [
            'materialdash/admin/js/widgets/TimeServerDiff.js',
            'materialdash/admin/js/widgets/DateInput.js',
            'materialdash/admin/js/widgets/TimeInput.js'
        ]
        css = {'all': (
            'materialdash/admin/css/split_datetime.min.css',
        )}

    def __init__(self, attrs=None, date_format=None, time_format=None, date_attrs=None, time_attrs=None):
        date_attrs = date_attrs or {}
        date_attrs.update({'class': 'datepicker'})
        time_attrs = time_attrs or {}
        time_attrs.update({'class': 'timepicker'})
        super().__init__(attrs, date_format, time_format, date_attrs, time_attrs)


class MaterialDashAdminTimeWidget(forms.TimeInput):
    """Time input with material css styles"""
    template_name = 'materialdash/admin/widgets/time.html'

    @property
    def media(self):
        return forms.Media(
            js=['materialdash/admin/js/widgets/TimeServerDiff.js', 'materialdash/admin/js/widgets/TimeInput.js'],
            css={'all': ('materialdash/admin/css/time-input.min.css',)}
        )


class MaterialDashAdminTextareaWidget(widgets.AdminTextareaWidget):
    """Textarea with material css styles"""

    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'materialize-textarea', **(attrs or {})})
