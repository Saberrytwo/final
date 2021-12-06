# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PdDrugs(models.Model):
    drugid = models.IntegerField(primary_key=True)
    drugname = models.CharField(max_length=30, unique=True)
    isopioid = models.CharField(max_length=5)

    class Meta:
        #managed = False
        db_table = 'pd_drugs'
    
    def __str__ (self):
        return(self.drugname)


class PdPrescriber(models.Model):
    npi = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.CharField(max_length=2)
    credentials = models.CharField(max_length=18, blank=True, null=True)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'pd_prescriber'

    def __str__ (self):
        return(self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.fname, self.lname)


class PdPrescribersCredentials(models.Model):
    npi = models.ForeignKey(PdPrescriber, to_field="npi", db_column="npi", primary_key=True, on_delete=models.DO_NOTHING)
    credentials = models.CharField(max_length=20)

    class Meta:
        #managed = False
        db_table = 'pd_prescribers_credentials'
        unique_together = (('npi', 'credentials'),)

    def __str__ (self):
        return(self.npi)

    @property
    def fullCreds(self):
        return '%s %s' % (self.credentials)


class PdStatedata(models.Model):
    state = models.CharField(primary_key=True, max_length=14)
    stateabbrev = models.CharField(max_length=2)
    population = models.IntegerField()
    deaths = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'pd_statedata'

    def __str__ (self):
        return(self.state)


class PdTriple(models.Model):
    id = models.IntegerField(primary_key=True)
    prescriberid = models.ForeignKey(PdPrescriber, to_field="npi", db_column="prescriberid", on_delete=models.DO_NOTHING)
    drugname = models.ForeignKey(PdDrugs, to_field="drugname", db_column="drugname", on_delete=models.DO_NOTHING)
    qty = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'pd_triple'

    def __str__ (self):
        return(self.qty)
