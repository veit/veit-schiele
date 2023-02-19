Security-Checks
===============

Ein System in einem öffentlichen Netzwerk wird das Ziel von Angriffen werden
– daher müssen solche Systeme abgesichert werden.

Hier einige allgemeine Tipps, wie Dienste abgesichert werden können:

- Halten Sie alle Dienste aktuell um sie gegen aktuelle Bedrohungen abzusichern
- Verwenden Sie sichere Protokolle
- Bieten Sie nur einen Typ von Netzwerk-Dienste pro Maschine
- Achten Sie auf allen Servern sorgfältig auf verdächtige Aktivitäten.

Ports überprüfen
----------------

Nachdem Netzwerk-Dienste konfiguriert wurden ist es wichtig, einen Überblick zu
erhalten, an welchen Ports gerade welche Dienste lauschen.

Um z.B. herauszubekommen, welche Dienst gerade an welchen ports lauschen, kann
``nmap`` verwendet werden:

.. code-block:: console

    sudo nmap -sT -O dev1.veit-schiele.de
    …
    PORT     STATE    SERVICE
    22/tcp   open     ssh
    80/tcp   open     http
    135/tcp  filtered msrpc
    139/tcp  filtered netbios-ssn
    443/tcp  open     https
    445/tcp  filtered microsoft-ds
    8000/tcp open     http-alt
    8080/tcp open     http-proxy
    9010/tcp open     sdr

Um können Sie auf dem Server selbst nachschauen, ob der entsprechende Service
auch eingetragen ist in ``/etc/services``:

.. code-block:: console

    cat /etc/services | grep 9010
    sdr             9010/tcp                # Secure Data Replicator Protocol

Mit ``netstat`` erhalten Sie weitere Informationen:

.. code-block:: console

    netstat -anp | grep 9010
    tcp        0      0 0.0.0.0:9010                0.0.0.0:*                   LISTEN      5638/python

In unserem Fall lauscht also ein Python-Prozess mit der Process-ID (PID)
``5638`` am Port ``9010``.
