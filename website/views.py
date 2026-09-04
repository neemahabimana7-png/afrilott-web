"""Render-only views for the existing Afrilott frontend templates."""

from django.http import HttpResponse
from django.shortcuts import render


def _render(request, template_name):
    return render(request, template_name)


def healthcheck(request):
    """Minimal unauthenticated health endpoint for the platform proxy."""
    return HttpResponse("ok", content_type="text/plain")


def home(request): return _render(request, "website/index.html")
def about(request): return _render(request, "website/navbar/about.html")
def contact(request): return _render(request, "website/navbar/contact.html")
def services(request): return _render(request, "website/navbar/service.html")
def why_choose_us(request): return _render(request, "website/navbar/whychooseus.html")
def privacy(request): return _render(request, "website/privacy.html")
def terms(request): return _render(request, "website/terms.html")

def procurement_supply_chain(request): return _render(request, "website/service-section/psm.html")
def general_trading_logistics(request): return _render(request, "website/service-section/gtl.html")
def digital_solutions(request): return _render(request, "website/service-section/digital.html")

def strategic_procurement(request): return _render(request, "website/service-section/service-procurement-details/stategic.html")
def industrial_equipment(request): return _render(request, "website/service-section/service-procurement-details/industrial.html")
def laboratory_equipment(request): return _render(request, "website/service-section/service-procurement-details/laboratory.html")
def specialized_equipment(request): return _render(request, "website/service-section/service-procurement-details/specialized Equipment.html")
def furniture_appliances(request): return _render(request, "website/service-section/service-procurement-details/furniture&appliances.html")
def woodworking_equipment(request): return _render(request, "website/service-section/service-procurement-details/woodworking.html")

def agricultural_commodities(request): return _render(request, "website/service-section/service-generaltrading-details/Agricultural.html")
def air_freight(request): return _render(request, "website/service-section/service-generaltrading-details/airfreight.html")
def customs_clearance(request): return _render(request, "website/service-section/service-generaltrading-details/customs.html")
def inland_transportation(request): return _render(request, "website/service-section/service-generaltrading-details/Inlandtranspo.html")
def ocean_freight(request): return _render(request, "website/service-section/service-generaltrading-details/oceanfreight.html")
def petroleum_logistics(request): return _render(request, "website/service-section/service-generaltrading-details/servicepl.html")
def warehousing(request): return _render(request, "website/service-section/service-generaltrading-details/warehousing.html")

def ai_data_science(request): return _render(request, "website/service-section/service-digital-details/ai&data.html")
def cctv_surveillance(request): return _render(request, "website/service-section/service-digital-details/cctv&surveillance.html")
def hardware_systems(request): return _render(request, "website/service-section/service-digital-details/hardware.html")
def network_solutions(request): return _render(request, "website/service-section/service-digital-details/networking.html")
def it_solutions(request): return _render(request, "website/service-section/service-digital-details/serviceit.html")
def software_solutions(request): return _render(request, "website/service-section/service-digital-details/software.html")

def subsidiaries(request): return _render(request, "website/subsidiaries-section/subsidia.html")
def afrilott_overseas(request): return _render(request, "website/subsidiaries-section/oversea.html")
def transtrade_africa(request): return _render(request, "website/subsidiaries-section/transtrade.html")
def afos(request): return _render(request, "website/subsidiaries-section/afos.html")
