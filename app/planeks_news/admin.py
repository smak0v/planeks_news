from django.contrib.admin import AdminSite


class PlaneksNewsAdminSite(AdminSite):
    site_header = 'PLANEKS News Administration'


admin_site = PlaneksNewsAdminSite(name='planeks_news_admin')
