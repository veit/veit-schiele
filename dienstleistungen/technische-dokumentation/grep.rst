grep
====

`grep <https://de.wikipedia.org/wiki/Grep>`_ ist ein Befehlszeilen-Werkzeug, das
der Suche und Filterung bestimmter Zeichenketten in Dateien dient. Hier ein
Beispiel:

.. code-block:: console

    $ grep -ir --include="*.pt" -B 2 -A 2 content-core src/vs.theme

``-i``
    ignoriert die Groß- und Kleinschreibung
``-r``
    durchsucht Verzeichnisse rekursiv
``--include``
    nur Dateien mit diesem Muster werden durchsucht, in unserem Fall Zope Page
    Templates mit der Endung ``.pt``.
``-B``
    Anzahl der Zeilen, die vor einem Suchergebnis angezeigt werden sollen
``-A``
    Anzahl der Zeilen, die nach einem Suchergebnis angezeigt werden sollen

.. _umgebungsvariablen:

Umgebungsvariablen
------------------

Die generelle Konfiguration der Umgebungsvariablen von ``grep`` lässt sich in
der ``–/.bashrc`` angeben. So können  z.B. mit ``--exclude-dir`` die
Verzeichnisse, in denen Versionsverwaltungen ihre Metainformationen abspeichern
ignoriert werden:

.. code-block:: console

    GREP_OPTIONS=
    if grep --help | grep -- --exclude-dir &>/dev/null; then
        for PATTERN in .cvs .git .hg .svn; do
            GREP_OPTIONS="$GREP_OPTIONS --exclude-dir=$PATTERN"
        done
    fi
    export GREP_OPTIONS

.. seealso::
   Eine vollständige Liste der Umgebungsvariablen erhalten Sie in `Environment
   Variables
   <http://www.gnu.org/software/grep/manual/html_node/Environment-Variables.html>`_.

Kolorieren
----------

.. code-block:: console

    export GREP_OPTIONS="--color=always $GREP_OPTIONS"
    export GREP_COLORS="ms=01;37:mc=01;37:sl=:cx=01;30:fn=35:ln=32:bn=32:se=36"
