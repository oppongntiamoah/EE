from django.contrib import admin
from .models import Student, Question, Response


class ResponseInline(admin.TabularInline):
    """
    Inline table to show responses inside Student admin page
    """
    model = Response
    extra = 0
    readonly_fields = ("question", "selected_option", "time_taken")
    can_delete = False


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("participant_id", "gender")
    list_filter = ("gender",)
    search_fields = ("id",)
    ordering = ("id",)
    inlines = [ResponseInline]

    def participant_id(self, obj):
        # Show custom ID: M1, F2, etc.
        prefix = "M" if obj.gender == "m" else "F"
        return f"{prefix}{obj.id}"
    participant_id.short_description = "Participant ID"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "option_a", "option_b")
    search_fields = ("text", "option_a", "option_b")
    ordering = ("id",)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("participant_display", "question", "selected_option", "time_taken")
    list_filter = ("selected_option", "question__id", "participant__gender")
    search_fields = ("participant__id", "question__text")
    ordering = ("question", "participant")

    def participant_display(self, obj):
        prefix = "M" if obj.participant.gender == "m" else "F"
        return f"{prefix}{obj.participant.id}"
    participant_display.short_description = "Participant"
