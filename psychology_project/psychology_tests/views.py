from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
import os
from . models import (
    Quiz,
)

class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = os.path.join('psychology_tests', 'quiz_list.html')
    
    def get_queryset(self):
        query = super().get_queryset()
        product_type_name = self.request.GET.get('product_type_name',None)
        if product_type_name:
            query = query.filter(
                product_type__name = product_type_name
            )
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_type_name'] = self.request.GET.get('product_type_name', '')
        return context
    
# class ProductDetailView(LoginRequiredMixin, DetailView):
#     model = Quiz
#     template_name = os.path.join('psychology_tests', 'quiz_detail.html')
    


# class QuizDetailView(LoginRequiredMixin, DetailView):
#     model = Quiz

#     def get_template_names(self):
#         """オブジェクトに設定されたテンプレート名を使用してテンプレートを選択"""
#         return [self.object.template_name] if self.object.template_name else ['default_quiz_template.html']
#         print("Using template:", template_name)  # デバッグ情報の出力
#         return [template_name]

class QuizDetailView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'admin/psychology_tests/default_quiz_template.html'

    def get_template_names(self):
        """
        オブジェクトに設定されたテンプレート名を使用してテンプレートを選択
        デフォルト以外のテンプレートが指定されている場合のみカスタムテンプレートを使用
        """
        if self.object.template_name != 'default_quiz_template.html':
            return [self.object.template_name]
        else:
            return ['default_quiz_template.html']
