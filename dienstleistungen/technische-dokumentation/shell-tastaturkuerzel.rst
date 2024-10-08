Shell-Tastaturkürzel
====================

Verwenden der Historie
----------------------

``Pfeil oben``
    erlaubt Ihnen das Navigieren durch die letzten
    Befehle wobei Sie zum nächstfrüheren Befehl kommen.
``Pfeil unten``
    erlaubt Ihnen das Navigieren durch die letzten
    Befehle wobei Sie zum nächstspäteren Befehl kommen.
``!!``
    Wiederholt den letzten Befehl.

    So wird :abbr:`z.B. (zum Beispiel)` mit

    .. code-block:: console

        $ sudo !!

    der letzte Befehl mit den Rechten des Superusers
    ausgeführt.

``!foo``
    führt den letzten Befehl aus, der mit ``foo`` begann.

    Falls Sie sich unsicher sind, welches der letzte Befehl mit ``foo`` war,
    können Sie sich mit ``!foo:p`` zunächst diesen Befehl anzeigen lassen.

    Eine übliche Befehlsabfolge ist demnach:

    .. code-block:: console

        $ !find:p
        find ~/tmp/* -mmin +10 -exec rm -rf {} \; >/dev/null 2>&1
        $ !!
        find ~/tmp/* -mmin +10 -exec rm -rf {} \; >/dev/null 2>&1

``foo !$``
    führt den Befehl ``foo`` aus mit den Attributen des
    vorigen Befehls, also z.B.:

    .. code-block:: console

        mkdir ~/new//folder
        cd !$

``!123``
    führt den Befehl aus, der in der Historie an 123ster
    Stelle aufgeführt ist. Ein typisches Szenario ist, dass wir zunächst in der Historie
    alle Befehle suchen, die ``find`` enthalten und anschließend den passenden ausführen:

    .. code-block:: console

        $ history | grep find
          224  find ~/tmp/* -mmin +10 -exec rm -rf {} \; >/dev/null 2>&1
          513  history | grep find
        $ !224
        find ~/tmp/* -mmin +10 -exec rm -rf {} \; >/dev/null 2>&1

Navigieren innerhalb von Befehlen
---------------------------------

``Esc + B``
    springt in Ihrem Befehl ein Argument nach links
``Esc + F``
    springt in Ihrem Befehl ein Argument nach rechts
``Ctrl + A``
    springt an den Anfang des Befehls
``Ctrl + E``
    springt an das Ende des Befehls
``Ctrl + U``
    löscht die Zeile vom Cursor zum Beginn der nächsten
    Zeile
``Ctrl + A``
    verschiebt den Cursor zum Anfang der Zeile
``Ctrl + E``
    verschiebt den Cursor zum Ende der Zeile
``Ctrl + R``
    erlaubt die Suche in früheren Befehlen

Expansion
---------

``{}``
    Geschweifte Klammern erlauben das ausführen von
    Befehlen auf mehrere Dateien gleichzeitig, z.B.:

    .. code-block:: console

        $ mkdir vs.policy/{trunk,branches,tags}

Aliase
------

Es können Aliase von Befehlen in der Bash-Konfigurationsdatei unter ``~/.bash_profile`` angegeben, z.B.:

.. code-block:: console

    alias ll='ls -ahlF'

Weitere Beispiele finden Sie :abbr:`z.B. (zum Beispiel)` in
:ref:`grep-Umgebungsvariablen <umgebungsvariablen>`.

Auto-Vervollständigung
----------------------

Die Bash liefert bereits viele Arten der Auto-Vervollständigung, z.B. für Pfade, Dateien, Nutzer, Hosts und Variablen.

Pfade
    das erste Wort einer Zeile wird zum Pfad einer
    ausführbaren Datei vervollständigt
Dateinamen
    das zweite Wort einer Zeile wird zu einem Datei- oder
    Verzeichnisnamen vervollständigt
Benutzernamen
    die Eingabe von ``~`` wird zu den Benutzernamen
    vervollständigt
Hostnamen
    die Eingabe von ``@`` wird zu den Hostnamen
    vervollständigt
Variablen
    wird dem Wort ``$`` vorangestellt, so wird zu einer Umgebungsvariablen vervollständigt

Bash-Completion
~~~~~~~~~~~~~~~

Wir haben Bash-Completion bereits installiert, es muss von Ihnen lediglich noch aktiviert werden indem Sie in der ``~/.bashrc``-Datei folgendes angeben:

.. code-block:: console

    if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
        . /etc/bash_completion
    fi

Anschließend erhalten Sie für die Unix-Befehle, aber auch für weitere Programme wie z.B. ``apache``, ``git``, ``mercurial``, ``paster`` und ``subversion`` programmatische Vervollständigungen.

.. Eigene Erweiterungen hinzufügen
   :::::::::::::::::::::::::::::::

   Sie können auch selbst programmatische
   Vervollständigungen schreiben in
   ``~/.bash_completion`` wobei Sie darauf achten
   sollten, dass die Datei ausführbar ist.

   Siehe auch: `Pro-Linux: Programmierbare Eingabe-Vervollständigung in Bash <http://www.pro-linux.de/artikel/2/153/2,programmierbare-eingabe-vervollstaendigung-in-bash.html>`_
