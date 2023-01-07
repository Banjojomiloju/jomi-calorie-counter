from django.shortcuts import render

#q0Fch+uoWbZn5SfghI+61Q==tL9H7xM9rR9dfiU5
# Create your views here.
def home(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST["query"]
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get  (api_url + query, headers = {'X-Api-Key': 'q0Fch+uoWbZn5SfghI+61Q==tL9H7xM9rR9dfiU5'})

        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api= 'oops there was an error'
            print(e)
        return render(request, "home.html",{"api":api})
    else:
        return render(request, "home.html",{"query":'enter a valid query'})

   
    
