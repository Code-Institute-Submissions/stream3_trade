from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm, UserLoginForm, ProfileRegistrationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect,get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Profiledetails
from products.models import Product
from trades.models import Trades


@login_required(login_url='/login')
def profile(request):
    try:
        details = Profiledetails.objects.filter(user=request.user)
        return render(request, "profile.html", {"details": details})
    except Profiledetails.DoesNotExist:
        return redirect(create_profile)



@login_required(login_url='/login')
def create_profile(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
        return redirect(profile)
    else:
        form = ProfileRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'create_profile.html', args)


@login_required(login_url='/login')
def profileupdate(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm()
        if form.is_valid():
            form.save()
    else:
        form = ProfileRegistrationForm()
        args = {'profile_form': form}
        args.update(csrf(request))
        return render(request, 'profile_details.html', args)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username_or_email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and 'next' in request.GET:
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()

    args = {'form': form, 'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse(create_profile))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)

@login_required(login_url='/login')
def get_details(request):
    details = Profiledetails.objects.filter(user=request.user)
    return render(request, "profile.html", {"details": details})

@login_required(login_url='/login')
def postMyProduct(request):
    products = Product.objects.filter(owner=request.user)
    args = {}
    args.update(csrf(request))
    return render(request, "profileitems.html", {"products": products}, args)

def postMyProductDetail(request, id):
    myprod = get_object_or_404(Product, pk=id)
    myprod.save()
    return render(request, "profileitem_details.html", {'myprod': myprod})

@login_required(login_url='/login')
def alltradeoffers(request):
    trades=Trades.objects.filter(receiver=request.user)
    return render(request, 'tradeoffers.html',{"trades":trades})

@login_required(login_url='/login')
def refusetrade(request, id):
    deletrade = get_object_or_404(Trades, pk=id)
    deletrade.delete()
    return redirect(get_details)