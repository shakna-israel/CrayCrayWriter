# CrayCrayWriter

A system for programmatically generating a story.

Inspired by the many NaNoGenMo projects.

---

## Example

An example book can be found in [outBook.md](outBook.md)

---

## Basic Usage

To write a book to file, run the following within Python:

```python
import CrayCrayWriter

insane = CrayCrayWriter()
insane.decide_map()
insane.decide_room_objects()
insane.write_book()
```

A MarkDown document, ```outBook.md``` will be produced.

---

## License

[MIT License](LICENSE.md)
