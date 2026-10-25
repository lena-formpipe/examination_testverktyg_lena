# US04 Som en användare vill jag
# kunna lägga till en bok i katalogen
# så att katalogen över böcker kan kompletteras med fler böcker.
#
# US06 Som en användare vill jag
# kunna navigera till de olika funktionerna
# så att jag kan nå den den funktion jag behöver
#noinspection CucumberUndefinedStep

  
Feature: Lägga till en bok

  Scenario: Lägg till en bok
    Given jag har navigerat till vyn Lägg till bok
    When jag lägger till boktitel Hunger Games
    And jag lägger till författarnamn Sean Banan
    And jag klickar på knappen Lägg till ny bok
    Then inmatningsfälten ska vara tomma
    And knappen Lägg till ny bok ska vara inaktiv
    And boken Hunger Games ska ligga i Katalogen

  Scenario: Kan inte lägga till bok med enbart titel
    Given jag har navigerat till vyn Lägg till bok
    When jag lägger till boktitel Hunger Games
    Then knappen Lägg till ny bok ska vara inaktiv

  Scenario: Kan inte lägga till bok med enbart författarnamn
    Given jag har navigerat till vyn Lägg till bok
    When jag lägger till författarnamn Sean Banan
    Then knappen Lägg till ny bok ska vara inaktiv

  Scenario: Visa vyn Lägg till bok
    Given jag surfar till Läslistan
    When jag klickar på knappen Lägg till bok
    Then ska information om att lägga till bok visas
    And knappen Lägg till bok ska vara inaktiv

