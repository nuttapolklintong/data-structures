students = []

while True:
    choice = input("กด a เพื่อเพิ่มข้อมูล, กด q เพื่อออก, กด p เพื่อแสดงข้อมูล: ").lower()

    if choice == 'a':
        print("\n=== เพิ่มข้อมูลนักศึกษา ===")
        student = {}
        student["รหัส"] = input("รหัส: ")
        student["ชื่อ"] = input("ชื่อ: ")
        student["นามสกุล"] = input("นามสกุล: ")
        student["เบอร์โทร"] = input("เบอร์โทร: ")
        student["เพศ"] = input("เพศ: ")
        student["สาขาวิชา"] = input("สาขาวิชา: ")
        students.append(student)
        print("บันทึกข้อมูลเรียบร้อย!\n")

    elif choice == 'p':
        print("\n=== แสดงข้อมูลนักศึกษาทั้งหมด ===")
        if len(students) == 0:
            print("ยังไม่มีข้อมูล\n")
        else:
            for i, s in enumerate(students, start=1):
                print(f"คนที่ {i}")
                print(f"รหัส: {s['รหัส']}")
                print(f"ชื่อ: {s['ชื่อ']} {s['นามสกุล']}")
                print(f"เบอร์โทร: {s['เบอร์โทร']}")
                print(f"เพศ: {s['เพศ']}")
                print(f"สาขาวิชา: {s['สาขาวิชา']}")
                print("-" * 30)
            print("รวมทั้งหมด:", len(students), "คน\n")

    elif choice == 'q':
        print("\nออกจากโปรแกรมแล้ว\n")
        break

    else:
        print("กรุณากดเฉพาะ a, p หรือ q เท่านั้น!\n")
