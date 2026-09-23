def checkmate(board: str):
    if not board:
        print("Fail")
        return

    # แยกบอร์ดเป็นบรรทัด
    lines = board.strip("\n").split("\n")
    if not lines or not lines[0]:
        print("Fail")
        return

    rows = len(lines)
    cols = len(lines[0])
    
    # ตรวจสอบความถูกต้องของตาราง (ต้องเป็นสี่เหลี่ยมผืนผ้า/จัตุรัสที่ขนาดแถวเท่ากัน)
    for line in lines:
        if len(line) != cols:
            print("Error")
            return

    # ค้นหาตำแหน่งของ King (K)
    king_pos = None
    for r in range(rows):
        for c in range(cols):
            char = lines[r][c]
            if char == 'K':
                if king_pos is not None:
                    print("Error")  // มี King มากกว่า 1 ตัว
                    return
                king_pos = (r, c)

    if king_pos is None:
        print("Fail")
        return

    kr, kc = king_pos
    valid_pieces = {'P', 'B', 'R', 'Q', 'K'}

    # 1. ตรวจสอบ Pawn (P) - โจมตีทแยง 1 ช่องรอบตัว
    pawn_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in pawn_offsets:
        nr, nc = kr + dr, kc + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if lines[nr][nc] == 'P':
                print("Success")
                return

    # 2. ตรวจสอบ Rook (R) และ Queen (Q) - แนวตรง 4 ทิศทาง
    ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in ortho_dirs:
        curr_r, curr_c = kr + dr, kc + dc
        while 0 <= curr_r < rows and 0 <= curr_c < cols:
            char = lines[curr_r][curr_c]
            if char in valid_pieces:
                if char in {'R', 'Q'}:
                    print("Success")
                    return
                break
            curr_r += dr
            curr_c += dc

    # 3. ตรวจสอบ Bishop (B) และ Queen (Q) - แนวทแยง 4 ทิศทาง
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diag_dirs:
        curr_r, curr_c = kr + dr, kc + dc
        while 0 <= curr_r < rows and 0 <= curr_c < cols:
            char = lines[curr_r][curr_c]
            if char in valid_pieces:
                if char in {'B', 'Q'}:
                    print("Success")
                    return
                break
            curr_r += dr
            curr_c += dc

    print("Fail")