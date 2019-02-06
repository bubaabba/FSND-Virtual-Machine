from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from items_catalogModel import Category, Base, Items, User

engine = create_engine('sqlite:///catalogs.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="aisha nasir", email="eshanas001@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()
# Catalog for Armwear
category1 = Category(user_id=1, name="Armwear")

session.add(category1)
session.commit()

item1 = Items(user_id=1, name="Gloves",
              description="sports gloves", category=category1)

session.add(item1)
session.commit()

item2 = Items(user_id=1, name="Armbands",
              description="similar to a bracelet or bangle",
              category=category1)

session.add(item2)
session.commit()

item3 = Items(user_id=1, name="Glove puppetry",
              description="type of opera using cloth puppet",
              category=category1)

session.add(item3)
session.commit()

# Catalog for Dresses
category2 = Category(user_id=1, name="Dresses",)

session.add(category2)
session.commit()

item1 = Items(user_id=1, name="Gowns",
              description="wedding dresses",
              category=category2)

session.add(item1)
session.commit()

item2 = Items(user_id=1, name="Royal Dresses",
              description="Coronation Gowns",
              category=category2)

session.add(item2)
session.commit()

# Catalog for Neckwear
category3 = Category(user_id=1, name="Neckwear")

session.add(category3)
session.commit()

item1 = Items(user_id=1, name="Necklaces",
              description="pendant crosses",
              category=category3)

session.add(item1)
session.commit()

item2 = Items(user_id=1, name="Neckties",
              description="necktie knots",
              category=category3)

session.add(item2)
session.commit()

# Catalog for Headgear
category4 = Category(user_id=1, name="Headgear")

session.add(category4)
session.commit()

item1 = Items(user_id=1, name="Hats",
              description="Bonnets",
              category=category4)

session.add(item1)
session.commit()

item2 = Items(user_id=1, name="Religious Headgear",
              description="Hijab", category=category4)

session.add(item2)
session.commit()

print "Added Catalog Items"
