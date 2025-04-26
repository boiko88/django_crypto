from django.contrib import admin
from .models import Profile, Mentor


admin.site.register(Profile)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'expertise', 'is_active', 'approved', 'blog_count', 'created_at')
    list_filter = ('is_active', 'approved', 'created_at')
    search_fields = ('profile__user__username', 'expertise', 'bio')
    readonly_fields = ('blog_count', 'created_at')
    actions = ['approve_mentors', 'deactivate_mentors']
    fieldsets = (
        ('Basic Information', {
            'fields': ('profile', 'expertise', 'bio')
        }),
        ('Status', {
            'fields': ('is_active', 'approved', 'blog_count', 'created_at')
        }),
    )

    def get_username(self, obj):
        return obj.profile.user.username
    get_username.short_description = 'Username'
    get_username.admin_order_field = 'profile__user__username'

    def approve_mentors(self, request, queryset):
        queryset.update(approved=True)
    approve_mentors.short_description = "Approve selected mentors"

    def deactivate_mentors(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_mentors.short_description = "Deactivate selected mentors"
