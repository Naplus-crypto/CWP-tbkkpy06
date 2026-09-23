def is_in_check(board: str) -> bool:
    """ ฟังก์ชันคืนค่า True ถ้า King โดนรุก (Success), False ถ้าไม่โดน (Fail), หรือ None ถ้ามี Error """
    if not board:
        return None

    lines = board.strip().splitlines()
    if not lines or not lines[0]:
        return None

    rows = len(lines)
    cols = len(lines[0])

    for line in lines:
        if len(line) != cols:
            return None

    king_pos = None
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == 'K':
                if king_pos is not None:
                    return None
                king_pos = (r, c)

    if king_pos is None:
        return None

    kr, kc = king_pos
    valid_pieces = {'P', 'B', 'R', 'Q', 'K'}

    # 1. Pawn
    pawn_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in pawn_offsets:
        nr, nc = kr + dr, kc + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if lines[nr][nc] == 'P':
                return True

    # 2. Rook / Queen (แนวตรง)
    ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in ortho_dirs:
        curr_r, curr_c = kr + dr, kc + dc
        while 0 <= curr_r < rows and 0 <= curr_c < cols:
            char = lines[curr_r][curr_c]
            if char in valid_pieces:
                if char in {'R', 'Q'}:
                    return True
                break
            curr_r += dr
            curr_c += dc

    # 3. Bishop / Queen (แนวทแยง)
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diag_dirs:
        curr_r, curr_c = kr + dr, kc + dc
        while 0 <= curr_r < rows and 0 <= curr_c < cols:
            char = lines[curr_r][curr_c]
            if char in valid_pieces:
                if char in {'B', 'Q'}:
                    return True
                break
            curr_r += dr
            curr_c += dc

    return False

def checkmate(board: str):
    """ ฟังก์ชันดั้งเดิมสำหรับพิมพ์ Success/Fail (ใช้ในโหมดรับไฟล์ปกติ) """
    result = is_in_check(board)
    if result is True:
        print("Success")
    elif result is False:
        print("Fail")
    else:
        print("Error")
