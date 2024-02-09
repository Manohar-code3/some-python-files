import signal
import sys#it provieds function and varabiles which used to manipulate  diffrent parts of  python runtime environment
def keyboard_interrupt_handler(signal, frame):
    print("\nKeyboard interrupt received. Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, keyboard_interrupt_handler)

def main():
    try:
        while True:
            user_input = input("Enter a command: ")

            if user_input.lower() == 'exit':
                break  
            elif user_input.lower() == 'greet':
                print("Hello! How are you?")
            elif user_input.lower() == 'time':
                import datetime
                current_time = datetime.datetime.now()
                print(f"The current time is: {current_time}")
            else:
                print("Invalid command. Please try again.")

    except KeyboardInterrupt:
        keyboard_interrupt_handler(signal.SIGINT, None)


if __name__ == "__main__":
    main()