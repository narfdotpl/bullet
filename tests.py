#!/usr/bin/env python
# encoding: utf-8

from imp import load_source
from unittest import TestCase, main

bullet = load_source('bullet', 'bullet')


class ApplyBreakpointsTests(TestCase):

    def assert_correct(self, text, expected_result):
        self.assertEqual(bullet.apply_breakpoints(text), expected_result)

    def test_it_doesnt_change_text_without_breakpoints(self):
        text = 'foo\nbar\nbaz'
        self.assert_correct(text, text)

    def test_requires_a_bullet_and_a_slide_beginning_marker(self):
        text = 'foo•bar'
        self.assert_correct(text, text)

    def test_applies_one_breakpoint_correctly(self):
        self.assert_correct("""
---
foo•bar
""", """
---
foo

---
foobar
""")

    def test_applies_two_breakpoints_correctly(self):
        self.assert_correct("""
---
foo•bar•baz
""", """
---
foo

---
foobar

---
foobarbaz
""")

    def test_adds_triple_backticks_where_needed(self):
        self.assert_correct("""
---
```
foo•bar
```
""", """
---
```
foo
```

---
```
foobar
```
""")

    def test_handles_the_README_example(self):
        self.assert_correct("""
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
""", """
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
""")


if __name__ == '__main__':
    main()
