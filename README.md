Bullet
======

Markdown processor written with the [Deckset][] app in mind.  Adds
"breakpoints" to slides (including code slides).

Breakpoints are denoted by the bullet symbol (`•`) that can be written
on OS X by pressing `⌥8`.

  [Deckset]: http://www.decksetapp.com/


Example
-------

Bullet changes this:

    # Hello, World!

    ---
    ``` swift
    func add(a: Int, b: Int) -> Int {
        return a + b
    }•

    add(0, 1)•  // 1
    ```

    ---
    # Goodbye, World!

into this:

    # Hello, World!

    ---
    ``` swift
    func add(a: Int, b: Int) -> Int {
        return a + b
    }
    ```

    ---
    ``` swift
    func add(a: Int, b: Int) -> Int {
        return a + b
    }

    add(0, 1)
    ```

    ---
    ``` swift
    func add(a: Int, b: Int) -> Int {
        return a + b
    }

    add(0, 1)  // 1
    ```

    ---
    # Goodbye, World!


Rationale
---------

I prepare my slides like this, so it's more obvious to me what to talk
about and more clear to the audience what to look at.  Bullet makes the
process easier and the resulting file [smaller][diff].

  [diff]: #TODO


Usage
-----

    $ cat source.md | bullet > slides.md


Installation
------------

Add `bullet` to your `$PATH`.


Meta
----

Written by [Maciej Konieczny](http://narf.pl/) and released into
public domain.
