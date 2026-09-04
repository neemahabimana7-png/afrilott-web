from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("why-choose-us/", views.why_choose_us, name="why_choose_us"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("services/procurement-supply-chain/", views.procurement_supply_chain, name="procurement_supply_chain"),
    path("services/general-trading-logistics/", views.general_trading_logistics, name="general_trading_logistics"),
    path("services/digital-solutions/", views.digital_solutions, name="digital_solutions"),
    path("services/procurement/strategic-procurement/", views.strategic_procurement, name="strategic_procurement"),
    path("services/procurement/industrial-equipment/", views.industrial_equipment, name="industrial_equipment"),
    path("services/procurement/laboratory-equipment/", views.laboratory_equipment, name="laboratory_equipment"),
    path("services/procurement/specialized-equipment/", views.specialized_equipment, name="specialized_equipment"),
    path("services/procurement/furniture-appliances/", views.furniture_appliances, name="furniture_appliances"),
    path("services/procurement/woodworking-equipment/", views.woodworking_equipment, name="woodworking_equipment"),
    path("services/logistics/agricultural-commodities/", views.agricultural_commodities, name="agricultural_commodities"),
    path("services/logistics/air-freight/", views.air_freight, name="air_freight"),
    path("services/logistics/customs-clearance/", views.customs_clearance, name="customs_clearance"),
    path("services/logistics/inland-transportation/", views.inland_transportation, name="inland_transportation"),
    path("services/logistics/ocean-freight/", views.ocean_freight, name="ocean_freight"),
    path("services/logistics/petroleum-logistics/", views.petroleum_logistics, name="petroleum_logistics"),
    path("services/logistics/warehousing/", views.warehousing, name="warehousing"),
    path("services/digital/ai-data-science/", views.ai_data_science, name="ai_data_science"),
    path("services/digital/cctv-surveillance/", views.cctv_surveillance, name="cctv_surveillance"),
    path("services/digital/hardware-systems/", views.hardware_systems, name="hardware_systems"),
    path("services/digital/network-solutions/", views.network_solutions, name="network_solutions"),
    path("services/digital/it-solutions/", views.it_solutions, name="it_solutions"),
    path("services/digital/software-solutions/", views.software_solutions, name="software_solutions"),
    path("subsidiaries/", views.subsidiaries, name="subsidiaries"),
    path("subsidiaries/afrilott-overseas/", views.afrilott_overseas, name="afrilott_overseas"),
    path("subsidiaries/transtrade-africa/", views.transtrade_africa, name="transtrade_africa"),
    path("subsidiaries/afrilott-overseas/afos/", views.afos, name="afos"),
]
