from django.shortcuts import render

def power(request):
    output = None  
    if request.method == 'POST':
      
            intensity = int(request.POST.get('intensity-input'))
            resistance = int(request.POST.get('resistance-input'))
            output = (intensity ** 2) * resistance
        
    return render(request, 'index.html', {'output': output})
