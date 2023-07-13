from django.shortcuts import render, redirect
from django.views import View
import requests, json
from django.http import HttpResponse
import zebedee
import environ

# Get Environmental Variables
env = environ.Env()

# Create a ZEBEDEE Project object
hackathon = zebedee.Project(env('ZEBEDEE_API_KEY'))

# You may now use the hackathon object to make API calls!


def index(request):
  # Example API Call
  # Getting balance
  wallet = hackathon.get_wallet_details()
  # Convert to Sats
  balance = hackathon.convert_msats_to_sats(wallet["balance"])
  # Creating the context for the template
  ctx = {"balance": balance}
  # Passing the context to the template in ./zbd/index.html and rendering the template.
  return render(request, "zbd/index.html", ctx)


def buy(request):
  invoice = hackathon.create_charge(amount_of_seconds_to_expire_after=600,
                                    amount_msats=100000,
                                    description="Lightning Rules")
  # Creating the context for the template
  ctx = {"ln_invoice": invoice}
  # Passing the context to the template in ./zbd/index.html and rendering the template.
  return render(request, "zbd/buy.html", ctx)


def charge_status(request, id):
  charge = hackathon.get_charge_details(id)
  status = charge["status"]
  if status != "completed":
    return HttpResponse(status)
  else:
    resp = HttpResponse("True")
    resp.headers["HX-Redirect"] = '/blog/'
    return resp


def blog(request):
  return render(request, "zbd/blog.html")
