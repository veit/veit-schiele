Fraunhofer-ISE: Unternehmenssuche
=================================

Januar bis April 2017: Unternehmenssuche für die Intranet-Anwendungen des Fraunhofer-ISE

.. figure:: ise-logo.gif
   :alt: Fraunhofer-ISE-Logo

Wir berieten das `Fraunhofer-Institut für Solare Energiesysteme ISE
<http://www.ise.fraunhofer.de/de>`_ bei der Einführung einer Unternehmenssuche.

Evaluation
----------

Zunächst evaluierten wir, welche technologische Plattform den Anforderungen des
Fraunhofer ISE an eine technologische Plattform genügen würde.

**Search-Appliances** wie `MaxxCAT <www.maxxcat.com/>`_, `Mindbreeze InSpire
<https://www.mindbreeze.com/de/enterprise-search-appliance>`_ oder `Thunderstone
<https://www.thunderstone.com/texis/site/pages/Appliance.html>`_ versprachen
zwar eine einfache und schnelle Bereitstellung sowie geringe Wartungs- und
Pflegeaufwände, die Nachteile überwogen jedoch deutlich:

* Schwierige oder keine Redundanz möglich
* Hohe Kosten für Server im Standby-Betrieb und zum Testen
* Aufwändige Überwachung der Lizenzauslastung

Auch **quelloffene Suchmaschinen**, wie `FESS <fess.codelibs.org/>`_ und
`OpenSearchServer <https://github.com/jaeksoft/opensearchserver>`_ wurden
evaluiert. Während FESS im Evaluationszeitraum auf das aktuelle Major-Release
von `elasticsearch <https://www.elastic.co/>`_ aktualisiert wurde, verblieb
der OpenSearchServer auf der nicht-API-kompatiblen Version 2. Desweiteren waren
beide Software-Lösungen im Bedarfsfall nur schwer erweiterbar.

.. figure:: elastic-stack.png
   :alt: elastic stack

Daher evaluierten wir anschließend den elastic stack selbst mit den Komponenten
`Elasticsearch River Web
<https://github.com/codelibs/elasticsearch-river-web>`_.
`FS Crawler <https://github.com/dadoonet/fscrawler>`_,
`IMAP/POP3/Mail importer
<https://github.com/salyh/elasticsearch-imap>`_ …
(s.a. `Elasticsearch Plugins and Integrations
<https://www.elastic.co/guide/en/elasticsearch/plugins/current/integrations.html>`_).

Elasticsearch 5 lässt sich darüberhinaus mit `X-Pack
<https://www.elastic.co/products/x-pack/>`_ einfach erweitern um die folgenden
Komponenten:

- `Security <https://www.elastic.co/de/products/x-pack/security>`_
  (vorm. Shield)
- `Reporting <https://www.elastic.co/de/products/x-pack/reporting>`_
- `Alerting <https://www.elastic.co/de/products/x-pack/alerting>`_
  (vorm. Watcher)
- `Monitoring <https://www.elastic.co/de/products/x-pack/monitoring>`_
  (vorm. Marvel)
- `Reporting <https://www.elastic.co/de/products/x-pack/reporting>`_
- `Graph <https://www.elastic.co/de/products/x-pack/graph>`_
- `Machine learning <https://www.elastic.co/de/products/x-pack/machine-learning>`_
  (Beta)

Zu beachten bleibt jedoch, dass X-Pack ein problematisches Lizenzmodell hat und
nach 30 Tagen viele Funktionen nicht mehr zur Verfügung stehen, s.a. `License Management
<https://www.elastic.co/guide/en/x-pack/current/license-management.html#license-management>`_.
Dennoch erschien es uns die praktikabelste Lösung für das Fraunhofer ISE zu
sein, zumal dort bereits ein elastic-Cluster mit
`Kibana <https://www.elastic.co/products/kibana>`_ und
`Logstash <https://www.elastic.co/de/products/logstash>`_ lief.

Realisation
-----------

Anschließend setzten wir einen Prototypen für das Fraunhofer ISE auf und
erweiterten ihn um die Anbindung an mehrere Sites auf Basis des  Enterprise
Content Management Systems `Plone <https://plone.org/>`_. Die Anbindung erfolgte
auf Basis von `collective.elasticindex
<https://pypi.python.org/pypi/collective.elasticindex/>`_.

.. seealso::
    * `Alternativen zur Google Search Appliance
      <https://de.slideshare.net/veitschielecom/gsa-alternativen>`_
