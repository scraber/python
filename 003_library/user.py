class User:

    def __init__(self, uid: int, firstname: str, lastname: str):
        self.uid = uid
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self, view: str = "user"):
        if "user" == view:
            return f"{self.firstname} {self.lastname}"
        elif "admin" == view:
            return f"{self.uid}: {self.firstname} {self.lastname}"

    def to_json(self):
        return {"firstname": self.firstname, "lastname": self.lastname}
