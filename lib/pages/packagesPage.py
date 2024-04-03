from lib.components.generalcomponents import GeneralComponents
from lib.pages.webelements.flightswebelements import FlightWebElements
from lib.pages.webelements.homewebelements import HomeWebElements
from lib.pages.webelements.packageselements import PackagesWebElements


class PackagesPage:
    def __init__(self, context):
        self.context = context
        self.web_driver = context.browser
        self.webElements = PackagesWebElements

    def validate_load_pages(self, title):
        tupleWebElement = self.webElements.title
        webElement = GeneralComponents.wait_until_element_is_present(self.context, tupleWebElement)
        text_element = webElement.text
        text_spect = title
        return text_spect in text_element
