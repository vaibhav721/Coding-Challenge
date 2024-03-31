from django.db import models


class Population(models.Model):
    State = models.TextField(("State"))
    County = models.TextField(("County"))
    Under5yrsPopulation_total =models.TextField(("Under5yrsPopulation_total"))
    Under5yrsPopulation_female = models.TextField(("Under5yrsPopulation_female"))
    t5to17yrsPopulation_total = models.TextField(("t5to17yrsPopulation_total"))
    t5to17yrs_Female = models.TextField(("t5to17yrs_Female"))
    t18to24yearsPopulation = models.TextField(("t18to24yearsPopulation"))
    t18to24yrs_Female = models.TextField(("t18to24yrs_Female"))
    t25to34yrs_Population = models.TextField(("t25to34yrs_Population"))
    t25to34years_Female = models.TextField(("t25to34years_Female"))
    t35to44yrs_Population = models.TextField(("t35to44yrs_Population"))
    t35to44yrs_Female = models.TextField(("t35to44yrs_Female"))
    t45to64yrs_Population = models.TextField(("t45to64yrs_Population"))
    t45to64yrs_Female = models.TextField(("t45to64yrs_Female"))
    t65to84years_Population = models.TextField(("t65to84years_Population"))
    t65to84yrs_Female = models.TextField(("t65to84yrs_Female"))
    t85to99yrs_Population = models.TextField(("t85to99yrs_Population"))
    t85to99yrs_Female = models.TextField(("t85to99yrs_Female"))
    t100_years_and_Over_Population = models.TextField(("t100_years_and_Over_Population"))
    t100yrs_and_over_Female = models.TextField(("t100yrs_and_over_Female"))


    class Meta:
        verbose_name = "Population"
        verbose_name_plural = "Population" 
        
    
 