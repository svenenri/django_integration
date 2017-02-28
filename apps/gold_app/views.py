from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import GoldGame
import random

# Declare all global values
activity = []

# Project views
def index(request):
	return render(request, 'gold_app/index.html')

def process(request):
	if request.method == 'POST':
		# request.session["activity"] = []
		click = request.POST["building"]
		try:
			yourGold = request.session["yourGold"]
		except:
			request.session['yourGold'] = 0
			yourGold = request.session['yourGold']
		counter = 0
		ninjaGold = GoldGame(click)
		if click == "farm":
			random = ninjaGold.randomGold()
			yourGold += random
			act = ninjaGold.getActivity(random)
			activity.append(act)
		elif click == "cave":
			random = ninjaGold.randomGold()
			yourGold += random
			act = ninjaGold.getActivity(random)
			activity.append(act)
		elif click == "house":
			random = ninjaGold.randomGold()
			yourGold += random
			act = ninjaGold.getActivity(random)
			activity.append(act)
		elif click == "casino":
			random = ninjaGold.randomGold()
			yourGold += random
			act = ninjaGold.getActivity(random)
			activity.append(act)

		request.session["yourGold"] = yourGold
		request.session["activity"] = activity
		request.session["counter"] = counter
		counter += 1

	return redirect(reverse('ninja_gold:gold_index'))

def reset(request):
	request.session['yourGold'] = 0
	request.session['counter'] = 0
	for activities in range(len(activity)):
		activity.pop()
	try:
		del request.session['activity']
		return redirect(reverse('ninja_gold:gold_index'))
	except:
		return redirect(reverse('ninja_gold:gold_index'))
