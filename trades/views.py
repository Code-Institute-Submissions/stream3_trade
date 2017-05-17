from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.template.context_processors import csrf
from models import Trades
from forms import tradeForForm
from accounts.views import profile
from models import Trades

# Create your views here.

@login_required(login_url='/login')
def postTradeMyProduct(request, id):
    if request.method=='POST':
        wanted = get_object_or_404(Product, id=int(id))
        offered = get_object_or_404(Product, id=(request.POST['offered']))
        sender = offered.owner
        receiver = wanted.owner

        offered.owner = receiver
        wanted.owner = sender

        wanted.save()
        offered.save()

        dele = get_object_or_404(Trades, receiver=request.user, wanted=id )
        dele.delete()

        return redirect(profile)
    else:
        trades = Trades.objects.filter(wanted=id)
        args = {"trades": trades}
        args.update(csrf(request))
        return render(request, "tradeofferconfirm.html", args)


@login_required(login_url='/login')
def traderequest(request, id):
    if request.method=='POST':
        trade = Trades()

        trade.sender = request.user

        trade.wanted = get_object_or_404(Product, id=int(id))
        trade.offered = get_object_or_404(Product, id=(request.POST['offered']))

        trade.receiver = trade.wanted.owner
        trade.save()
        return render(request, "tradeconfirm.html")
    else:
        products = Product.objects.filter(owner=request.user)
        args = {"products": products}
        args.update(csrf(request))
        return render(request, "trade.html", args)



