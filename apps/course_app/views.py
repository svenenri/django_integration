from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Course
from ..login_reg_app.models import User

# Views for Courses project.
def index(request):
	# try:
	userSelect = User.userManager.getAllUsers()
	courseSelect = Course.courseManager.getAllCourses()
	userCount = Course.courseManager.countUsers()
	print userCount
	context = {
		'allUsers': userSelect,
		'allCourses': courseSelect,
		'userCount': userCount,
	}
 	return render(request, 'course_app/users_courses.html', context)
	# except:
	# 	return render(request, 'course_app/users_courses.html')

def add(request):
	getCourses = Course.courseManager.getAllCourses()
	context = {
		'allCourses': getCourses,
	}
	return render(request, 'course_app/index.html', context)
def process(request):
	if request.method == 'POST':
		if request.POST['add']:
			course = request.POST['name']
			description = request.POST['description']
			checkCourse = Course.courseManager.getCourseByName(course)
			if checkCourse:
				messages.error(request, 'This course already exists.')
				return redirect(reverse('courses:courses_add'))
			else:
				addCourse = Course.courseManager.addCourse(course, description)
				messages.success(request, addCourse[1])
				return redirect(reverse('courses:courses_add'))
	return redirect(reverse('courses:courses_index'))
def addUser(request):
	# Get selected user and course
	user = request.POST['user']
	course = request.POST['course']
	# Add user to course
	# addUserCourse = Course.courseManager.addUserCourse(user, course)
	# if addUserCourse[0] == True:
	# 	messages.success(request, addUserCourse[1])
	# 	return redirect(reverse('courses:courses_index'))
	# else:
	# 	messages.error(request, 'An error occured.')
	# 	return redirect(reverse('courses:courses_index'))
	messages.error(request, '\"Add User to Course\" functionality will be added in the future.')
	return redirect(reverse('courses:courses_index'))
def destroy(request, id):
	userID = id
	courseSelect = Course.courseManager.getACourse(userID)
	courses = {
		'allCourses': courseSelect,
	}
	return render(request, 'course_app/destroy.html', courses)

def delete(request, id):
	if request.method == 'POST':
		if 'yes' in request.POST:
			userID = id
			courseDelete = Course.courseManager.delete(userID)
			if courseDelete[0] == True:
				messages.success(request, courseDelete[1])
				return redirect(reverse('courses:courses_add'))
			else:
				messages.error(request, courseDelete[1])
				return redirect(reverse('courses:courses_add'))
		elif 'no' in request.POST:
			return redirect(reverse('courses:courses_add'))
