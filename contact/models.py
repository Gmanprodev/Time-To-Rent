from django.db import models

customer_query = [
    ('general_query', 'General Query'),
    ('technical_issue', 'Technical Issue'),
    ('plan_query', 'Plan Query'),
    ('delivery', 'Delivery'),
]


class Contact(models.Model):
    """ Model for create Contact Form """
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    contact_reason = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default='general_query')
    message = models.TextField(max_length=1500, null=False, blank=False)

    def __str__(self):
        return f'{self.contact_reason} - {self.full_name}'
