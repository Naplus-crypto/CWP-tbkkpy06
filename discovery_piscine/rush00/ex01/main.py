import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("Error")
        return
    
    # วนลูปอ่านไฟล์ที่ส่งเข้ามาทีละไฟล์ผ่าน command-line arguments
    for filepath in sys.argv[1:]:
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                checkmate(content)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()