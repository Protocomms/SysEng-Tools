from django.db import models
from django.forms import ModelForm
from django.urls import reverse



# Create your models here.
class Requirement(models.Model):
	description = models.TextField()
	parent = models.ForeignKey('Requirement', on_delete=models.SET_NULL, null=True, blank=True)
	is_constraint = models.BooleanField(default=False)
	min_measure_of_effectiveness = models.TextField(blank=True, default=None)
	target_measure_of_effectiveness = models.TextField(blank=True, default=None)
	rationale = models.TextField(blank=True, default=None)
	remarks = models.TextField(blank=True, default=None)

	TEST = 'TE'
	DEMONSTRATE = 'DE'
	ANALYSIS = 'AN'

	ACCEPTANCE_CRITERIA_CHOICES = [
		(TEST, 'Test'),
		(DEMONSTRATE, 'Demonstrate'),
		(ANALYSIS, 'Analysis'),
	]

	acceptance_criteria_type = models.CharField(
		max_length=2,
		choices=ACCEPTANCE_CRITERIA_CHOICES,
		default=None,
		blank=True
	)

	MANDATORY = 'MA'
	KEY = 'KE'
	HIGH = 'HI'
	MEDIUM = 'ME'
	LOW = 'LO'

	PRIORITY_CHOICES = [
	    (MANDATORY, 'Mandatory'),
		(KEY, 'Key Requirement'),
		(HIGH, 'High'),
		(MEDIUM, 'Medium'),
		(LOW, 'Low'),
	]

	priority = models.CharField(
		max_length=2,
		choices=PRIORITY_CHOICES,
		default=None,
		blank=True
	)

	DRAFT = 'DR'
	CANDIDATE = 'CA'
	TRADED = 'TR'
	TRANSFERRED = 'TF'
	CANCELLED = 'CL'
	BASELINED = 'BA'

	STATUS_CHOICES = [
		(DRAFT, 'Draft'),
		(CANDIDATE, 'Candidate'),
		(TRADED, 'Traded'),
		(TRANSFERRED, 'Transferred'),
		(CANCELLED, 'Cancelled'),
		(BASELINED, 'Baselined'),
	]

	status = models.CharField(
		max_length=2,
		choices=STATUS_CHOICES,
		default=DRAFT,
	)

	def __str__(self):
		return "Requirement " + str(self.id) + " " + self.description

	# This function is used to define the return URL when the requirement is
    # updated.
	def get_absolute_url(self):
		return reverse('requirements:detail', kwargs={'pk': self.id})

	# This function is used to define the edit URL when the requirement is
	# displayed.
	def get_edit_url(self):
		return reverse('requirements:edit', kwargs={'pk': self.id})
