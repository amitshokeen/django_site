from django.contrib import admin
from .models import Meetup, Location, Participant

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     # Filter participants based on the selected meetup
    #     if request.resolver_match.kwargs.get('object_id'):
    #         meetup = qs.get(pk=request.resolver_match.kwargs['object_id'])
    #         return meetup.participants.all()
    #     return qs
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # If an object is being edited
            form.base_fields['participants'].queryset = obj.participants.all()
        return form
    
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
