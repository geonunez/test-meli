# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Human(models.Model):
    """
    Human model.
    """

    dna = models.TextField(unique=True)
    is_mutant = models.BooleanField(default=False)

    def __str__(self):
        return self.dna
