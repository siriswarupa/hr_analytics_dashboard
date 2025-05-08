# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Data(models.Model):
    employee_name = models.CharField(db_column='Employee_Name', max_length=100)  # Field name made lowercase.
    empid = models.BigIntegerField(db_column='EmpID', primary_key=True)  # Field name made lowercase.
    marriedid = models.BigIntegerField(db_column='MarriedID')  # Field name made lowercase.
    genderid = models.BigIntegerField(db_column='GenderID')  # Field name made lowercase.
    empstatusid = models.BigIntegerField(db_column='EmpStatusID')  # Field name made lowercase.
    deptid = models.BigIntegerField(db_column='DeptID')  # Field name made lowercase.
    fromdiversityjobfairid = models.BigIntegerField(db_column='FromDiversityJobFairID')  # Field name made lowercase.
    salary = models.BigIntegerField(db_column='Salary')  # Field name made lowercase.
    termd = models.BigIntegerField(db_column='Termd')  # Field name made lowercase.
    positionid = models.BigIntegerField(db_column='PositionID')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=100)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=10)  # Field name made lowercase.
    maritaldesc = models.CharField(db_column='MaritalDesc', max_length=50)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'data'
