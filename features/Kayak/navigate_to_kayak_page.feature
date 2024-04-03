@regression_tests

Feature: Validate element created dropdown column

  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The page "should" contain the next elements
      | name        | type   |
      | origin      | input  |
      | destination | input  |
      | start_date  | span   |
      | fin_date    | span   |
      | search      | button |

  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The url page should be equal to the next "https://www.kayak.com.co/" url

  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |

  Scenario Outline: Verify page loading for each option
    Given I navigate to the kayak main page
    When I click on the "<option>" option
    Then The "<title>" from page "<option>" should load correctly

    Examples:
      | option       | title                                                       |
      | Vuelos       | Busca en cientos de webs de vuelos a la vez.                |
      | Alojamientos | Busca el alojamiento perfecto para ti.                      |
      | Carros       | Busca en cientos de webs de alquiler de carros en segundos. |
      | Paquetes     | Busca los mejores paquetes turísticos en oferta             |
