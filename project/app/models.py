from django.db import models

class Asset_table(models.Model):
    uid = models.CharField(primary_key=True, max_length=256)
    asset_code = models.CharField(max_length=256)
    asset_desc = models.CharField(max_length=256)

class RFIDData(models.Model):
    sum_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class NewTable(models.Model):
    sum_value = models.IntegerField()
    
class Kit_table(models.Model):
    kit_id = models.CharField(primary_key=True, max_length=256)
    uid = models.ForeignKey(Asset_table, on_delete=models.CASCADE)
    in_loc_place = models.CharField(max_length=256)
    in_loc_ts = models.DateTimeField(null=True, blank=True)

class Kit_table2(models.Model):
    kit_id = models.CharField(primary_key=True, max_length=256)
    uid = models.ForeignKey(Asset_table, on_delete=models.CASCADE)
    out_loc_place = models.CharField(max_length=256)
    out_loc_ts = models.DateTimeField(null=True, blank=True)

class locations(models.Model):
    kit_id = models.ForeignKey(Kit_table, on_delete=models.CASCADE)
    in_loc = models.CharField(max_length=256)
    out_loc = models.CharField(max_length=256)
