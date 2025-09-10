class DomainException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class UserNotFoundException(DomainException):
    pass

class CourseNotFoundException(DomainException):
    pass

class TodoNotFoundException(DomainException):
    pass