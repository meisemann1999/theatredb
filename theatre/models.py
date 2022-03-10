# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import random
from django.db import IntegrityError, models
import phonenumbers


class Accounting(models.Model):
    subgroup_id = models.AutoField(db_column='Subgroup_ID', primary_key=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', blank=True, null=True, max_length=30)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    entry_name = models.TextField(db_column='Entry_Name', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ACCOUNTING'
        app_label = 'theatre'
    
    def __str__(self):
        return self.type + " - " + self.entry_name + " (" + str(self.amount) + ")"


class Department(models.Model):
    department_id = models.AutoField(db_column='Department_ID', primary_key=True)  # Field name made lowercase.
    department_name = models.TextField(db_column='Department_Name', unique=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DEPARTMENT'
        app_label = 'theatre'
    
    def __str__(self):
        return self.department_name


class Employee(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', unique=True, max_length=7, primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', blank=True, null=True, max_length= 16)  # Field name made lowercase.
    minit = models.CharField(db_column='MInit', blank=True, null=True, max_length = 1)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', blank=True, null=True, max_length = 30)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', unique=True, max_length=9)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length = 60, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.CharField(db_column='City', max_length = 35, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zip = models.CharField(db_column='ZIP', blank=True, null=True, max_length = 5)  # Field name made lowercase.
    supervisor_id = models.ForeignKey('self', on_delete=models.SET_NULL, db_column='Supervisor_ID', blank=True, null=True, max_length = 10)  # Field name made lowercase.
    earns = models.ForeignKey(Accounting, models.DO_NOTHING, db_column='Earns', blank=True, null=True)  # Field name made lowercase.
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='Department', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.CharField(db_column='Phone', blank=True, null=True, max_length = 12)  # Field name made lowercase.
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='Role', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'
        app_label = 'theatre'
    
    def generate_id(self):
        id = self.fname[0].lower() + self.lname[0:2].lower() + "_" + str(random.randint(100, 999))
        return id

    # def save(self, *args, **kwargs):
    #     self.employeeid = self.generate_id()
    #     super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.fname + " "  + self.lname


            

    def format_phone(self, country='US'):
        return phonenumbers.format_number(phonenumbers.parse(self.phone, country), phonenumbers.PhoneNumberFormat.NATIONAL) 



class Equipment(models.Model):
    inventory_id = models.CharField(db_column='Inventory_ID', unique=True, max_length = 15, primary_key=True)  # Field name made lowercase.
    brand = models.TextField(db_column='Brand', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    condition = models.TextField(db_column='Condition', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_notes = models.TextField(db_column='Repair_notes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    event_id = models.ForeignKey('Event', on_delete=models.SET_NULL, db_column='Event_ID', blank=True, null=True, max_length = 15)  # Field name made lowercase.
    checked_out_by = models.ForeignKey('Employee', on_delete=models.SET_NULL, db_column='Checked_out_by', blank=True, null=True, max_length = 10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EQUIPMENT'
        app_label = 'theatre'


class Event(models.Model):
    event_id = models.CharField(db_column='Event_ID', unique=True, max_length = 15, primary_key=True)  # Field name made lowercase.
    venue = models.TextField(db_column='Venue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    event_name = models.CharField(db_column='Event_Name', blank=True, null=True, max_length = 50)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT'
        app_label = 'theatre'


class Login(models.Model):
    employeeid = models.OneToOneField(Employee, on_delete=models.CASCADE, db_column='EmployeeID', unique=True, max_length =7, primary_key=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase. This field type is a guess.
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='Role', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOGIN'
        app_label = 'theatre'


class Role(models.Model):
    role_id = models.AutoField(db_column='Role_ID', primary_key=True)  # Field name made lowercase.
    role_name = models.TextField(db_column='Role_Name', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ROLE'
        app_label = 'theatre'
    
    def __str__(self):
        return self.role_name
