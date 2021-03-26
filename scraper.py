from dc_base_scrapers.ckan_scraper import CkanScraper
from dc_base_scrapers.geojson_scraper import GeoJsonScraper


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

council_id = 'YOR'


stations_meta_scraper = CkanScraper(
    base_url,
    council_id,
    stations_info['dataset'],
    stations_info['return_format'],
    stations_info['extra_fields'],
    'utf-8')
stations_url = stations_meta_scraper.scrape()

districts_meta_scraper = CkanScraper(
    base_url,
    council_id,
    districts_info['dataset'],
    districts_info['return_format'],
    districts_info['extra_fields'],
    'utf-8')
districts_url = districts_meta_scraper.scrape()

if stations_url:
    stations_scraper = GeoJsonScraper(
        stations_url, council_id, 'utf-8', 'stations', key='OBJECTID_1')
    stations_scraper.scrape()

if districts_url:
    districts_scraper = GeoJsonScraper(
        districts_url, council_id, 'utf-8', 'districts', key='OBJECTID_1')
    districts_scraper.scrape()
