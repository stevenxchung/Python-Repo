from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle_request(self, doc) -> None:
        pass


class Document:
    def __init__(self):
        self.state = Draft()
        self.approved = False

    def get_state(self) -> State:
        print(f'get_state(): {type(self.state).__name__}')
        return self.state

    def set_state(self, state: State) -> None:
        self.state = state

    def publish(self) -> None:
        self.state.handle_request(self)

    def set_approval(self, approved: bool) -> None:
        self.approved = approved

    def is_approved(self) -> bool:
        return self.approved


class Draft(State):
    def handle_request(self, doc: Document) -> None:
        doc.set_state(Review())


class Review(State):
    def handle_request(self, doc: Document) -> None:
        if doc.is_approved():
            doc.set_state(Published())
        else:
            doc.set_state(Draft())


class Published(State):
    def handle_request(self, doc: Document) -> None:
        doc.set_state(self)


if __name__ == '__main__':
    document = Document()
    isinstance(document.get_state(), Draft)  # True

    document.publish()
    isinstance(document.get_state(), Review)  # True

    document.publish()
    isinstance(document.get_state(), Draft)  # True

    document.set_approval(True)
    document.publish()  # Draft -> Review
    document.publish()  # Review -> Published
    isinstance(document.get_state(), Published)  # True

    document.publish()
    isinstance(document.get_state(), Published)  # True
