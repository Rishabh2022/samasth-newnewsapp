# from django.http import HttpResponse
# from django.shortcuts import render
# class errormsgmiddleware(object):
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         return self.get_response(request)
#     def process_exception(self,request,exception):
#         return render(request,"testapp/error.html")

# class execution(object):
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         print("this line printed preprocessing of request")
#         response=self.get_response(request)
#         print("this line printed post processing of request")
#         return response
#     def process_exception(self,request,exception):
#         return render(request,"testapp/error.html") 