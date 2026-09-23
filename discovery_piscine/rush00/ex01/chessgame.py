import sys

def init_board():
    """ สร้างกระดานหมากรุกมาตรฐาน 8x8 """
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

def print_board(board):
    """ แสดงผลกระดานพร้อมตัวเลขกำกับพิกัดแถวและคอลัมน์ """
    print("\n    0 1 2 3 4 5 6 7")
    print("   -----------------")
    for r in range(8):
        row_str = " ".join(board[r])
        print(f"{r} | {row_str} |")
    print("   -----------------")

def is_white(piece):
    return piece.isupper() and piece != '.'

def is_black(piece):
    return piece.islower() and piece != '.'

def is_valid_move(board, sr, sc, tr, tc, turn):
    """ ตรวจสอบความถูกต้องเบื้องต้นของการเดิน """
    if not (0 <= sr < 8 and 0 <= sc < 8 and 0 <= tr < 8 and 0 <= tc < 8):
        return False, "พิกัดอยู่นอกกระดาน"

    piece = board[sr][sc]
    if piece == '.':
        return False, "ไม่มีตัวหมากในตำแหน่งเริ่มต้นที่เลือก"

    if turn == 'W' and not is_white(piece):
        return False, "ตาของฝ่ายขาว (White) กรุณาเลือกตัวหมากพิมพ์ใหญ่"
    if turn == 'B' and not is_black(piece):
        return False, "ตาของฝ่ายดำ (Black) กรุณาเลือกตัวหมากพิมพ์เล็ก"

    target = board[tr][tc]
    if target != '.':
        if turn == 'W' and is_white(target):
            return False, "ไม่สามารถกินตัวหพวกเดียวกันเองได้"
        if turn == 'B' and is_black(target):
            return False, "ไม่สามารถกินตัวหพวกเดียวกันเองได้"

    return True, ""

def play_standard_chess():
    """ ฟังก์ชันรันเกมหมากรุกมาตรฐาน """
    board = init_board()
    turn = 'W' # 'W' เริ่มก่อน, ตามด้วย 'B'

    print("========================================")
    print("      STANDARD TEXT CHESS GAME          ")
    print("========================================")
    print("วิธีเล่น: ใส่พิกัด [แถวเริ่มต้น] [คอลัมน์เริ่มต้น] [แถวปลายทาง] [คอลัมน์ปลายทาง]")
    print("ตัวอย่างเช่น: 6 4 4 4 (เดินเบี้ยขาวจากแถว 6 ไปแถว 4)")
    print("พิมพ์ 'quit' เพื่อออกจากเกม\n")

    while True:
        print_board(board)
        current_player_name = "White (Uppercase)" if turn == 'W' else "Black (Lowercase)"
        print(f"\n[ ตาของฝ่าย: {current_player_name} ]")

        user_input = input("ระบุตาเดิน (เช่น 6 4 4 4): ").strip()
        if user_input.lower() == 'quit':
            print("จบเกม ออกจากโปรแกรม...")
            break

        parts = user_input.split()
        if len(parts) != 4:
            print("❌ รูปแบบไม่ถูกต้อง! กรุณาใส่ตัวเลข 4 ตัวคั่นด้วยเว้นวรรค")
            continue

        try:
            sr, sc, tr, tc = map(int, parts)
        except ValueError:
            print("❌ กรุณากรอกเฉพาะตัวเลขเท่านั้น!")
            continue

        valid, err_msg = is_valid_move(board, sr, sc, tr, tc, turn)
        if not valid:
            print(f"❌ เดินไม่ได้: {err_msg}")
            continue

        # ทำการขยับตัวหมาก (Move execution)
        target_piece = board[tr][tc]
        board[tr][tc] = board[sr][sc]
        board[sr][sc] = '.'

        # ตรวจสอบการกิน King (ถ้า King ฝ่ายตรงข้ามหายไป ถือว่าชนะ)
        if target_piece == 'k':
            print_board(board)
            print("🏆 ฝ่ายขาว (White) ชนะ! กิน King ดำได้สำเร็จ!")
            break
        elif target_piece == 'K':
            print_board(board)
            print("🏆 ฝ่ายดำ (Black) ชนะ! กิน King ขาวได้สำเร็จ!")
            break

        # สลับตาเดิน
        turn = 'B' if turn == 'W' else 'W'
