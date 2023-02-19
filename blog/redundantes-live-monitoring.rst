Redundantes Live-Monitoring
===========================

In der Folge des `MonitoringLove-Sprints
<http://www.pysprints.de/monitoringlove/>`_ im Juni 2013 haben wir begonnen,
unser Monitoring nach und nach umzustellen um in Echtzeit relevante
Informationen zu erhalten. Ein Problem des damaligen Setups war jedoch, dass
es Lücken in der Aufzeichnung gab sobald ein Monitoring-Node ausfiel.

|Apache Cassandra Logo|

Nun haben wir mit `Apache Cassandra <http://cassandra.apache.org/>`_ eine
Möglichkeit gefunden, diese Lücken zu schließen da sich Cassandra :abbr:`ggf.
(gegebenenfalls)` resynchronisiert sofern auch nur ein Node immer
erreichbar ist.

.. |Apache Cassandra Logo| image:: cassandra_logo.png
   :class: image-right

Zukünftig wird an jedem der beiden Rechenzentrumsstandorte einen
Monitoring-Node betrieben. Durch ein entsprechendes `Resource Record
<https://de.wikipedia.org/wiki/Resource_Record>`_-Set kann eine einfache
Verteilung auf die beiden Standorte gewährleistet werden. Zudem wird jeder
Admin einen *Monitoring-Client* auf seinem Notebook oder PC haben, der auf einen
der Monitoring-Nodes zugreift.

Im Einzelnen setzen wir nun folgende Toolchain ein:

#. `collectd <http://collectd.org/>`_ zur Erfassung der Daten
#. `riemann <http://riemann.io/>`_ zur Aggregation der Events
#. `cyanite <https://github.com/pyr/cyanite>`_ zur persistenten und redundanten
   Speicherung mittels Apache Cassandra und `Elasticsearch
   <http://www.elasticsearch.org/>`_.
#. `graphite-api <http://graphite.readthedocs.org/en/latest/render_api.html>`_
   zur Abfrage von Clients mit dem Graphite-Protokoll.

Dabei erfolgt die Netzwerkkommunikation von allen Systemen zu den `Riemann
<http://riemann.io/>`_-Instanzen via `stunnel
<http://en.wikipedia.org/wiki/Stunnel>`_ und von den Clients zum REST-Service
mit ``HTTPS``.
