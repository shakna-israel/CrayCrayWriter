from __future__ import print_function
from __future__ import unicode_literals

import random
import re

class CrayCrayWriter(object):
    """An object that can generate stories!"""

    def __init__(self):
        """Init all the data we need"""

        self.charactersDict = { "Kate":"She",
                            "Andrew":"He",
                            "Micah":"He",
                            "Elizabeth":"She"
                           }
        self.actionsDict = { "Punch": "the",
                         "Kick": "the",
                         "Yell": "at the",
                         "Ignor": "the",
                         "Us": "the",
                         "Observ": "the",
                         "Star": "at the",
                         "Patt": "the",
                         "Cuddl": "the",
                         "Kiss": "the",
                         "Talk": "to the",
                         "Fart": "at the",
                         "Laugh":"at the",
                         "Hat":"the",
                         "Lov":"the",
                         "Sneer":"at the",
                         "Jeer":"at the",
                         "Cheer":"the",
                         "Cri":"because of the",
                         "Strok":"the",
                         "Lick":"the",
                       }
        self.objects = ["Couch","Chair","TV","Computer","Cat","Dog","Table","Keyboard","Mouse","Mug","Glass","Speaker","Deoderant","Biscuit","Pizza","Fire Blanket","Walking Cane","Cane Sugar","Fire","Mummy","Ghost","Vampire","Zombie","Stone","Boulder","Axe","Reindeer","Elf","Spear","Pestle","Clay","Toy","Pot","Saucepan","Shower head","Envelope","Coat of arms","Tablet","Maths Text Book", "English Text Book","Cape","Dressing Gown","Vessel","Ship","Bell","Coin","Wallet","Purse","Pipe","Scroll","Plate","Fork","Knife","Staff","Sword","Helmet","Shield","Roof tile","Painting","Crystal","Tomb","Vase","Flower","Seat","Sculpture","Galleon","Elephant","Kangaroo","Prince","Codex","Drum","Poem","Compass","Penny","Village","Weapon","Lamp"]
        self.rooms = ["Bedroom","Library","Bathroom","Kitchen","Lounge","Playroom","Backyard","Laboratory","Maze","Torture Chamber","Mirror","Dreamworld","Digital Realm"]
        # self.map becomes a list of connections between rooms later on.
        self.map = dict()
        # A tracker for the current chapter
        self.chapters = 0

    def choose_character(self):
        """Randomly return one of the available characters"""

        return list(self.charactersDict)[random.randrange(0, len(self.charactersDict))]

    def choose_action(self):
        """Randomly return one of the possible actions"""

        return self.actionsDict[random.randrange(0, len(self.actionsDict))]

    def choose_object(self):
        """Randomly return one of the possible objects"""

        return self.objects[random.randrange(0, len(self.objects))].lower()

    def choose_room(self):
        """Randomly return one of the possible rooms"""

        return self.rooms[random.randrange(0, len(self.rooms))]

    def decide_map(self):
        """Generate a map of rooms and where they connect"""

        for room in self.rooms:
            self.map[room] = dict()
        for room in self.map:
            self.map[room]["connected"] = list()
        for room in self.map:
            self.map[room]["characters"] = list()
        for room in self.map:
            self.map[room]["objects"] = list()
        for room in self.map:
            iter = len(self.rooms) - 1
            while iter > 0:
                if random.randrange(0, 2) > 0:
                    randRoom = self.choose_room()
                    self.map[room]["connected"].append(randRoom)
                iter = iter - 1
        for room in self.map:
            self.map[room]["connected"] = list(set(self.map[room]["connected"]))
        return self.map

    def decide_room_objects(self):
        """Generate a list of objects and link them to a room"""

        for room in self.map:
            self.map[room]["objects"] = list()
            self.map[room]["objects"].append("Door")
        for room in self.map:
            iter = len(self.rooms) - 1
            while iter > 0:
                if random.randrange(0, 2) > 0:
                    randObj = self.choose_object()
                    self.map[room]["objects"].append(randObj)
                iter = iter - 1
        for room in self.map:
            self.map[room]["objects"] = list(set(self.map[room]["objects"]))
        return self.map

    def check_room_objects(self, room):
        """Check what objects are in the room"""

        return self.map[room]["objects"]

    def check_room_connected(self, room):
        """Check what rooms are connected"""

        return self.map[room]["connected"]

    def remove_character_location(self, character):
        """Remove a characters location from memory"""
        for room in self.map:
            if character in self.map[room]["characters"]:
                  self.map[room]["characters"] = [x for x in self.map[room]["characters"] if x != character]
        return self.map

    def set_character_location(self, room, character):
        """Set a characters location in memory"""

        try:
           self.map[room]["characters"]
        except KeyError:
           for rooms in self.map:
               self.map[rooms]["characters"] = list()
        if type(self.map[room]["characters"]) != list:
            self.map[room]["characters"] = list()
        self.remove_character_location(character)
        self.map[room]["characters"].append(character)
        self.map[room]["characters"] = list(set(self.map[room]["characters"]))
        return self.map

    def check_character_location(self, character):
        """Get a characters location from memory"""
        for room in self.map:
            if character in self.map[room]["characters"]:
                return room
        # We use this return value to check if we need to assign a room to a character.
        return "Character Not Found"

    def choose_action(self):
        """Randomly choose an action to do"""

        self.actionsDict["move"] = "move"
        return list(self.actionsDict)[random.randrange(0, len(self.actionsDict))]

    def choose_object_from_avail(self, room):
        """Randomly choose object from those available in the room"""

        available_objects = self.check_room_objects(room)
        return available_objects[random.randrange(0, len(available_objects))]

    def build_sentence(self):
        """Generate a sentence from available data"""
        # We choose what character we're going to write a sentence for.
        character_focus = self.choose_character()
        # We check if that character has a location yet, if not, give them one.
        if self.check_character_location(character_focus) == "Character Not Found":
            character_room = self.choose_room()
            self.set_character_location(character_room, character_focus)
        else:
            character_room = self.check_character_location(character_focus)
        # We check what action the character is going to take.
        character_action = self.choose_action()
        # If the character is moving, make sure they actually move.
        if character_action == "move":
            connected_rooms = self.check_room_connected(character_room)
            if len(connected_rooms) > 0:
                chosen_room = connected_rooms[random.randrange(0, len(connected_rooms))]
                self.set_character_location(chosen_room, character_focus)
                return " " + character_focus + " moved to the " + chosen_room + "."
            else:
                # If there's no connecting room, we random chance either teleporting or staying and crying.
                if random.randrange(0, 10) > 4:
                    chosen_room = self.rooms[random.randrange(0, len(self.rooms))]
                    self.set_character_location(chosen_room, character_focus)
                    return " " + character_focus + " teleported to the " + chosen_room + "."
                else:
                    return " " + character_focus + " cried because they were stuck."
        # If the character didn't move, we choose an object they will interact with.
        character_object = self.choose_object_from_avail(character_room)
        # We check if anybody else is in the room.
        character_avail = self.choose_character_from_avail(character_room, character_focus)
        # Set the noun based on whether they interact with a person or an object.
        if character_avail:
            if random.randrange(0, 10) > 4:
                available_chosen = character_avail
                noun = self.actionsDict[character_action].replace("the","")
            else:
                available_chosen = character_object
                noun = self.actionsDict[character_action] + " "
        else:
            available_chosen = character_object
            noun = self.actionsDict[character_action] + " "
        # We return a nicely built sentence.
        return " " + character_focus + " " + character_action.lower() + "ed " + noun + available_chosen + "."

    def choose_character_from_avail(self, room, character):
        """Return a random character who is also in the room."""

        characters_present = self.map[room]["characters"]
        available_list = list()
        for item in characters_present:
            if item != character:
                available_list.append(item)
        if len(available_list) > 0:
            return available_list[random.randrange(0, len(available_list))]
        else:
            return False

    def write_character_locations(self):
        """A nice paragraph intro that says where everyone is."""

        for i in self.charactersDict:
            if self.check_character_location(i) == "Character Not Found":
                character_room = self.choose_room()
                self.set_character_location(character_room, i)
        return [x + " is in the " + self.check_character_location(x) + ".\n" for x in list(self.charactersDict)]

    def build_paragraph(self):
        """Take some paragraph intros and sentence and bind them together prettily."""

        paragraphIntro = str()
        for item in self.write_character_locations():
            paragraphIntro = paragraphIntro + item
        paragraph = str()
        paragraph_build = list()
        iter = 20
        while iter > 0:
            paragraph_build.append(self.build_sentence())
            iter = iter - 1
        for character in self.charactersDict:
            list_iter = 0
            first_occur = True
            for item in paragraph_build:
                if character in item[:len(character)+1]:
                    if first_occur:
                        paragraph = paragraph + "\n\n---\n\n" + paragraph_build[list_iter][1:]
                        first_occur = False
                    else:
                        paragraph = paragraph + paragraph_build[list_iter].replace(character, self.charactersDict[character])
                list_iter = list_iter + 1
        return paragraphIntro + "\n" + paragraph[1:]

    def build_book(self):
        """Bind a bunch of paragraphs together with a rough estimate, to make a 50,000 word book"""

        bookStream = str()
        while len(bookStream) < (50000 * 8):
            self.chapters = self.chapters + 1
            bookStream = bookStream + "---\n\n## Chapter " + str(self.chapters) + ":\n\n" + self.build_paragraph() + "\n\n"
        return bookStream

    def write_book(self):
        """Write a whole 50,000 word book to file."""

        with open("outBook.md", "w+") as openFile:
            openFile.write(self.build_book())
        return "outBook.md"

if __name__ == "__main__":
    insane = CrayCrayWriter()
    insane.decide_map()
    insane.decide_room_objects()
    iter = 10
    while iter > 0:
        print(insane.build_paragraph())
        print("\n\n")
        iter = iter - 1
    insane.write_book()
