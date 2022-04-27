class Database:
    def __init__(self):
        self.dbs = {
            "foods": Foods(),
            "entertainment": Entertainment(),
            "medical_products": MedicalProducts(),
            "chemicals": Chemicals()
        }

    def get_item_info(self, label):
        dbs = self.dbs.keys()
        for db in dbs:
            for entry in self.dbs[db].list:
                if entry["label"] in label or label in entry["label"]:
                    item = entry
                    item["type"] = db
                    return item
        return None

class Foods():
    def __init__(self):
        self.list = [
            {
                "label": "chocolate",
                "category": "sweet"
            }
        ]


class Entertainment():
    def __init__(self):
        self.list = [
            {
                "label": "CD",
                "category": "media"
            },
            {
                "label": "book",
                "category": "books"
            }
        ]


class MedicalProducts():
    def __init__(self):
        self.list = [
            {
                "label": "pills",
                "category": "drug"
            }
        ]


class Chemicals():
    def __init__(self):
        self.list = [
            {
                "label": "perfume",
                "category": "personal_care"
            }
        ]
