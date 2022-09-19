from django import template
##템플릿 필터 작성하기

register = template.Library()

# 위처럼 sub 함수에 @register.filter 애너테이션을 적용하면
# 템플릿에서 해당 함수를 필터로 사용할 수 있게 된다.
# sub 함수는 기존 값 value에서
# 입력으로 받은 값 arg를 빼서 리턴하는 함수이다.
# sub 필터를 사용하기 위해서는
# 템플릿 상단에 다음처럼 {% load pybo_filter %} 로
# sub 필터를 저장한 파일(pybo_filter.py)을 먼저 로드해야 한다.
@register.filter
def sub(value, arg):
    return value - arg