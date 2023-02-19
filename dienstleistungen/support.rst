Support
=======

Wir verstehen Support als Teil des Entwicklungsprozesses.

Agile Software-Entwicklung bei gleichzeitigem Support
-----------------------------------------------------

Wir entwickeln Ihre Individualsoftware agil – und sind so in der Lage, Ihnen
funktionierende Software schnell und zu einem frühen Zeitpunkt zu liefern. Dabei
wird häufig eine frühere Version Ihrer Software produktiv genutzt – entweder ein
zu ersetzendes Legacy-System oder unser neues, sich noch in der Entwicklung
befindliche System oder beides.

Bei der agilen Entwicklung achten wir üblicherweise darauf, dass das
Entwicklungsteam ihre Sprint-Ziele und -Verpflichtungen einhalten kann, wobei
sie während Ihrer Arbeit nicht unterbrochen werden sollen. Auf der anderen Seite
liefern wir unsere Software früh und häufig an unsere Kunden aus, damit diese
die Software so bald wie möglich produktiv nutzen können. Und die für die
Nutzung der Software benötigte Unterstützung und Hilfe erhalten Sie am besten
von den Entwicklern selbst.

Wir mussten nun also einen Weg finden, Support und Wartungsarbeiten in Einklang
zu bringen mit Design und Entwicklung qualitativ hochwertiger Software innerhalb
festgelegter Zeiten. Don Schueler beschreibt in seinem Artikel `The Fragile
Balance between Agile Development and Customer Support
<http://servicestrategies.com/community/articles/the-fragile-balance-between-agile-development-and-customer-support/>`_
ausführlich die Diskrepanz zwischen Entwicklungs- und Support-Teams:
Entwicklungsteams seien eher nach innen gerichtet und auf Code-Qualität und
technische Belange fokussiert während Support-Teams nach außen gerichtet und auf
die Kundenbeziehung konzentriert seien.

#. Extreme Programming

   Zunächst haben wir, wie Kent Beck und Martin Fowler in Ihrem Buch `Planning
   Extreme Programming
   <http://www.amazon.de/Planning-Extreme-Programming-Kent-Beck/dp/0201710919>`_
   vorgeschlagen haben, mit einem Support-Team von 2 Entwicklern gearbeitet, die
   sich auf Bug-Fixes und operative Probleme konzentrierten. Diese arbeiteten,
   bevor Sie in den Support gingen, im Entwicklungsteam und kehrten danach auch
   wieder dorthin zurück. Damit gewährleisteten wir die Verbindung zu den
   aktuellen Entwicklungen, dennoch blieb der Support eine Randerscheinung. Auch
   ließ sich der Umfang der Wartungs- und Support-Arbeiten nicht mit den Zyklen
   des Entwicklungsteams in Einklang bringen.

#. Kanban

   Hier erschien uns `Kanban <http://swreflections.blogspot.ca/2012/08/what-can-you-get-out-of-kanban.html>`_
   deutlich besser geeignet, zwischen Development, Support, Maintenance und
   Operations zu vermitteln: Das Queuing-Model und die Nutzung von Task-Boards
   erleichtert den Überblick, welche Arbeiten getan werden müssen und welche
   Arbeiten bereits von wem übernommen wurden (s.a. `Combining Scrum with Kanban
   for support and enhancement teams <http://www.innovel.net/?p=40>`_). Dies
   erleichterte uns die Koordinierung von verschiedenartigen Arbeiten, die
   unterschiedliche Fähigkeiten und Zeitfenster erfordern.

#. DevOps

   `DevOps <http://devops.com/>`_, wie sie von `Etsy
   <http://codeascraft.com/2011/02/04/how-does-etsy-manage-development-and-operations/>`_, `Facebook <http://arstechnica.com/business/2012/04/exclusive-a-behind-the-scenes-look-at-facebook-release-engineering/>`_
   et al.  verfolgt wird, riss dann vollständig die Grenzen zwischen
   Entwicklung, Wartung, Support und Betrieb ein. In einer solchen Organisation
   sind die Entwickler selbst verantwortlich für ihre Software im gesamten
   Lebenszyklus, s.a. `Development and Deployment at Facebook
   <https://www.facebook.com/download/1411324735760067/devops.pdf>`_.

   DevOps änderte die Art und Weise, wie unsere Entwickler arbeiteten: Sie
   bewegen sich weg von der Projektarbeit hin zu schneller Feature-Entwicklung,
   Fein-Tuning und Härten. Verfügbarkeit, Zuverlässigkeit, Performance und
   Sicherheit gewannen viel mehr Gewicht als Liefertermine und
   Entwicklungsgeschwindigkeit.

Wartung und Support – Verantwortung und Feedback
------------------------------------------------

Es gibt überzeugende Vorteile, Entwickler direkt in die Unterstützung und
Wartung der Software zu beteiligen, s.a. `Should software engineers also act as
tech support?
<http://programmers.stackexchange.com/questions/35819/should-software-engineers-also-act-as-tech-support>`_.
Das wichtigste ist `Feedback
<http://www.ambysoft.com/essays/whyAgileWorksFeedback.html>`_ zu erhalten von
einem realen System. Dieses Feedback wird benötigt um herauszufinden, was
wirklich nützlich für den Kunden ist und wo das bisherige Design nicht mehr
passt. So kann ein Umbau geplant und gewichtet werden.

Resümee
-------

In den letzten Jahren konnten wir kontinuierlich den Support für unsere Kunden
verbessern und **gleichzeitig** erhielten unsere Entwickler die Informationen,
die sie benötigen. Das Ergebnis ist, dass wir in den letzten Jahren immer
weniger ernsthafte Probleme hatten und sich auch die Zeiten, in denen wir diese
Probleme lösen konnten, deutlich verringerte.

Heute nutzen wir die Vorteile der Agilität nicht mehr nur für die Entwicklung
der Software, sondern für alle Bereiche in deren Lebenszyklus. Damit können wir
viel schneller auf Probleme und sich ändernde Anforderungen in Produktivsystemen
reagieren und sind damit einer nachhaltigen Entwicklung deutlich näher gekommen.

.. Quelle: `Don't You Know that Support is the Most Important Part of a
   Developer’s Job? <http://swreflections.blogspot.ca/2013/10/dont-you-know-that-support-is-most.html>`_
