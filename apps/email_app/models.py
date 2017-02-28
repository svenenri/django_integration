from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class EmailValidate(models.Manager):
	# CRUD Operations as functions

	# Get Emails from the Db
	def getAllEmails(self):
		allEmails = self.all()
		return allEmails

	# Validate Emails
	def validate(self, email):
		emailValidate = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(email) < 1 or not emailValidate.match(email):
			isValid = (False, 'Email is not valid!')
			return isValid
		else:
			# Add email to Db
			self.create(email = email)
			isValid = (True, 'Email is valid!')
			return isValid

	# Delete an email from the Db
	# Since user is never manually passing in the ID, no checks will be used to validate the ID.
	def delete(self, id):
		try:
			self.filter(id = id).delete()
			confirm = (True, 'Email has been successfully deleted.')
			return confirm
		except:
			confirm = (False, 'Email not found.')
			return confirm

class Email(models.Model):
	email = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	emailValidate = EmailValidate()

	def __str__(self):
		return self.email
