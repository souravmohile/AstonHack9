import pyglet
import random

# Location of music file
music = pyglet.media.load('/Users/souravmohile/Codingwoding/PycharmProjects/pyglet_audio_testing/GooseTrack.wav')

# TODO: START SCREEN
# Makes the main window
window = pyglet.window.Window(width=800, height=500, caption="NoteNinja")

# Set the clear color to white
white_background = pyglet.image.SolidColorImagePattern((255, 255, 255, 255)).create_image(window.width, window.height)

# Creates Start button
button_image = pyglet.image.load('/Users/souravmohile/Codingwoding/PycharmProjects/Goosies/images/start/start_button.jpeg')
button_sprite = pyglet.sprite.Sprite(button_image, x=225, y=80)
button_sprite.scale = 0.4

# Creates the goose image on the start page
start_goose_image = pyglet.image.load('/Users/souravmohile/Codingwoding/PycharmProjects/Goosies/images/start/start_goose.jpeg')
start_goose_sprite = pyglet.sprite.Sprite(start_goose_image, x=(window.width - start_goose_image.width) + 113 // 2, y=(window.height - start_goose_image.height) // 2 + 250)
start_goose_sprite.scale = 0.4

current_page = "start"

# TODO: MAIN SCREEN
# Sets the Score label
score = 0
label = pyglet.text.Label(
    f'Score: {score}',
    font_name='Arial',
    font_size=16,
    x=10,
    y=window.height - 5,
    anchor_x='left',
    anchor_y='top'
)

# Starts the main game background animation
background_animation = pyglet.image.load_animation('/Users/souravmohile/Codingwoding/PycharmProjects/Goosies/images/background/background_main.gif')
bg_sprite = pyglet.sprite.Sprite(background_animation, x=13, y=15)
bg_sprite.scale = 1.15

# Gets our main game goosie running
goose_animation = pyglet.image.load_animation('/Users/souravmohile/Codingwoding/PycharmProjects/Goosies/images/goose/gooseie2.gif')
goose_sprite = pyglet.sprite.Sprite(goose_animation, x=30, y=65)
goose_sprite.scale = 1

# Shows the obstacle
star_animation = pyglet.image.load_animation('/Users/souravmohile/Codingwoding/PycharmProjects/Goosies/images/Obstacle/star.gif')
star_sprite = pyglet.sprite.Sprite(star_animation, x=580, y=120)
star_sprite.scale = 1

# Create a label for the random letter
letter_label = pyglet.text.Label(
    '',
    font_name='Arial',
    font_size=24,
    x=star_sprite.x + star_sprite.width // 2,
    y=star_sprite.y + star_sprite.height + 10,
    anchor_x='center',
    anchor_y='bottom'
)

# Makes the quit button
quit_image = pyglet.image.load('/Users/souravmohile/Codingwoding/PycharmProjects/Goosies/images/start/cross.png')
quit_sprite = pyglet.sprite.Sprite(quit_image, x=730, y=410)
quit_sprite.scale = 0.02

# makes the music player
player = pyglet.media.Player()
player.queue(music)

# Example: Variable to store the target letter
target_letter = ''

# Example: Function to generate a new random letter
def generate_target_letter():
    global target_letter
    target_letter = random.choice('ABCDEFG')
    letter_label.text = target_letter

# Schedule a new random letter every second
pyglet.clock.schedule_interval(lambda dt: generate_target_letter(), 1.3)

@window.event
def on_key_press(symbol, modifiers):
    global score, target_letter
    if current_page == "main":
        # Check if the pressed key matches the target letter
        pressed_char = chr(symbol)
        if pressed_char.isalpha() and pressed_char.upper() == target_letter:
            score += 1
            label.text = f'Score: {score}'

@window.event
def on_draw():
    if current_page == "start":
        white_background.blit(0, 0)
        button_sprite.draw()
        start_goose_sprite.draw()
    elif current_page == "main":
        window.clear()
        bg_sprite.draw()
        goose_sprite.draw()
        star_sprite.draw()
        quit_sprite.draw()
        label.draw()  # Draw the score label
        letter_label.draw()  # Draw the random letter label
        player.play()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global current_page, score
    if current_page == "start":
        if (
            button_sprite.x < x < button_sprite.x + button_sprite.width
            and button_sprite.y < y < button_sprite.y + button_sprite.height
        ):
            current_page = "main"
    elif current_page == "main":
        if (
            quit_sprite.x < x < quit_sprite.x + quit_sprite.width
            and quit_sprite.y < y < quit_sprite.y + quit_sprite.height
        ):
            # Stop the music
            player.pause()

            # Reset player to start
            player.seek(0.0)

            # Reset the score
            score = 0
            label.text = f'Score: {score}'

            # Set current_page back to "start"
            current_page = "start"

# Run app
pyglet.app.run()
