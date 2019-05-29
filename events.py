#!/usr/bin/env python3
class InputComponent:
    def __init__(self):
        """
        Constructor in Python is always called `__init__`
        You should initialize all object-level variables in the constructor
        """
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def emit_event_value_changed(self, new_value):
        for observer in self._observers:
            observer.on_value_changed_handler(new_value)

    def user_enters_value(self, value):
        # we don't even store the value in this object.
        # Just an arbitrary choice
        print('InputComponent: User enters value. Value: {}'.format(value))
        self.emit_event_value_changed(value)


class LabelComponent:
    def __init__(self):
        self.displayed_value = None

    def set_displayed_value(self, value):
        self.displayed_value = value
        print("LabelComponent: setting displayed value as: {}"
              .format(self.displayed_value))

    def on_value_changed_handler(self, new_value):
        print('LabelComponent reacts to new value. new_value: {}'
              .format(new_value))
        self.set_displayed_value(new_value)


class DataStore:
    """
    Data store has only one value for now, `username`
    """

    def __init__(self):
        self.username = None
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def emit_event_value_changed(self, new_value):
        for observer in self._observers:
            observer.on_value_changed_handler(new_value)

    def on_value_changed_handler(self, new_value):
        print('DataStore reacts to new value. new_value: {}'.format(new_value))
        self.set_username(new_value)

    def set_username(self, value):
        self.username = value
        self.emit_event_value_changed(value)

    def get_username(self):
        return self.username


def main():
    # put the stuff together
    input_component = InputComponent()
    label_component = LabelComponent()
    data_store = DataStore()
    input_component.register_observer(data_store)
    data_store.register_observer(label_component)

    user_input = "biedak"
    while user_input != "q":
        input_component.user_enters_value(user_input)
        user_input = input("\nEnter new username. (or `q` to quit) > ")


# this is so running this file executes the code
if __name__ == '__main__':
    main()

"""
future steps:
- more dynamic data store
- more dynamic bindings of components to the data store
- generic `Component` class + inheritance 
- Observer and Observable classes
- more `official` event system, maybe a mini library in a separate file 
- threads
"""
