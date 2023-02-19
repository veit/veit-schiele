vim
===

Kurzreferenz für den Texteditor vim.

+------------------------+--------------------------------------------------------+
| Befehl                 | Beschreibung                                           |
+========================+========================================================+
| **Starten**                                                                     |
+------------------------+--------------------------------------------------------+
| vim *Datei*            | vim starten und Laden von *Datei*                      |
+------------------------+--------------------------------------------------------+
| vim *Datei1* *Datei2*  | vim starten und Laden von *Datei1* und *Datei2*        |
+------------------------+--------------------------------------------------------+
| vim -R *Datei*         | vim starten und Laden von *Datei* im Nur-Lesen-Modus   |
+------------------------+--------------------------------------------------------+
| **Speichern und Beenden**                                                       |
+------------------------+--------------------------------------------------------+
| :w                     | Speichern der Datei                                    |
+------------------------+--------------------------------------------------------+
| :w!                    | Speichern der Datei auch wenn sie im Nur-Lesen-Modus   |
|                        | geöffnet wurde                                         |
+------------------------+--------------------------------------------------------+
| :w Datei               | Speichern der Datei unter dem Dateinamen *Datei*       |
+------------------------+--------------------------------------------------------+
| :wq                    | Speichern der Datei und Verlassen von vim              |
+------------------------+--------------------------------------------------------+
| :q!                    | Beenden von vim und Verwerfen der Änderungen           |
+------------------------+--------------------------------------------------------+
| **Laden von Dateien**                                                           |
+------------------------+--------------------------------------------------------+
| :e Datei2              | Laden von Datei2                                       |
+------------------------+--------------------------------------------------------+
| :e! Datei              | Lädt Datei neu und verwirft die bisherigen Änderingen  |
+------------------------+--------------------------------------------------------+
| :e +n Datei            | Laden von Datei und Springen in Zeile n der Datei      |
+------------------------+--------------------------------------------------------+
| :e + Datei             | Laden von Datei und Springen ans Ende der Datei        |
+------------------------+--------------------------------------------------------+
| :args                  | Liste der geöffneten Dateien                           |
+------------------------+--------------------------------------------------------+
| **Cursorbewegungen**                                                            |
+------------------------+--------------------------------------------------------+
| :0                     | Springt zum Anfang der Datei                           |
+------------------------+--------------------------------------------------------+
| :n                     | Springt zu Zeile n der Datei                           |
+------------------------+--------------------------------------------------------+
| :$                     | Springt zum Ende der Datei                             |
+------------------------+--------------------------------------------------------+
| 0                      | Springt zum Anfang der Zeile                           |
+------------------------+--------------------------------------------------------+
| ^                      | Springt zum ersten Zeichen, das kein Leerzeichen ist   |
+------------------------+--------------------------------------------------------+
| $                      | Springt zum Ende der Zeile                             |
+------------------------+--------------------------------------------------------+
| ``return``             | Springt zur nächsten Zeile                             |
+------------------------+--------------------------------------------------------+
| w                      | Springt ein Wort vorwärts                              |
+------------------------+--------------------------------------------------------+
| b                      | Springt ein Wort rückwärts                             |
+------------------------+--------------------------------------------------------+
| )                      | Springt zum nächsten Satz                              |
+------------------------+--------------------------------------------------------+
| (                      | Springt zum vorherigen Satz                            |
+------------------------+--------------------------------------------------------+
| }                      | Springt zum nächsten Absatz                            |
+------------------------+--------------------------------------------------------+
| {                      | Springt zum vorherigen Absatz                          |
+------------------------+--------------------------------------------------------+
| **Einfügen und Ändern**                                                         |
+------------------------+--------------------------------------------------------+
| i                      | Aktiviert den Eingabemodus vor dem Cursor              |
+------------------------+--------------------------------------------------------+
| I                      | Aktiviert den Eingabemodus am Zeilenanfang             |
+------------------------+--------------------------------------------------------+
| A                      | Aktiviert den Eingabemodus am Zeilenende               |
+------------------------+--------------------------------------------------------+
| ``esc``                | Eingabemodus beenden                                   |
+------------------------+--------------------------------------------------------+
| J                      | Entfernt den Zeilenumbruch am Ende einer Zeile,        |
|                        | fügt also die aktuelle und die folgende Zeile zusammen.|
+------------------------+--------------------------------------------------------+
| x                      | Löscht das Zeichen unter dem Cursor                    |
+------------------------+--------------------------------------------------------+
| dw                     | Löscht das Wort                                        |
+------------------------+--------------------------------------------------------+
| d *n* w                | Löscht die folgenden *n* Wörter                        |
+------------------------+--------------------------------------------------------+
| D                      | Löscht alles bis zum Ende der Zeile                    |
+------------------------+--------------------------------------------------------+
| d^                     | Löscht alles bis zum Anfang der Zeile                  |
+------------------------+--------------------------------------------------------+
| dd                     | Zeile löschen                                          |
+------------------------+--------------------------------------------------------+
| *n* d                  | Löscht *n* Zeilen                                      |
+------------------------+--------------------------------------------------------+
| **Kopieren und Einfügen**                                                       |
+------------------------+--------------------------------------------------------+
| yy                     | Kopiert die Zeile                                      |
+------------------------+--------------------------------------------------------+
| *n* yy                 | Kopiert *n* Zeilen                                     |
+------------------------+--------------------------------------------------------+
| p                      | Fügt die kopierten Zeilen nach der aktuellen Zeile ein.|
|                        |                                                        |
|                        | Auch gelöschte Zeilen können so wieder eingefügt       |
|                        | werden.                                                |
+------------------------+--------------------------------------------------------+
| P                      | Fügt die kopierten Zeilen vor der aktuellen Zeile ein. |
|                        |                                                        |
|                        | Auch gelöschte Zeilen können so wieder eingefügt       |
|                        | werden.                                                |
+------------------------+--------------------------------------------------------+
| :v                     | Um Absätze neu zu fromatieren, wird zunächst in den    |
|                        | Visual-Mode gewechselt,                                |
|                        |                                                        |
| ↑ → ↓ ←                | anschließend der gewünschte Abschnitt markiert         |
|                        |                                                        |
| gqa                    | und schließlich ``gpa`` eingegeben.                    |
+------------------------+--------------------------------------------------------+
| **Suchen und Ersetzen**                                                         |
+------------------------+--------------------------------------------------------+
| / *Zeichenkette*       | Vorwärts suchen                                        |
+------------------------+--------------------------------------------------------+
| ? *Zeichenkette*       | Rückwärts suchen                                       |
+------------------------+--------------------------------------------------------+
| n                      | Wiederholt das letzte / oder ? Kommando                |
+------------------------+--------------------------------------------------------+
| N                      | Wiederholt das letzte / oder ? Kommando                |
|                        | in umgekehrter Suchrichtung                            |
+------------------------+--------------------------------------------------------+
| :1,$s/alt/neu/g        | ersetzt jedes Vorkommen von *alt* durch *neu*          |
+------------------------+--------------------------------------------------------+
| :X,Ys/alt/neu/g        | ersetzt von Zeile X bis Zeile Y jedes Vorkommen        |
|                        | von *alt* durch *neu*                                  |
+------------------------+--------------------------------------------------------+
| **Split Screen**                                                                |
+------------------------+--------------------------------------------------------+
| :split Datei           | teilt die Ansicht der Dateien horizontal               |
+------------------------+--------------------------------------------------------+
| :vsplit Datei          | teilt die Ansicht der Dateien vertikal                 |
+------------------------+--------------------------------------------------------+
| Ctrl-W h               | wechselt zum linken Fenster                            |
+------------------------+--------------------------------------------------------+
| Ctrl-W j               | wechselt zum unteren Fenster                           |
+------------------------+--------------------------------------------------------+
| Ctrl-W k               | wechselt zum oberen Fenster                            |
+------------------------+--------------------------------------------------------+
| Ctrl-W l               | wechselt zum rechten Fenster                           |
+------------------------+--------------------------------------------------------+
| **Verschiedenes**                                                               |
+------------------------+--------------------------------------------------------+
| u                      | rückgängig machen des letzten Kommandos                |
+------------------------+--------------------------------------------------------+
| U                      | Rückgängig machen auf einer Zeile                      |
+------------------------+--------------------------------------------------------+
| Ctrl-r                 | Wiederherstellen                                       |
+------------------------+--------------------------------------------------------+
| ~                      | Ändert die Groß- und Kleinschreibung                   |
+------------------------+--------------------------------------------------------+
| .                      | Wiederholt das letzte Kommando                         |
+------------------------+--------------------------------------------------------+

Vi mode in Bash
---------------

Die Bash-Shell kann konfiguriert werden in ``~/.bashrc`` und ``~/.inputrc``. Um
nun den vi-Modus in der Bash und anderen Werkzeugen zu verwenden, die GNU
Readline verwenden, müssen Sie nur die folgende Zeile in Ihre ``~/.inputrc``-
Datei übernehmen:

.. code-block:: console

    set editing-mode vi

Falls Sie den Bearbeitungsmodus nur für die Bash ändern wollen, können Sie
stattdessen die ``~/.bashrc`` konfigurieren:

.. code-block:: console

    set -o vi

Mit dem folgenden Befehl können Sie überprüfen, ob die Änderungen übernommen
wurden:

.. code-block:: console

    $ bind -P

Dies sollte eine Liste der verfügbaren Bindings ausgeben.

Nun sollte eine Befehlszeile im Eingabemodus von vi geöffnet werden. Wollen Sie
diesen Modus verlassen und in den normalen vi-Modus zu wechseln, können Sie
einfach die ``esc``-Taste drücken. Anschließend erhalten Sie die typischen vi-
Bindings, also z.B.:

``^``
    Zum Anfang der Zeile springen
``$``
    Zum Ende der Zeile springen
``b``
    Zum Anfang des Wortes springen
``w``
    Zum Ende des Wortes springen
``e``
   Zum Ende des nächsten Wortes springen

.. seealso::
   * `Selflinux: Wichtige vi-Kommandos <http://www.selflinux.org/selflinux/html/vim04.html>`_
   * `vi für Fortgeschrittene <http://debiananwenderhandbuch.de/vi.html>`_
   * `Best of Vim Tips <http://www.rayninfo.co.uk/vimtips.html>`_
   * `Ian Langworth: Vim After 15 Years <https://statico.github.io/vim3.html>`_
