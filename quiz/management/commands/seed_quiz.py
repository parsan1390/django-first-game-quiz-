from django.core.management.base import BaseCommand
from quiz.models import Category, Quiz, Question, Choice


class Command(BaseCommand):
    help = 'Seeds gaming trivia categories and quizzes (15 questions each)'

    def handle(self, *args, **options):
        Category.objects.all().delete()

        data = {
            'Action & Adventure': {
                'icon': '⚔️',
                'quiz_title': 'World of Action Games',
                'questions': [
                    ('Who is the main character of God of War?', ['Kratos', 'Master Chief', 'Dante', 'Geralt'], 0),
                    ('Elden Ring was developed by which studio?', ['FromSoftware', 'Rockstar', 'Ubisoft', 'Naughty Dog'], 0),
                    ('How many playable main characters does GTA V have?', ['2', '3', '4', '1'], 1),
                    ('Which decade does Red Dead Redemption 2 mostly take place in?', ['1900s', '1950s', '1800s', '2000s'], 0),
                    ('Who is the main character in Uncharted?', ['Nathan Drake', 'Kratos', 'Marcus Fenix', 'Sam Fisher'], 0),
                    ('Sekiro was developed by which company?', ['FromSoftware', 'Capcom', 'Konami', 'Square Enix'], 0),
                    ('In Assassins Creed, the rival organization is called?', ['The Templars', 'The Guardians', 'The Knights', 'The Mafia'], 0),
                    ('Devil May Cry is famous for which genre?', ['Hack and slash', 'Strategy', 'Simulation', 'Puzzle'], 0),
                    ('Who is the main character of Metal Gear Solid?', ['Snake', 'Kratos', 'Doomguy', 'Lara'], 0),
                    ('Doom belongs to which genre?', ['First-person shooter', 'Strategy', 'Racing', 'Sports'], 0),
                    ('Which studio developed Horizon Zero Dawn?', ['Guerrilla Games', 'Naughty Dog', 'Insomniac', 'Sucker Punch'], 0),
                    ('In Ghost of Tsushima, the main character is from?', ['Tsushima', 'Kyoto', 'Okinawa', 'Tokyo'], 0),
                    ('Bloodborne belongs to which genre?', ['Souls-like action RPG', 'Sports', 'Strategy', 'Puzzle'], 0),
                    ('Which company made the original Tomb Raider?', ['Core Design', 'Konami', 'Sega', 'Capcom'], 0),
                    ('Sifu is centered around which martial art?', ['Kung Fu', 'Karate', 'Judo', 'Boxing'], 0),
                ],
            },
            'Strategy': {
                'icon': '🧠',
                'quiz_title': 'Classic Strategy Games',
                'questions': [
                    ('Age of Empires belongs to which genre?', ['Real-time strategy', 'RPG', 'Action', 'Sports'], 0),
                    ('Blizzards most iconic strategy game is?', ['StarCraft', 'Diablo', 'Overwatch', 'Hearthstone'], 0),
                    ('Civilization is mainly about?', ['Building a civilization through history', 'Space warfare', 'Racing', 'Sports'], 0),
                    ('How many pieces does each side start with in chess?', ['16', '12', '20', '8'], 0),
                    ('XCOM is best known for which genre?', ['Turn-based strategy', 'Online action', 'Sports', 'Adventure'], 0),
                    ('Which studio developed Total War?', ['Creative Assembly', 'Blizzard', 'Paradox', 'Firaxis'], 0),
                    ('Which decade was Command & Conquer released in?', ['1990s', '2000s', '2010s', '1980s'], 0),
                    ('In StarCraft, which race is insect-like?', ['Zerg', 'Terran', 'Protoss', 'Covenant'], 0),
                    ('Plants vs Zombies belongs to which genre?', ['Tower defense', 'Shooter', 'Sports', 'Racing'], 0),
                    ('Clash of Clans was originally released on?', ['Mobile', 'Console', 'PC', 'Arcade'], 0),
                    ('Company of Heroes is set during?', ['World War II', 'Cold War', 'The future', 'Medieval times'], 0),
                    ('Warcraft III was the prelude to which famous game?', ['World of Warcraft', 'Diablo', 'Overwatch', 'Hearthstone'], 0),
                    ('The main goal in Risk is to?', ['Conquer every continent', 'Build a city', 'Farm resources', 'Trade goods'], 0),
                    ('Cities: Skylines is about?', ['City-building simulation', 'Warfare', 'Sports', 'Adventure'], 0),
                    ('Frostpunk is set in which environment?', ['A frozen post-apocalyptic world', 'A desert', 'A jungle', 'Outer space'], 0),
                ],
            },
            'Role-Playing (RPG)': {
                'icon': '🗡️',
                'quiz_title': 'The World of RPGs',
                'questions': [
                    ('The Witcher 3 is based on novels by?', ['Andrzej Sapkowski', 'J.R.R. Tolkien', 'Marvel Comics', 'None of the above'], 0),
                    ('In Skyrim, the main character is known as the?', ['Dragonborn', 'Knight', 'Hero', 'Wizard'], 0),
                    ('What year was Final Fantasy VII released?', ['1997', '2000', '1990', '2005'], 0),
                    ('Which studio developed Mass Effect?', ['BioWare', 'Bethesda', 'CD Projekt', 'Square Enix'], 0),
                    ('Dark Souls is famous for being?', ['Extremely difficult and challenging', 'Very easy', 'Average difficulty', 'No challenge at all'], 0),
                    ('Baldurs Gate 3 uses which combat system?', ['Turn-based based on Dungeons & Dragons', 'Real-time', 'Card-based', 'Sports-style'], 0),
                    ('Persona 5 belongs to which genre?', ['Japanese role-playing game (JRPG)', 'Shooter', 'Strategy', 'Sports'], 0),
                    ('Which company created Diablo?', ['Blizzard', 'BioWare', 'Bethesda', 'CD Projekt'], 0),
                    ('In Elden Ring, the game world is called?', ['The Lands Between', 'Middle-earth', 'Skyrim', 'Hyrule'], 0),
                    ('Fallout is mostly set in a?', ['Nuclear post-apocalyptic world', 'Space colony', 'Medieval kingdom', 'Ordinary modern city'], 0),
                    ('The most common RPG class trio is?', ['Warrior, mage, rogue', 'Runner, swimmer', 'Singer, painter', 'Driver, pilot'], 0),
                    ('Cyberpunk 2077 was developed by?', ['CD Projekt Red', 'Rockstar', 'Bethesda', 'BioWare'], 0),
                    ('In Genshin Impact, what is the core game mechanic?', ['Seven natural elements', 'Only fire', 'Only water', 'None'], 0),
                    ('Dragon Age was developed by which studio?', ['BioWare', 'Bethesda', 'CD Projekt', 'Obsidian'], 0),
                    ('The main goal in Pokemon is to?', ['Collect and train Pokemon', 'Build a city', 'Race cars', 'Cook meals'], 0),
                ],
            },
            'General Gaming': {
                'icon': '🎮',
                'quiz_title': 'General Gaming Trivia',
                'questions': [
                    ('What was Sonys first game console called?', ['PlayStation', 'Xbox', 'Nintendo 64', 'Sega Genesis'], 0),
                    ('What is the most popular battle royale game?', ['Fortnite', 'Tetris', 'Chess.com', 'Solitaire'], 0),
                    ('Which company created Minecraft?', ['Mojang', 'EA', 'Ubisoft', 'Valve'], 0),
                    ('What is usually considered the first video game in history?', ['Pong', 'Mario', 'Tetris', 'Pac-Man'], 0),
                    ('Which company makes the Xbox console?', ['Microsoft', 'Sony', 'Nintendo', 'Apple'], 0),
                    ('Pac-Man was first released in which decade?', ['1980s', '1990s', '2000s', '1970s'], 0),
                    ('The Steam platform belongs to which company?', ['Valve', 'EA', 'Epic Games', 'Ubisoft'], 0),
                    ('What is the most popular MOBA game?', ['League of Legends', 'Tetris', 'Pac-Man', 'Solitaire'], 0),
                    ('Mario first appeared in which game?', ['Donkey Kong', 'Super Mario Bros', 'Mario Kart', 'Zelda'], 0),
                    ('Among Us is mostly about?', ['Social deduction and finding the impostor', 'Action combat', 'Sports', 'War strategy'], 0),
                    ('Which company makes the Nintendo Switch?', ['Nintendo', 'Sony', 'Microsoft', 'Sega'], 0),
                    ('What does Roblox allow users to do?', ['Create their own games', 'Only watch movies', 'Only chat', 'Only shop online'], 0),
                    ('The Epic Games Store competes with which platform?', ['Steam', 'PlayStation Store', 'Xbox Live', 'App Store'], 0),
                    ('What is the most popular building and survival game?', ['Minecraft', 'Fortnite', 'FIFA', 'Chess'], 0),
                    ('What year was the first Call of Duty released?', ['2003', '1995', '2010', '2000'], 0),
                ],
            },
        }

        for cat_name, cat_data in data.items():
            category = Category.objects.create(
                name=cat_name,
                slug=cat_name.lower().replace(' ', '-').replace('&', 'and').replace('(', '').replace(')', ''),
                icon=cat_data['icon'],
            )
            quiz = Quiz.objects.create(
                title=cat_data['quiz_title'],
                category=category,
                time_limit=10,
            )
            for order, (q_text, choices, correct_index) in enumerate(cat_data['questions']):
                question = Question.objects.create(quiz=quiz, text=q_text, order=order)
                for i, choice_text in enumerate(choices):
                    Choice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=(i == correct_index),
                    )

        self.stdout.write(self.style.SUCCESS('✅ Sample data (15 questions per quiz) seeded successfully.'))