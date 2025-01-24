from business.models import BusinessInformation
import json
def read_json(path):
    with open(path,'r') as file:
        data = json.loads(file.read())
        return data

data = read_json('./localhost.json')
data = data[8]['data']
BusinessInformation.objects.all().delete()

for i, item in enumerate(data):
    b = BusinessInformation.objects.create(
        abn=item['abn'],
        availability=item['availability'],
        awards=item['awards'],
        business_name=item['business_name'],
        category=item['category'],
        contact_information=item['contact_information'],
        current_url=item['current_url'],
        description=item['description'],
        email=item['email'],
        equipment_provided=item['equipment_provided'],
        experience=item['experience'],
        insurance_coverage=item['insurance_coverage'],
        license_number=item['license_number'],
        location=item['location'],
        phone_number=item['phone_number'],
        primary_services=item['primary_services'],
        rating_avg=item['rating_avg'],
        response_time=item['response_time'],
        reviews=item['reviews'],
        service_area=item['service_area'],
        social_media=item['social_media'],
        specializations=item['specializations'],
        trade_type=item['trade_type'],
        website=item['website'],
        lat_long=item['lat_long'],
    )
    b.save()
    print(f'Adding item {i} out of {len(data)}')
