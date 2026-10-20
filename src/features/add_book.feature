#noinspection CucumberUndefinedStep

Feature: F-004 Lägga till en bok
  Scenario: Lägg till en bok
    Given jag har navigerat till vyn Lägg till bok
    When jag lägger till en boktitel
    And jag lägger till ett författarnamn
    And jag klickar på knappen Lägg till ny bok
    Then inmatningsfälten ska vara tomma
    And knappen Lägg till ny bok ska vara inaktiv
    And boken ska läggas till i Katalogen

  Scenario: Kan inte lägga till bok med enbart titel
    Given jag har navigerat till vyn Lägg till bok
    When jag lägger till en boktitel
    Then knappen Lägg till ny bok ska vara inaktiv

  Scenario: Kan inte lägga till bok med enbart författarnamn
    Given jag har navigerat till vyn Lägg till bok
    When jag lägger till ett författarnamn
    Then knappen Lägg till ny bok ska vara inaktiv

  Scenario: Visa vyn Lägg till bok
    Given jag surfar till Läslistan
    When jag klickar på knappen Lägg till bok
    Then ska information om att lägga till bok visas
    And knappen Lägg till bok ska vara inaktiv

