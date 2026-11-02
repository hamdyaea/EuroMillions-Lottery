#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""EuroMillions random ticket picker, for entertainment."""
import argparse
import random

def draw(rng=None) -> tuple[list[int], list[int]]:
    rng = rng if rng is not None else random.SystemRandom()
    return sorted(rng.sample(range(1, 51), 5)), sorted(rng.sample(range(1, 13), 2))

def format_ticket(numbers: list[int], stars: list[int]) -> str:
    return f"Numbers: {', '.join(map(str, numbers))}\nStars: {', '.join(map(str, stars))}"

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", action="store_true", help="Print one ticket in terminal")
    args = parser.parse_args()
    if args.text:
        print(format_ticket(*draw()))
        return
    import tkinter as tk
    from tkinter import ttk
    root = tk.Tk()
    root.title("EuroMillions Lottery")
    root.geometry("380x175")
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)
    result = tk.StringVar(value="Generate a ticket to begin")
    ttk.Label(frame, textvariable=result, justify="center").pack(pady=10)
    def new_ticket() -> None:
        result.set(format_ticket(*draw()))
    ttk.Button(frame, text="Generate / Replay", command=new_ticket).pack(pady=8)
    ttk.Label(frame, text="For entertainment; no prediction of winning numbers.").pack()
    root.mainloop()

if __name__ == "__main__":
    main()
