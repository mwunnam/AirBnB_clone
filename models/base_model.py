#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
<<<<<<< HEAD
    """Class base that defines all commons attributes and methods for other classes."""
    
    def __init__(self, *args, **kwargs):
        """
            Initialize all attributes of the instance.

            Attributes:
                id: a string wich get its value from uuid.uuid4() module.

                created_at: Timestamp indication when a class instance was created.
                updated_at: Timestamp indicating when a class instance was updated.
                All these attributes are public attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        slef.updated_at = datetime.now()

    def __str__(self):
        """
            This prints the class info in this format:
            [<class_name>] (<self.id>) <self.__dict__>
=======
    """
    This is the base class and contains all the common attributes and
    methods all other classes will inherited
    """

    def __init__(self):
        """
        This initializes a new instances of the BaseModel class.

        Attributes:
            id : a string which get it value from uuid.uuid4() module

            created_at: Timestamp indication when a class instance was created
            updated_at: Timestamp indicating when a class instance was up dated
            All these arttributes are public attribbutes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        This prints the class info in this format:
            [<class name>] (<self.id>) <self.__dict__>
>>>>>>> ea067676bad02ab17b79b4fdb8d8bed01f28776f
        """
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
<<<<<<< HEAD
            This updates the public instance attribute updated_at with
            current datetime.
=======
        This updates the public instance attribute updated_at with
        current datetime
>>>>>>> ea067676bad02ab17b79b4fdb8d8bed01f28776f
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
<<<<<<< HEAD
            This is a method that get data from __dict__ makes a copy of it
            then manipulate the date and time values from the created_at and
            updated_at values into the iso format.
        
            Returns: The updated dictionary.
=======
        This is a method that get data from __dict__ makes a copy of it
        the maniputated the date and time values from the created_at and
        updated_at values into the isoformat

        Returns: the updated dictionary
>>>>>>> ea067676bad02ab17b79b4fdb8d8bed01f28776f
        """
        data_dict = self.__dict__.copy()
        data_dict['__class__'] = self.__class__.__name__
        data_dict['created_at'] = self.created_at.isoformat()
<<<<<<< HEAD
        data_dict['updated_at'] = self.created_at.isoformat()
=======
        data_dict['updated_at'] = self.updated_at.isoformat()
>>>>>>> ea067676bad02ab17b79b4fdb8d8bed01f28776f
        return data_dict
