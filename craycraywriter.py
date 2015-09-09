from __future__ import print_function
from __future__ import unicode_literals

import random

class CrayCrayWriter(object):
    """An object that can generate stories!"""

    def __init__(self):
        """Init all the data we need"""

        self.characters = ["Kate","Andrew","Micah", "Elizabeth"]
        # Actions should be a dict pair, of action and noun.
        # There should be two sets of actions: Objects and Characters
        self.actions = ["Punch","Kick","Yell","Ignor","Us", "Observ", "Star", "Patt", "Cuddl", "Kiss", "Talk", "Fart", "Laugh", "Hat", "Lov"]
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
                         "Lov":"the"
                       }
        self.objects = ["Couch","Chair","TV","Computer","Cat","Dog"]
        self.rooms = ["Bedroom","Library","Bathroom","Kitchen","Lounge","Playroom","Backyard"]
        self.map = dict()

    def choose_character(self):
        """Randomly return one of the available characters"""

        return self.characters[random.randrange(0, len(self.characters))]

    def choose_action(self):
        """Randomly return one of the possible actions"""

        return self.actions[random.randrange(0, len(self.actions))]

    def choose_object(self):
        """Randomly return one of the possible objects"""

        return self.objects[random.randrange(0, len(self.objects))]

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
        return "Character Not Found"

    def choose_action(self):
        """Randomly choose an action to do"""

        self.actions.append("move")
        self.actions = list(set(self.actions))
        return self.actions[random.randrange(0, len(self.actions))]

    def choose_object_from_avail(self, room):
        """Randomly choose object from those available in the room"""

        available_objects = self.check_room_objects(room)
        return available_objects[random.randrange(0, len(available_objects))]

    def build_sentence(self):
        """Generate a sentence from available data"""
        character_focus = self.choose_character()
        if self.check_character_location(character_focus) == "Character Not Found":
            character_room = self.choose_room()
            self.set_character_location(character_room, character_focus)
        else:
            character_room = self.check_character_location(character_focus)
        # Actions need to happen after object is chosen, so that only appropriate actions are available.
        character_action = self.choose_action()
        if character_action == "move":
            connected_rooms = self.check_room_connected(character_room)
            if len(connected_rooms) > 0:
                chosen_room = connected_rooms[random.randrange(0, len(connected_rooms))]
                self.set_character_location(chosen_room, character_focus)
                return " " + character_focus + " moved to the " + chosen_room + "."
            else:
                if random.randrange(0, 10) > 4:
                    chosen_room = self.rooms[random.randrange(0, len(self.rooms))]
                    self.set_character_location(chosen_room, character_focus)
                    return " " + character_focus + " teleported to the " + chosen_room + "."
                else:
                    return " " + character_focus + " cried because stuck."
        character_object = self.choose_object_from_avail(character_room)
        character_avail = self.choose_character_from_avail(character_room, character_focus)
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
        return " " + character_focus + " " + character_action.lower() + "ed " + noun + available_chosen + "."

    def choose_character_from_avail(self, room, character):
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
        for i in self.characters:
            if self.check_character_location(i) == "Character Not Found":
                character_room = self.choose_room()
                self.set_character_location(character_room, i)
        return [x + " is in the " + self.check_character_location(x) + ".\n" for x in self.characters]

    def build_paragraph(self):
        paragraphIntro = str()
        for item in self.write_character_locations():
            paragraphIntro = paragraphIntro + item
        paragraph = str()
        paragraph_build = list()
        iter = 20
        while iter > 0:
            paragraph_build.append(self.build_sentence())
            iter = iter - 1
        # For loop per character, per item, examining the first word.
        for character in self.characters:
            list_iter = 0
            for item in paragraph_build:
                if character in paragraph_build[list_iter]:
                    paragraph = paragraph + paragraph_build[list_iter]
                list_iter = list_iter + 1
        return paragraphIntro + paragraph[1:]

    def build_book(self):
        bookStream = str()
        while len(bookStream) < (50000 * 8):
            bookStream = bookStream + self.build_paragraph() + "\n\n"
        return bookStream

    def write_book(self):
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
