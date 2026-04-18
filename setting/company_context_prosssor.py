from .models import company



def company_context_processor(request):
    data = company.objects.last()
    return {'company_data':data}