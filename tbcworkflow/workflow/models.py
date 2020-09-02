from django.db import models
from django.utils import timezone

class Project(models.Model):
    projectID = models.CharField(max_length=30)
    sampleID = models.CharField(max_length=30)
    enterprise = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    expire = models.DateField()
    
    class Meta:
        ordering = ('-projectID',)
        
    def __str__(self):
        return self.projectID

class Sample(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sampleName = models.CharField(max_length=50)
    sampleType = models.CharField(max_length=30)
    sampleNumber = models.CharField(max_length=30)
    deliverPerson = models.CharField(max_length=30)
    deliverEnterprise = models.CharField(max_length=100)
    reveivePerson = models.CharField(max_length=30)
    receiveDate = models.DateField()
    
    class Meta:
        ordering = ('-receiveDate',)
        
    def __str__(self):
        return self.sampleName

class Sequence(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sequenceType = models.CharField(max_length=30)
    sequenceBases = models.CharField(max_length=30)
    sequencePerson = models.CharField(max_length=30)
    sequenceExtract = models.CharField(max_length=30)
    sequenceExtractDate = models.DateField()
    sequenceQC = models.CharField(max_length=30)
    sequenceQCDate = models.DateField()
    sequencePurify = models.CharField(max_length=30)
    sequencePurigyDate = models.DateField()
    sequenceBreak = models.CharField(max_length=30)
    sequenceBreakDate = models.DateField()
    sequenceLib = models.CharField(max_length=30)
    sequenceLibDate = models.DateField()
    sequenceBP = models.CharField(max_length=30)
    sequenceBPDate = models.DateField()
    sequenceRun = models.CharField(max_length=30)
    sequenceRunDate = models.DateField()
    sequenceText = models.CharField(max_length=200)

class Assembly(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assemblySurvey = models.CharField(max_length=30)
    assemblySurveyDate = models.DateField()
    assemblyContig = models.CharField(max_length=30)
    assemblyContigDate = models.DateField()
    assemblyHic = models.CharField(max_length=30)
    assemblyHicDate = models.DateField()
    assemblyText = models.CharField(max_length=200)

class Genemodel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    genemodelRepeat = models.CharField(max_length=30)
    genemodelRepeatDate = models.DateField()

class Analyse(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    analyseTree = models.CharField(max_length=30)
    analyseTreeDate = models.DateField()

