Microservices: Jenseits der Monolithen
======================================

Große Anwendungen wie PayPal, Netflix oder Yelp sind dafür bekannt,
dass sie ihre Systeme fast beliebig skalieren können. Doch auch sie hatten bis
vor kurzem Probleme, ihren Systemen schnell genug erweitern oder ändern zu
können. Erst mit der Einführung modularer, entkoppelter Systeme, also mit
der Einführung der Microservices-Archtektur (MSA) konnten sie ihre Probleme
beseitigen.

Ziel dieser Architektur ist es, die einzelnen Services mit möglichst
geringen Abhängigkeiten erweitern und betreiben zu können. Zudem soll eine
vollständige Testabdeckung die kontinuierliche Übernahme in die
Produktivumgebung erlauben.

Die Idee hinter der MSA ist, auch bei komplexer Software besser auf
Kundenanforderungen eingehen zu können. Dabei ist unser agiler
Software-Entwicklungsprozess bestens geeignet, solche Architekturen zu
realisieren: wir werden noch schneller und flexibler auf Kundenanforderungen
reagieren können.

Warum Microservices?
--------------------

Früher sollten die Anwendungen mit klar definierten Schnittstellen (APIs) und
einer oder mehrerer Technologien zur `Orchestrierung
<http://de.wikipedia.org/wiki/Dienstekomposition#Orchestrierung>`_ beschrieben
werden. Mit zusätzlichen Werkzeugen sollten die zunehmend komplexer werdenden
Anwendungen auch für einen längeren Zeitraum beherrschbar bleiben.

Diese Methoden verhindern jedoch, dass sich eine Anwendung schnell den
geänderten Anforderungen angepasst werden kann. So können diese Anwendungen
schnell veralten oder immense Kosten verursachen um die nötigen Anpassungen
vorzunehmen.

Abhängigkeiten aus Entwicklerperspektive:

+------------------------+------------------------+------------------------+
| 1990er Jahre           | 2000er Jahre           | 2010er Jahre           |
+========================+========================+========================+
| monolithisch           | modular                | Microservices          |
+------------------------+------------------------+------------------------+
| Enge Kopplung          | Lose Kopplung          | entkoppelt             |
+------------------------+------------------------+------------------------+
| |Spaghetti|            | |Pizza|                | |Antipasti|            |
+------------------------+------------------------+------------------------+
| Um monolithische       | Module können etwas    | Entwickler können neue |
| Software zu ändern     | unabhängiger           | Microservices          |
| müssen alle beteiligten| entwickelt werden,     | erstellen und in       |
| Parteien involviert    | müssen jedoch          | Betrieb nehmen ohne    |
| sein.                  | weiterhin mit den      | sich mit anderen       |
| Jede Änderung wird     | anderen abgestimmt     | abstimmen zu müssen.   |
| unerwartete Effekte    | werden um in das       | Das einhalten der MSA- |
| zur Folge haben, die   | Gesamtdesign zu passen.| Prinzipien macht       |
| aufwändiges Testen     |                        | Continous Delivery     |
| erfordern.             |                        | neuer oder geänderter  |
|                        |                        | Services dennoch       |
|                        |                        | möglich.               |
+------------------------+------------------------+------------------------+

    Mit größerer Modularität, loser Kopplung und reduzierten Abhängigkeiten
    können Integrationsaufgaben vereinfacht werden!

.. |Spaghetti| image:: spaghetti.jpg
.. |Pizza| image:: pizza.jpg
.. |Antipasti| image:: antipasti.jpg
