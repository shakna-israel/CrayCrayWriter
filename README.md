# CrayCrayWriter

A system for programmatically generating a story.

Inspired by the many NaNoGenMo projects.

---

## Example

Elizabeth is in the Backyard.

Micah is in the Library.

Kate is in the Torture Chamber.

Andrew is in the Lounge.


---

Elizabeth talked to the helmet. She kissed the chair. She loved the scroll. She cried because of the english text book. She cuddled the scroll.

---

Micah talked to the crystal. He loved the crystal. He farted at the Door. He laughed at the Door.

---

Kate observed the Door. She stared at the helmet. She cuddled the speaker.

---

Andrew kicked the ghost. He stared at the chair. He observed the ghost. He farted at the Door. He cheered the ghost. He punched the mug. He licked the codex. He stroked the mug.

---

Further Reading Examples:

* [Markdown](outBook.md)
* [PDF](outBook.pdf)
* [Website](http://shakna-israel.github.io/CrayCrayWriter/)

---

## Basic Usage

To write a book to file, run the following within Python:

```python
form craycraywriter import CrayCrayWriter

insane = CrayCrayWriter()
insane.decide_map()
insane.decide_room_objects()
insane.write_book()
```

A MarkDown document, ```outBook.md``` will be produced.

---

## License

[MIT License](LICENSE.md)

---

## Notes

As each characters strand is seperated from another, their sentences should be read as if they had each occured at the same time.

For why?

In rare cases more than one character can move rooms, and then interact with each other. This may appear confusing at first.
