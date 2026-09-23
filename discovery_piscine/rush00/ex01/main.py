#!/usr/bin/env python3
import sys
from checkmate import checkmate, is_in_check
from chessgame import play_standard_chess

def print_help():
    print("Usage: python3 main.py [mode] [files...]")
    print("Modes:")
    print("  <file1.chess> ...  : Check if King is in check from given files.")
    print("  --best-move <file> : Find the best move for King to escape check.")
    print("  --play             : Start a standard 8x8 text chess game.")

def find_best_move(board_str):
    result = is_in_check(board_str)
    if result is None:
        print("Error")
        return
    if result is False:
        print("King is not in check.")
        return

    lines = [list(line) for line in board_str.strip().splitlines()]
    rows = len(lines)
    cols = len(lines[0])

    kr, kc = None, None
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == 'K':
                kr, kc = r, c
                break

    move_dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    safe_moves = []

    for dr, dc in move_dirs:
        nr, nc = kr + dr, kc + dc
        if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '.':
            lines[kr][kc] = '.'
            lines[nr][nc] = 'K'

            test_board = "\n".join(["".join(row) for row in lines])
            if not is_in_check(test_board):
                safe_moves.append(f"Move King to row {nr}, col {nc}")

            lines[nr][nc] = '.'
            lines[kr][kc] = 'K'

    if safe_moves:
        print("Best moves to escape check:")
        for move in safe_moves:
            print("- " + move)
    else:
        print("Checkmate! No safe moves.")

def main():
    if len(sys.argv) < 2:
        print("Error")
        print_help()
        return

    arg1 = sys.argv[1]

    if arg1 == "--help":
        print_help()
        return

    # เปิดโหมดเล่นเกมหมากรุกมาตรฐาน
    if arg1 == "--play":
        play_standard_chess()
        return

    # โหมดหาตาเดินแก้รุก
    if arg1 == "--best-move":
        if len(sys.argv) < 3:
            print("Error")
            return
        try:
            with open(sys.argv[2], 'r', encoding='utf-8') as f:
                find_best_move(f.read())
        except Exception:
            print("Error")
        return

    # โหมดอ่านไฟล์บอร์ดปกติ (Default)
    for filepath in sys.argv[1:]:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.strip():
                    print("Error")
                    continue
                checkmate(content)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()
