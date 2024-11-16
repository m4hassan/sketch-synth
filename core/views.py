from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .firebase import *
from .modelslabAPI import *
from .models import Creations

def home(request):
    return render(request, 'core/home.html', {})


def register_user(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                messages.success(request, ("Holy Guacomole! You have been successfully registered and logged in!"))
                return redirect('home')
            
            else:
                messages.error(request, ("There was an error. Kindly try logging in again"))
                pass
        
        else:
            messages.error(request, ("Whoops! There was an error registering, please try again!"))
            return redirect('register')
    else:
        form = SignUpForm()
        return render(request, 'core/register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            messages.success(request, ("You have been logged in!"))
            return redirect('controlnet_view')
        else:
            messages.error(request, ("Incorrect login! Please try again!"))
            return redirect('login')
    else:
        return render(request, 'core/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home')

@login_required(login_url='/login/')
def controlnet_view(request):
    
    if request.method == 'POST':
        form = Controlnet_Form(request.POST, request.FILES)
        if form.is_valid():
            creation_instance = form.save(commit=False)
            creation_instance.user = request.user
            init_img = request.FILES['init_img']
            p_prompt = request.POST['p_prompt']
            n_prompt = request.POST['n_prompt']

            img_public_url = firebase_storage(init_img)
            try:
                output_url, json_response = controlnet_api(img_public_url, n_prompt, p_prompt)
                error_msg = json_response.get('message', '')
                
                if error_msg:
                    print("Response Error: ", error_msg)
                    return JsonResponse({"Error: ": error_msg})
                
                creation_instance.generated_img = output_url
                creation_instance.save()
                return JsonResponse({'output_url':output_url})
            
            except Exception as e:
                print("<== cmd exception ==>", e)
                return JsonResponse({'CMD Error:': str(e)}) 
            
    else:
        form = Controlnet_Form()
        return render(request, 'core/controlnet_view.html', {'form': form})

@login_required(login_url='/login/')
def creations_gallery(request):
    creations = Creations.objects.filter(user=request.user).order_by('-created_at')
    modified_creations = []
    for creation in creations:
        modified_img_url = creation.generated_img.replace('[', '').replace(']', '').replace("'", '')

        modified_creations.append({
            'id': creation.id,
            'init_img': creation.p_prompt,
            'p_prompt': creation.n_prompt,
            'generated_img': modified_img_url,
            'created_at': creation.created_at,
        })
        
    return render(request, 'core/creations_gallery.html', {'creations':modified_creations})

@login_required(login_url="/login/")
def user_profile(request):
    user = User.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, 'core/user_profile.html', context)


@login_required(login_url="/login/")
def delete_creation(request, pk):
    instance = Creations.objects.get(id=pk)
    instance.delete()
    return redirect('gallery')