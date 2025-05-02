#! usr/bin/env/python3

"""Main Runner file."""
import primary_ui as pu

def main():
    primary_window = pu.MainView()
    primary_window.window.mainloop()

if __name__ == "__main__":
    main()
