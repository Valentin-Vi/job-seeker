class Job:
    def __init__(self, title, location, type, date, href_details, details):
        self.title = title
        self.location = location
        self.type = type
        self.date = date
        self.href_details = href_details
        self.details = details

    def as_dict(self):
        return {
            "title": self.title,
            "location": self.location,
            "type": self.type,
            "date": self.date,
            "href_details": self.href_details,
            "details": self.details
        }

    def __str__(self):
        return f"Title: {self.title}, Location: {self.location}, Type: {self.type}, Date: {self.date}, Href: {self.href_details}, Details: {self.details}"
