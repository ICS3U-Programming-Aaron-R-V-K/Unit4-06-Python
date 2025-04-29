# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: April 28, 2025
# This program all RGB colors from 0 to 255, increasing by 15
# It uses three nested loops one for each color


def main():

    # Red start from 0 until 255, by 15
    for red in range(0, 256, 15):

        # Green start from 0 until 255, by 15
        for green in range(0, 256, 15):

            # Blue start from 0 until 255 by 15
            for blue in range(0, 256, 15):
                # Display each output each time inside the loop
                print(f"{red};{green};{blue}")


if __name__ == "__main__":
    main()
