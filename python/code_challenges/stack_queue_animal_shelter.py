from collections import deque


class AnimalShelter:
    def __init__(self, stretch=False):
        self.dogs = Queue()
        self.cats = Queue()

        self.stretch = stretch

        if stretch:
            self.animals = Queue()  # stretch

    def enqueue(self, animal):

        if self.stretch:
            self.animals.enqueue(animal)  # stretch

        if isinstance(animal, Cat):
            self.cats.enqueue(animal)
        else:
            self.dogs.enqueue(animal)

    def dequeue(self, pref=""):

        if pref == "cat":
            return self.cats.dequeue()
        elif pref == "dog":
            return self.dogs.dequeue()
        elif self.stretch:
            # stretch
            animal = self.animals.dequeue()
            if isinstance(animal, Cat):
                self.cats.dequeue()
            else:
                self.dogs.dequeue()

            return animal
        else:
            return None


class Dog:
    def __repr__(self):
        return


class Cat:
    def __repr__(self):
        return


class Queue(deque):

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        return self.popleft()
