"""Route and static-reference checks for the rendered static website."""

import re
from urllib.parse import unquote

from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


PAGES = {
    "home": "website/index.html",
    "about": "website/navbar/about.html",
    "contact": "website/navbar/contact.html",
    "services": "website/navbar/service.html",
    "why_choose_us": "website/navbar/whychooseus.html",
    "privacy": "website/privacy.html",
    "terms": "website/terms.html",
    "procurement_supply_chain": "website/service-section/psm.html",
    "general_trading_logistics": "website/service-section/gtl.html",
    "digital_solutions": "website/service-section/digital.html",
    "strategic_procurement": "website/service-section/service-procurement-details/stategic.html",
    "industrial_equipment": "website/service-section/service-procurement-details/industrial.html",
    "laboratory_equipment": "website/service-section/service-procurement-details/laboratory.html",
    "specialized_equipment": "website/service-section/service-procurement-details/specialized Equipment.html",
    "furniture_appliances": "website/service-section/service-procurement-details/furniture&appliances.html",
    "woodworking_equipment": "website/service-section/service-procurement-details/woodworking.html",
    "agricultural_commodities": "website/service-section/service-generaltrading-details/Agricultural.html",
    "air_freight": "website/service-section/service-generaltrading-details/airfreight.html",
    "customs_clearance": "website/service-section/service-generaltrading-details/customs.html",
    "inland_transportation": "website/service-section/service-generaltrading-details/Inlandtranspo.html",
    "ocean_freight": "website/service-section/service-generaltrading-details/oceanfreight.html",
    "petroleum_logistics": "website/service-section/service-generaltrading-details/servicepl.html",
    "warehousing": "website/service-section/service-generaltrading-details/warehousing.html",
    "ai_data_science": "website/service-section/service-digital-details/ai&data.html",
    "cctv_surveillance": "website/service-section/service-digital-details/cctv&surveillance.html",
    "hardware_systems": "website/service-section/service-digital-details/hardware.html",
    "network_solutions": "website/service-section/service-digital-details/networking.html",
    "it_solutions": "website/service-section/service-digital-details/serviceit.html",
    "software_solutions": "website/service-section/service-digital-details/software.html",
    "subsidiaries": "website/subsidiaries-section/subsidia.html",
    "afrilott_overseas": "website/subsidiaries-section/oversea.html",
    "transtrade_africa": "website/subsidiaries-section/transtrade.html",
    "afos": "website/subsidiaries-section/afos.html",
}


class MigratedPageTests(SimpleTestCase):
    def test_every_page_renders_and_its_local_static_files_exist(self):
        static_url = settings.STATIC_URL
        pattern = re.compile(r'(?:href|src)=["\'](' + re.escape(static_url) + r'[^"\']+)["\']')

        for name, template_name in PAGES.items():
            with self.subTest(page=name):
                response = self.client.get(reverse(f"website:{name}"))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template_name)

                for asset_url in pattern.findall(response.content.decode()):
                    asset_path = unquote(asset_url.removeprefix(static_url).split("?", 1)[0])
                    self.assertIsNotNone(finders.find(asset_path), asset_path)

    def test_templates_do_not_keep_local_html_navigation(self):
        local_html_link = re.compile(r'''(?:href|src)=["\'](?!https?://)[^"\']*\.html(?:[?#][^"\']*)?["\']''')

        for template_name in PAGES.values():
            with self.subTest(template=template_name):
                template_path = settings.BASE_DIR / "templates" / template_name
                self.assertIsNone(local_html_link.search(template_path.read_text(encoding="utf-8")))

    def test_healthcheck_returns_ok(self):
        response = self.client.get("/healthz/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")

    def test_rendered_markup_matches_the_original_except_link_destinations(self):
        attribute_value = re.compile(r'''\b(href|src)\s*=\s*["\'][^"\']*["\']''', re.IGNORECASE)

        def normalize(markup):
            markup = markup.replace("\r\n", "\n")
            return attribute_value.sub(lambda match: f'{match.group(1)}="__PATH__"', markup)

        for name, template_name in PAGES.items():
            with self.subTest(page=name):
                original_path = settings.BASE_DIR / template_name.removeprefix("website/")
                original = original_path.read_text(encoding="utf-8")
                rendered = self.client.get(reverse(f"website:{name}")).content.decode()
                self.assertEqual(normalize(rendered), normalize(original))
