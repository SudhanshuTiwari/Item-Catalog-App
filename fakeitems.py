#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
DBSession = sessionmaker(bind=engine)
# Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(
    name="Sudhanshu Tiwari",
    email="sudhanshu.tiwari1590@gmail.com",
    picture='~\static\image-profile.jpg')
session.add(user1)
session.commit()

# Items for Strings
category1 = Category(name="Arts & Photography", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(
    name="The 5 Love Languages: The Secret to Love that Lasts",
    user_id=1,
    description="In the no.1 New York Times bestseller The 5 Love Languages,"
    "you will discover the secret that has transformed millions of relationships"
    "worldwide. Whether your relationship is flourishing or failing, Dr. Gary "
    "Chapmans proven approach to showing and receiving love will help you "
    "experience deeper and richer level of intimacy with your partner starting"
    "today.The 5 Love Languages is as practical as it is insightful."
    "Updated to reflect"
    "the complexities of relationships today, this new edition "
    "reveals intrinsic "
    "truths and applies relevant, actionable wisdom in ways that work.",
    category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Born a Crime: Stories from a South African Childhood",
    user_id=1,
    description="One of the comedy world's fastest rising stars"
    "tells his wild coming of age story during the twilight of"
    "apartheid in South Africa and the tumultuous days of "
    "freedom that followed. Noah provides something "
    "deeper than traditional memorists: powerfully funny"
    "observations about how farcical political and social"
    "systems play out in our lives.revor Noah is the host"
    "of the Emmy and Peabody Award winning the Daily Show.",
    category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(
    name="Essential Elements for Strings: Book 1 with EEi (Violin)",
    user_id=1,
    description="(Essential Elements for Strings). Essential"
    "Elements for Strings and Essential Elements Interactive"
    "are fully compatible with Essential Elements 2000 for"
    "Strings) Essential Elements for Strings offers beginning"
    "students sound pedagogy and engaging music, all carefully"
    "paced to successfully start young players on their musical"
    "journey. EE features both familiar songs and specially "
    "designed exercises, created and arranged for the classroom"
    "in a unison learning environment, as well as "
    "instrument specific exercises to focus each student on the"
    "unique characteristics of their own instrument.",
    category=category1)

session.add(item3)
session.commit()

# Items for Woodwinds
category2 = Category(name="Biographies & Memoirs", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(
    name="The Mamba Mentality: How I Play",
    user_id=1,
    description="Citing an obligation and an opportunity to "
    "teach young players, hardcore fans, and devoted students"
    "of the game how to play it \"the right way\", The Mamba "
    "Mentality takes us inside the mind of one of the most "
    "intelligent, analytical, and creative ",
    category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Women in Science: 50 Fearless Pioneers Who Changed the World",
    user_id=1,
    description="Full of striking, singular art, this fascinating"
    "collection also contains infographics about relevant topics "
    "such as lab equipment, rates of women currently working in "
    "STEM fields, and an illustrated scientific glossary. The "
    "trailblazing women profiled include well known figures like"
    "primatologist Jane Goodall, as well as lesser known pioneers "
    "such as Katherine Johnson, the African American physicist and"
    "mathematician who calculated the trajectory of the 1969 Apollo"
    "11 mission to the moon. Women in Science celebrates the "
    "achievements of the intrepid women who have paved the way for"
    "the next generation of female engineers, biologists, "
    "mathematicians, doctors, astronauts, physicists, and more! ",
    category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(
    name="Shade: A Tale of Two Presidents ",
    user_id=1,
    description="As Chief Official White House Photographer, Pete"
    "Souza spent more time alongside President Barack Obama than"
    "almost anyone else. His years photographing the President "
    "gave him an intimate behin the scenes view of the unique "
    "gravity of the Office of the Presidency and the tremendous"
    "responsibility that comes with it.",
    category=category2)

session.add(item3)
session.commit()

# Items for Percussion
category3 = Category(name="Business & Investing", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(
    name="Mindset: The New Psychology of Success", user_id=1,
    description="After decades of research, world renowned Stanford"
    "University psychologist Carol S. Dweck, Ph.D., discovered a "
    "simple but groundbreaking idea: the power of mindset. In this "
    "brilliant book, she shows how success in school, work, sports, "
    "the arts, and almost every area of human endeavor can be "
    "dramatically influenced by how we think about our talents and"
    "abilities. People with a fixed mindset those who believe that "
    "abilities are fixed are less likely to flourish than those with "
    "a growth mindset those who believe that abilities can be developed."
    "Mindset reveals how great parents, teachers, managers, and athletes"
    "can put this idea to use to foster outstanding accomplishment.",
    category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Rich Dad Poor Dad",
    user_id=1,
    description="Rich Dad Poor Dad is Robert's story of growing "
    "up with two dads his real father and the father of his best"
    "friend, his rich dad and the ways in which both men shaped"
    "his thoughts about money and investing. The book explodes"
    "the myth that you need to earn a high income to be rich and"
    "explains the difference between working for money and "
    "having your money work for you.",
    category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(
    name="Outliers: The Story of Success", user_id=1,
    description="In this stunning new book, Malcolm Gladwell takes"
    "us on an intellectual journey through the world of outliers"
    "the best and the brightest, the most famous and the most"
    "successful. He asks the question: what makes high achievers"
    "different?His answer is that we pay too much attention to "
    "what successful people are like, and too little attention to"
    "where they are from: that is, their culture, their family, "
    "their generation, and the idiosyncratic experiences of their"
    "upbringing. Along the way he explains the secrets of software"
    "billionaires, what it takes to be a great soccer player, why "
    "Asians are good at math, and what made the Beatles"
    "the greatest rock band.",
    category=category3)

session.add(item3)
session.commit()

item4 = CategoryItem(
    name="Thinking, Fast and Slow", user_id=1,
    description="Engaging the reader in a lively conversation"
    "about how we think, Kahneman reveals where we can and "
    "cannot trust our intuitions and how we can tap into the"
    "benefits of slow thinking. He offers practical and "
    "enlightening insights into how choices are made in both"
    "our business and our personal lives and how we can use "
    "different techniques to guard against the mental glitches"
    "that often get us into trouble. Winner of the National "
    "Academy of Sciences Best Book Award and the Los Angeles"
    "Times Book Prize and selected by The New York Times Book"
    "Review as one of the ten best books of 2011, Thinking,"
    "Fast and Slow is destined to be a classic.",
    category=category3)

session.add(item4)
session.commit()

# Items for Brass
category4 = Category(name="Literature & Fiction", user_id=1)

session.add(category4)
session.commit()


item1 = CategoryItem(
    name="The Alchemist",
    user_id=1,
    description="Paulo Coelho's masterpiece tells the mystical "
    "story of Santiago, an Andalusian shepherd boy who yearns to"
    "travel in search of a worldly treasure. His quest will lead"
    "him to riches far different and far more satisfying than he"
    "ever imagined. Santiago's journey teaches us about the "
    "essential wisdom of listening to our hearts, of recognizing"
    "opportunity and learning to read the omens strewn along life's"
    "path, and, most importantly, to follow our dreams.",
    category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="To Kill a Mockingbird", user_id=1,
    description="One of the best loved stories of all time, To"
    "Kill a Mockingbird has been translated into more than "
    "forty languages, sold more than forty million copies "
    "worldwide, served as the basis for an enormously popular"
    "motion picture, and was voted one of the best novels of "
    "the twentieth century by librarians across the country."
    "A gripping, heart wrenching, and wholly remarkable tale of"
    "coming of age in a South poisoned by virulent prejudice, it"
    "views a world of great beauty and savage inequities through"
    "the eyes of a young girl, as her father a crusading local"
    "lawyer risks everything to defend a black man unjustly "
    "accused of a terrible crime.",
    category=category3)

session.add(item2)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
