Datenschutz und Sicherheit
==========================

Lange vor der NSA-Affäre beschäftigten wir uns schon mit der Erhöhung von
Datenschutz und -sicherheit von Web-Anwendungen. Hierzu luden wir bereits im
August 2011 unabhängige Experten ein um mit uns gemeinsam Maßnahmen für ein. dem
Bundesdatenschutzgesetz (BDSG) konformen, Web-Hosting zu erarbeiten [#]_.

Seitdem arbeiten wir kontinuierlich an der Verbesserung der
Informationssicherheit. Hierfür erstellen wir ein :abbr:`ISMS
(Informationssicherheits-Managementsystem)`, das nach der ISO 27000-Normenreihe
zertifiziert wird.

Daher sind wir sehr glücklich, dass wir nun auch das Vertrauen der `Gesellschaft
für Datenschutz und Datensicherheit <https://www.gdd.de/>`_ gewinnen konnten.

.. Aber auch Sie können von unseren Services profitieren. So sind unsere Services
   gut geschützt gegen:

   * `Elementare Gefährdungen
     <https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Inhalt/_content/g/g00/g00.html>`_
   * `Höhere Gewalt
     <https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Inhalt/_content/g/g01/g01.html>`_
   * `Organisatorische Mängel
     <https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Inhalt/_content/g/g02/g02.html>`_
   * `Menschliche Fehlhandlungen
     <https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Inhalt/_content/g/g03/g03.html>`_
   * `Technisches Versagen
     <https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Inhalt/_content/g/g04/g04.html>`_
   * `Vorsätzliche Handlungen
     <https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Inhalt/_content/g/g05/g05.html>`_

Damals wie heute orientieren wir uns im Wesentlichen an den in `Anlage zu § 9
Satz 1`_ beschriebenen Maßnahmen zum Schutz personenbezogener Daten:

.. _`Anlage zu § 9 Satz 1`: http://www.gesetze-im-internet.de/bdsg_1990/anlage_79.html

Zutrittskontrolle
-----------------

    Unbefugten ist der Zutritt zu Datenverarbeitungsanlagen, mit denen
    personenbezogene Daten verarbeitet oder genutzt werden, zu verwehren.

Das Hosting erfolgt über die `Hostsharing eG <hostsharing.net>`_. Deren Server
sind im Alboin-Kontor in einem eigenen Cage untergebracht, für den Vor-Ort-
Service nutzt die  Hostsharing eG die Dienste der `Sinma GmbH
<http://www.sinma.de/>`_. Die Zutrittskontrolle zum Rechenzentrum erfolgt über
die folgenden Authentifizierungs­systeme:

* Zugangskarte
* PIN
* Videoüberwachung
* Cage-Schließanlage
* Rack-Schließanlage

Zugangskontrolle
----------------

    Es ist zu verhindern, dass Datenverarbeitungssysteme von Unbefugten genutzt
    werden können.

Um dies zu gewährleisten, wird ein breites Spektrum an Maßnahmen getroffen. Im
Einzelnen:

Zugangsrechner
~~~~~~~~~~~~~~

* Die Festplatten der Zugangsrechner sind verschlüsselt
* Die darauf befindlichen SSH-Schlüssel sind zusätzlich mit einer Passphrase
  geschützt

Passwortverfahren
~~~~~~~~~~~~~~~~~

Service-User
::::::::::::

* Die Nutzer-Identifikation erfolgt ausschließlich über persönliche Nachweise
  (Credentials) sodass Aktionen immer auf eine bestimmte Person zurückgeführt
  werden können
* Geteilte Berechtigungen sind nicht zulässig
* SSH-Anmeldungen erfolgen ausschließlich mittels SSH-Keys
* Erfolgreiche SSH-Logins werden protokolliert
* Wechsel in Service-User mit ``sudo``

Hosts
:::::

#. Reguläre Zugänge

   * VPN-Zugang ausschließlich für Hostmaster der Hostsharing eG
   * Personenbezogener ssh-Zugang mit SSH-Key
   * ``sudo`` mit persönlichem Passwort
   * Zugriffe werden protokolliert

#. Zugänge im Notfall

   * via Remote Access Cards

     * VPN-Zugang
     * Personenbezogener Login mit persönlichem Passwort
     * Login mit ``root``-Passwort via RAC-Konsole
     * Zugriffe werden protokolliert und dokumentiert

   * via Vor-Ort-Zugriff

     * Login mit ``root``-Passwort
     * Zugriffe werden protokolliert und dokumentiert

#. Web services

   Web services zur Auftragsdatenverarbeitung wie `JIRA
   <https://www.atlassian.com/de/software/jira>`_,
   `Confluence <https://www.atlassian.com/de/software/confluence>`_, `Jenkins
   <http://jenkins-ci.org/>`_ und `Sentry
   <https://github.com/getsentry/sentry>`_ versenden ausschließlich an Mailboxen
   der Hostsharing eG. Damit kann gewährleistet werden, dass der Transport mit
   ``TLS`` verschlüsselt wird. Der Abruf der Mails erfolgt ausschließlich mit
   ``TLS``.

#. Netzwerke

   Eine bessere Zugangskontrolle im Netzwerk wird gewährleistet durch die
   Einrichtung verschiedener physikalisch getrennter Netze oder VLANs, die durch
   eine Firewall im Gateway getrennt werden. Dabei werden die Netze im
   Wesentlichen danach unterschieden, welcher Traffic in ihnen zu erwarten ist:

   Frontend-Netzwerk
    physikalisch getrenntes Netz für allgemeine Anfragen
   Server-Netzwerk
    für die Kommunikation der Anwendungen untereinander
   Speichernetzwerk
    Punkt-zu-Punkt-Verbindung zur Replikation

    Die Festplatteninhalte werden mithilfe von `DRBD <http://www.drbd.org/>`_ in
    Echtzeit auf ein Standby-System (`RAID 1
    <http://de.wikipedia.org/wiki/RAID#RAID_1:_Mirroring_.E2.80.93_Spiegelung>`_
    über das Netzwerk) repliziert.

    Dies soll sicherstellen, dass im Fall eines Hardwareschadens der Betrieb mit
    allen persistent gespeicherten Daten unverzüglich fortgesetzt werden kann,
    ohne dass durch das Einspielen des Backups Datenänderungen, die sich in der
    Zwischenzeit ergeben haben – etwa eingegangene E-Mails oder
    Datenbanktransaktionen – verloren gehen.

   Backup-Netzwerk
    SSH-Tunnel zum `interxion
    <http://www.interxion.com/de/standorte/deutschland/frankfurt/>`_-
    Rechenzentrum in Frankfurt
   Management-Netzwerk
    physikalisch getrenntes Netz an dem die Hosts, die aktiven
    Netzwerkkomponenten und die Remote-Access-Karten der Hosts angeschlossen
    sind

Zugriffskontrolle
-----------------

    Es ist zu gewährleisten, dass die zur Benutzung eines
    Datenverarbeitungssystems Berechtigten ausschließlich auf die ihrer
    Zugriffsberechtigung unterliegenden Daten zugreifen können, und dass
    personenbezogene Daten bei der Verarbeitung, Nutzung und nach der
    Speicherung nicht unbefugt gelesen, kopiert, verändert oder entfernt werden
    können.

* Wir unterscheiden zwischen Aufgaben zur Instandhaltung der Anwendungen und
  privilegierten Aufgaben zur Aktualisierung und Konfiguration des
  Betriebssystems.
* Benötigt ein Anwendungsentwickler zur Lösung eines Problems privilegierten
  Zugang, so erfolgt dies in einer Multiuser-Session mit `GNU Screen
  <http://www.gnu.org/software/screen/>`_ oder `TeamViewer
  <http://www.teamviewer.com/de/>`_ zusammen mit einem Administrator.
* Logs

  * sie werden nicht per Mail verschickt
  * Logs der Anwendungen werden im Server-Netzwerk an den Monitoring-Server
    übertragen
  * Systemlogs werden über ``TLS``-Verbindungen an die internen und externen
    Logging-Sever übertragen

Weitergabekontrolle
-------------------

    Es ist zu gewährleisten, dass personenbezogene Daten bei der elektronischen
    Übertragung oder während ihres Transports oder ihrer Speicherung auf
    Datenträger nicht unbefugt gelesen, kopiert, verändert oder entfernt werden
    können, und dass überprüft und festgestellt werden kann, an welche Stellen
    eine Übermittlung personenbezogener Daten durch Einrichtungen zur
    Datenübertragung vorgesehen ist.

Alle personenbezogenen Daten werden ausschließlich über authentifizierte und
verschlüsselte Kommunikationskanäle übertragen. Hierzu gehören auch

* Anwendungsdaten, die von oder zu einem Nutzer per ``SFTP``/``SCP``
  transferiert werden
* der Transfer persistenter Daten, die auf einem Backup-Server gespeichert sind
* Log-Dateien

  * werden zu einem zentralen Log-Server im Service-Netz übertragen
  * werden nach der Log-Retention-Period entfernt

Eingabekontrolle
----------------

    Es ist zu gewährleisten, dass nachträglich überprüft und festgestellt werden
    kann, ob und von wem personenbezogene Daten in Datenverarbeitungssysteme
    eingegeben, verändert oder entfernt worden sind (Nr. 5 der Anlage zu § 9
    BDSG).

* Die Eingabe als ``root``-Nutzer wird mit `ttyrec <http://0xcc.net/ttyrec/>`_
  protokolliert
* JIRA protokolliert Änderungen an den Aufgaben in sog. *Work-Logs*
* Änderungen an den Konfigurationsdateien werden in git-Repositories
  protokolliert

Auftragskontrolle
-----------------

    Es ist zu gewährleisten, dass personenbezogene Daten, die im Auftrag
    verarbeitet werden, nur entsprechend den Weisungen des Auftraggebers
    verarbeitet werden können.

* Alle Aufgaben werden in der Auftragsverwaltung JIRA festgehalten
* Für die Verarbeitung personenbezogene Daten ist eine Weisung des Auftraggebers
  erforderlich

Verfügbarkeitskontrolle
-----------------------

    Es ist zu gewährleisten, dass personenbezogene Daten gegen zufällige
    Zerstörung oder Verlust geschützt sind.

Backups

* täglich
* Speicherung in entferntem Rechenzentrum
* Produktivsysteme haben auf gesicherte Daten ausschließlich Lesezugriff
* Notfallpläne, die Ausfallszenarien, Vorsorgemaßnahmen und Maßnahmen zur
  Beseitigung beschreiben

Trennungskontrolle
------------------

    Es ist zu gewährleisten, dass zu unterschiedlichen Zwecken erhobene Daten
    getrennt verarbeitet werden können.

* Die zu unterschiedlichen Zwecken erhobenen Daten werden getrennt verarbeitet
* Verschiedene Unix-User separieren die Verarbeitung der Daten
* Verschiedene Netzwerke trennen die Übermittlung von Daten

----

.. [#] `Sicherheit und Datenschutz bei Web-Anwendungen <http://www.pysprints.de/sicherheit-und-datenschutz/index.html>`_
