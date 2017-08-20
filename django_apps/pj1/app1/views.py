from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.template import RequestContext
from app1.models import Shain


# Create your views here.

def shain(request):
    # データベース上のIPアドレス情報を配列型で取得
    shains = Shain.objects.all().order_by('shain_id')
    context = {'shains' : shains }

    return  render(
        request,
        'shain.html', # テンプレート名を指定
        context
        #{'shains' : shains }, # 取得したIPアドレス情報をテンプレート内の変数に代入
        #context_instance=RequestContext(request)
        )


