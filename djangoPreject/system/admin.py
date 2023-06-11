from django.contrib import admin
from .models import Book
from openpyxl import Workbook
import time
from django.http import HttpResponse

class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields][1:]
        field_verbose_names = [field.verbose_name for field in meta.fields][1:]
        response = HttpResponse(content_type='application/msexcel')
        filename = self.model._meta.verbose_name
        response['Content-Disposition'] = f'attachment; filename={filename.encode("utf-8").decode("ISO-8859-1")}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_verbose_names)
        for obj in queryset:
            data = []
            for field in field_names:
                if hasattr(obj, f'get_{field}_display'):
                    value = getattr(obj, f'get_{field}_display')()
                else:
                    value = getattr(obj, field)
                data.append(f'{value}')
            ws.append(data)
        wb.save(response)
        return response

    export_as_excel.short_description = '导出Excel'
    export_as_excel.type = 'success'

class ControlBook(admin.ModelAdmin, ExportExcelMixin):
    list_display = ['category', 'short_title', 'author' ,'createTime', 'press','now_price','pre_price','discount','short_detail','star','comment_num','addTime']
    ordering = ['category']
    list_filter = ['title']
    list_per_page = 20
    actions = ['export_as_excel']

admin.site.register(Book,ControlBook)
admin.site.site_header = '图书分析大屏展示系统'
admin.site.site_title = '图书分析大屏展示系统'
admin.site.index_title = '图书分析大屏展示系统'
