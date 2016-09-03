from ckan_scraper import scrape_resources
from geojson_scraper import scrape


base_url = 'https://data.yorkopendata.org/api/3/action/package_show?id='

stations_info = {
    'dataset': 'polling-stations',
    'extra_fields': [],
    'return_format': 'GeoJSON',
}

districts_info = {
    'dataset': 'polling-districts',
    'extra_fields': [],
    'return_format': 'GeoJSON'
}

council_id = 'E06000014'


stations_url = scrape_resources(
    base_url,
    stations_info['dataset'],
    stations_info['return_format'],
    stations_info['extra_fields'],
    'utf-8')
districts_url = scrape_resources(
    base_url,
    districts_info['dataset'],
    districts_info['return_format'],
    districts_info['extra_fields'],
    'utf-8')


if stations_url:
    scrape(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID_1')
if districts_url:
    scrape(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
