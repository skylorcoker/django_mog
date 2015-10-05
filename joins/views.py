from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import EmailForm, JoinForm
from .models import Join
import uuid
from django.conf import settings

#uuid creates us a random id.. specifically uuid4() will give us a random id and set it to ref_id all lower case.
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		# need to handle if id_exist == true
		get_ref_id()
		# by doing this it will keep looping until it creates a ref_id that is unique!!
	except:
		return ref_id

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""

	return ip

# Create your views here.
def home(request):

	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
		print("the obj is %s" %(obj.email))
	except:
		obj = None
	# This is using Regular Djano Forms ##
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print(new_join, created)
	# 	if created:
	# 		print("This Object was Created")
	########################################################################
	# This is using Model Forms
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		# new_join.ip_address = get_ip(request)
		#we may do something before we commit (hence .save())
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			if not obj == None:
				new_join_old.friend = obj
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		# new_join.save()

		#print all friends that join as result of main sharer email

		# print(Join.objects.filter(friend=obj))
		# print(obj.referral.all())

		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))

	context = {"form": form}
	template = "home.html"
	return render(request, template, context)


# Create your views here.
def share(request, ref_id):
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		count = join_obj.referral.all().count()
		ref_url = settings.SHARE_URL + str(join_obj.ref_id)
		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request, template, context)
	except: 
		raise Http404