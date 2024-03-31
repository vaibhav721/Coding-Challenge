from django.http import JsonResponse
from .models import Population   

def query_view(request):
    username=request.GET.get('username',None)
    password=request.GET.get('password',None)
    if username=="vaibhav" and password=="vaibhav721":
        state = request.GET.get('State', None)
        county = request.GET.get('County', None)
        Gender=request.GET.get('Gender',None)
      #Validations State/County/Gender
        if state is None or not state.strip(): 
            return JsonResponse({'error': 'State is required'}, status=400)

        if county is None or not county.strip():  
            return JsonResponse({'error': 'County is required'}, status=400)

        if Gender is not None and Gender not in ['Male', 'Female']: 
            return JsonResponse({'error': 'Gender must be "Male" or "Female"'}, status=400)
        
        queryset = Population.objects.filter(State=state,County__contains=county)

        if queryset.exists():
            print("Queryset enter")
            population_data=queryset.first()

            if(Gender=="Female"):
                filtered_result = { 
                'County': population_data.County,
                'State': population_data.State,
                'Under5yrsPopulation': population_data.Under5yrsPopulation_female,
                't5to17yrs': population_data.t5to17yrs_Female,
                't18to24yrs': population_data.t18to24yrs_Female,
                't25to34years': population_data.t25to34years_Female,
                't35to44yrs': population_data.t35to44yrs_Female,
                't45to64yrs': population_data.t45to64yrs_Female,
                't65to84yrs': population_data.t65to84yrs_Female,
                't85to99yrs': population_data.t85to99yrs_Female,
                't100yrs_and_over': population_data.t100yrs_and_over_Female
                }

                print(filtered_result)
                return JsonResponse(filtered_result, safe=False)       
            else:
                filtered_result = {
                    'County': population_data.County,
                    'State': population_data.State,
                    'Under5yrsPopulation': str(int(population_data.Under5yrsPopulation_total) - int(population_data.Under5yrsPopulation_female)),
                    't5to17yrs': str(int(population_data.t5to17yrsPopulation_total) - int(population_data.t5to17yrs_Female)),
                    't18to24yrs': str(int(population_data.t18to24yearsPopulation) - int(population_data.t18to24yrs_Female)),
                    't25to34years': str(int(population_data.t25to34yrs_Population) - int(population_data.t25to34years_Female)),
                    't35to44yrs': str(int(population_data.t35to44yrs_Population) - int(population_data.t35to44yrs_Female)),
                    't45to64yrs': str(int(population_data.t45to64yrs_Population) - int(population_data.t45to64yrs_Female)),
                    't65to84yrs': str(int(population_data.t65to84years_Population) - int(population_data.t65to84yrs_Female)),
                    't85to99yrs': str(int(population_data.t85to99yrs_Population) - int(population_data.t85to99yrs_Female)),
                    't100yrs_and_over': str(int(population_data.t100_years_and_Over_Population) - int(population_data.t100yrs_and_over_Female))
                } 
                return JsonResponse(filtered_result,safe=False)
            
        else:
            return JsonResponse({}, status=404)
    else:
        return JsonResponse({}, status=404)



def state_county_list(request):
    username=request.GET.get('username',None)
    password=request.GET.get('password',None)

    if username=="vaibhav" and password=="vaibhav721":
        state = request.GET.get('State', None)
        queryset = Population.objects.filter(State=state)
        
        if queryset.exists():
            county_names = [obj.County.rstrip('County').strip() for obj in queryset]

        return JsonResponse(county_names,safe=False)
    else:
        return JsonResponse(county_names,safe=False)
