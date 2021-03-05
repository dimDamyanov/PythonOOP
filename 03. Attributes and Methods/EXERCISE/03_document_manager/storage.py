from .category import Category
from .topic import Topic
from .document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for i in range(len(self.categories)):
            if self.categories[i].id == category_id:
                self.categories[i].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for i in range(len(self.topics)):
            if self.topics[i].id == topic_id:
                self.topics[i].topic = new_topic
                self.topics[i].storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for i in range(len(self.documents)):
            if self.documents[i].id == document_id:
                self.documents[i].file_name = new_file_name

    def delete_category(self, category_id: int):
        for i in range(len(self.categories)):
            if self.categories[i].id == category_id:
                self.categories.remove(self.categories[i])

    def delete_topic(self, topic_id: int):
        for i in range(len(self.topics)):
            if self.topics[i].id == topic_id:
                self.topics.remove(self.topics[i])

    def delete_document(self, document_id: int):
        for i in range(len(self.documents)):
            if self.documents[i].id == document_id:
                self.documents.remove(self.documents[i])

    def get_document(self, document_id: int):
        for i in range(len(self.documents)):
            if self.documents[i].id == document_id:
                return self.documents[i]

    def __repr__(self):
        return '\n'.join([repr(document) for document in self.documents])
