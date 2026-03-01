import mysql.connector as s
import pyfiglet
import time
#--------------------------------------------------------------------------------------------------------------------------------------
def connectionestablisher():
    try:
        con=s.connect(host="localhost",user="root",password="root",database="mysql_prototype")
        if con.is_connected():
            print("")
            print(" ")
            print("𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇 𝖾𝗌𝗍𝖺𝖻𝗅𝗂𝗌𝗁𝖾𝖽.")
            print("")
            print(" ")
            return con
    except s.Error as e:
        print("")
        print(" ")
        print("𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇 𝖿𝖺𝗂𝗅𝖾𝖽.")
        print("")
        print(" ")
        print("𝖤𝗋𝗋𝗈𝗋:",e)
        return None
#--------------------------------------------------------------------------------------------------------------------------------------
def loading_bar_database():
    print("")
    print(" ")
    print("𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗇𝗀", end="")
    for i in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" ✓")
#--------------------------------------------------------------------------------------------------------------------------------------
def options(con,cur):
    if cur is None:
        return
    while True:
        print("")
        print(" ")
        n="""                                                         𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗅𝖾𝖼𝗍 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇.

1) 𝖨𝗇𝗌𝖾𝗋𝗍 𝖱𝖾𝖼𝗈𝗋𝖽?          2) 𝖴𝗉𝖽𝖺𝗍𝖾 𝖱𝖾𝖼𝗈𝗋𝖽?          3) 𝖲𝖾𝗅𝖾𝖼𝗍 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇?          4) 𝖣𝗋𝗈𝗉 𝖺 𝗍𝖺𝖻𝗅𝖾?          5) 𝖵𝗂𝖾𝗐 𝖳𝖺𝖻𝗅𝖾𝗌          6) 𝖢𝗋𝖾𝖺𝗍𝖾 𝖳𝖺𝖻𝗅𝖾
7) 𝖤𝗑𝗂𝗍"""
        for i in n:
            print(i,end="")
        print("")
        print(" ")
        try:
            choice=int(input("𝖤𝗇𝗍𝖾𝗋 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 1-6="))
        except ValueError:
            print("❌ 𝖤𝗇𝗍𝖾𝗋 𝗇𝗎𝗆𝖻𝖾𝗋𝗌 𝗈𝗇𝗅𝗒.")
            continue
        if choice==1:
            insertrecord(con,cur)
        elif choice==2:
            updaterecord(con,cur)
        elif choice==3:
            selectrecord(con,cur)
        elif choice==4:
            droptable(con,cur)
        elif choice==5:
            viewtable(con,cur)
        elif choice==6:
            createtable(con,cur)
        elif choice==7:
            break
        else:
            print("𝖸𝗈𝗎 𝗁𝖺𝗏𝖾 𝖾𝗇𝗍𝖾𝗋𝖾𝖽 𝖺𝗇𝗈𝗍𝗁𝖾𝗋 𝖼𝗁𝗈𝗂𝖼𝖾 𝗍𝗁𝖺𝗇 𝗍𝗁𝖾 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖾𝖽 𝗋𝖺𝗇𝗀𝖾.")
#--------------------------------------------------------------------------------------------------------------------------------------
def cursorobject(con):
    if con is None:
        return None
    print("𝖢𝗋𝖾𝖺𝗍𝗂𝗇𝗀 𝖼𝗎𝗋𝗌𝗈𝗋 𝖮𝖻𝗃𝖾𝖼𝗍", end="")
    for i in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" ✓")
    cur=con.cursor()
    print("𝖢𝗎𝗋𝗌𝗈𝗋 𝖮𝖻𝗃𝖾𝖼𝗍 𝖢𝗋𝖾𝖺𝗍𝖾𝖽!")
    return cur  
#--------------------------------------------------------------------------------------------------------------------------------------
def insertrecord(con,cur):
    showtables(con,cur)
    table = input("𝖤𝗇𝗍𝖾𝗋 𝗍𝖺𝖻𝗅𝖾 𝗇𝖺𝗆𝖾=")
    viewtablealt(con,cur,table)
    desc_data = desctable(con,cur,table)
    if desc_data is None:  # Table doesn't exist
        return  # Go back to menu
    irl=[]
# ... rest of code continues only if table exists
    try:
        n=int(input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝗎𝗆𝖻𝖾𝗋 𝗈𝖿 𝖾𝗇𝗍𝗋𝗂𝖾𝗌 𝗂𝗇 𝗈𝗇𝖾 𝗊𝗎𝖾𝗋𝗒="))
    except ValueError:
        print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖭𝗎𝗆𝖻𝖾𝗋")
        return
    for i in range(n):
        try:
            cho=int(input("""𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗁𝗈𝗂𝖼𝖾 𝗈𝖿 𝖽𝖺𝗍𝖺 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖾𝗇𝗍𝖾𝗋
1) 𝖳𝖾𝗑𝗍
2) 𝖨𝗇𝗍𝖾𝗀𝖾𝗋
3) 𝖤𝖷𝖨𝖳 𝖯𝗅𝖾𝖺𝗌𝖾 𝖾𝗇𝗍𝖾𝗋 𝖿𝗋𝗈𝗆 1-3="""))
        except ValueError:
            print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
        if cho==1:
            txt=input("𝖤𝗇𝗍𝖾𝗋 𝖺 𝗍𝖾𝗑𝗍 𝖽𝖺𝗍𝖺 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖾𝗇𝗍𝖾𝗋=")
            irl.append(txt)
        elif cho==2:
            try:
                irl.append(int(input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝗎𝗆𝖻𝖾𝗋 𝖽𝖺𝗍𝖺 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖾𝗇𝗍𝖾𝗋=")))
            except ValueError:
                print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖭𝗎𝗆𝖻𝖾𝗋")
        elif cho==3:
            break
        else:
            print("𝖸𝗈𝗎 𝗁𝖺𝗏𝖾 𝖾𝗇𝗍𝖾𝗋𝖾𝖽 𝖺𝗇𝗈𝗍𝗁𝖾𝗋 𝗈𝗉𝗍𝗂𝗈𝗇")
    desc_data = desctable(con,cur,table)
    num_columns = len(desc_data)
    while len(irl) < num_columns:
        irl.append(None)
    placeholders = ", ".join(["%s"] * len(irl))
    query = f"INSERT INTO {table} VALUES ({placeholders})"
    try:
        cur.execute(query,tuple(irl))
        con.commit()
        print("✓ 𝖱𝖾𝖼𝗈𝗋𝖽 𝗂𝗇𝗌𝖾𝗋𝗍𝖾𝖽!")
    except s.Error as e:
        print("❌ 𝖨𝗇𝗌𝖾𝗋𝗍 𝖿𝖺𝗂𝗅𝖾𝖽:",e)
#--------------------------------------------------------------------------------------------------------------------------------------
def updaterecord(con,cur):
    showtables(con,cur)
    table=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝖺𝖻𝗅𝖾 𝗇𝖺𝗆𝖾=")
    viewtablealt(con,cur,table)
    desc_data = desctable(con,cur,table)
    if desc_data is None:  # Table doesn't exist
        return 
    irl=[]
    try:
        cho=int(input("""𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗁𝗈𝗂𝖼𝖾 𝗈𝖿 𝖽𝖺𝗍𝖺 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖾𝗇𝗍𝖾𝗋
1) 𝖳𝖾𝗑𝗍
2) 𝖨𝗇𝗍𝖾𝗀𝖾𝗋
3) 𝖤𝖷𝖨𝖳 𝖯𝗅𝖾𝖺𝗌𝖾 𝖾𝗇𝗍𝖾𝗋 𝖿𝗋𝗈𝗆 1-3="""))
    except ValueError:
        print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖭𝗎𝗆𝖻𝖾𝗋")
    if cho==1:
        txt=input("𝖤𝗇𝗍𝖾𝗋 𝖺 𝗍𝖾𝗑𝗍 𝖽𝖺𝗍𝖺 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖾𝗇𝗍𝖾𝗋=")
        irl.append(txt)
    elif cho==2:
        inte=int(input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝗎𝗆𝖻𝖾𝗋 𝖽𝖺𝗍𝖺 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖾𝗇𝗍𝖾𝗋="))
        irl.append(inte)
    elif cho==3:
        return
    else:
        print("𝖸𝗈𝗎 𝗁𝖺𝗏𝖾 𝖾𝗇𝗍𝖾𝗋𝖾𝖽 𝖺𝗇𝗈𝗍𝗁𝖾𝗋 𝗈𝗉𝗍𝗂𝗈𝗇")    
    clmn=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝖺𝗆𝖾 𝗈𝖿 𝗍𝗁𝖾 𝖼𝗈𝗅𝗎𝗆𝗇 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝗎𝗉𝖽𝖺𝗍𝖾 𝗍𝗁𝖾 𝖽𝖺𝗍𝖺 𝗂𝗇=")
    confirm=input("𝖣𝗈 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖺𝖽𝖽 𝖺 𝗐𝗁𝖾𝗋𝖾 𝖼𝗈𝗇𝖽𝗂𝗍𝗂𝗈𝗇? (𝖸/𝖭)=")
    if confirm=="Y":
        modify_column=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗈𝗅𝗎𝗆𝗇 𝗐𝗁𝗂𝖼𝗁 𝗍𝗁𝖾 𝖽𝖺𝗍𝖺 𝗂𝗌 𝗍𝗈 𝖻𝖾 𝗆𝗈𝖽𝗂𝖿𝗂𝖾𝖽=")
        value_location=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗏𝖺𝗅𝗎𝖾 𝖿𝗈𝗋 𝗐𝗁𝗂𝖼𝗁 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗁𝖺𝗍 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖽𝖺𝗍𝖺 𝗍𝗈 𝖻𝖾 𝗆𝗈𝖽𝗂𝖿𝗂𝖾𝖽=")
        placeholders = ", ".join(["%s"] * len(irl))
        query = f"UPDATE {table} SET {clmn}=%s WHERE {modify_column}=%s"
        cur.execute(query, (irl[0], value_location))
    else:
        confirm_all = input("⚠️ 𝖳𝗁𝗂𝗌 𝗐𝗂𝗅𝗅 𝗎𝗉𝖽𝖺𝗍𝖾 𝖠𝖫𝖫 𝗋𝗈𝗐𝗌. 𝖢𝗈𝗇𝗍𝗂𝗇𝗎𝖾? (𝖸/𝖭)=")
        if confirm_all.upper() != "Y":
            return
        query = f"UPDATE {table} SET {clmn}=%s"
    try:
        cur.execute(query, (irl[0],))
        con.commit()
        print("✓ 𝖱𝖾𝖼𝗈𝗋𝖽 𝖴𝗉𝖽𝖺𝗍𝖾𝖽!")
    except s.Error as e:
        print("❌ 𝖴𝗉𝖽𝖺𝗍𝖾 𝖿𝖺𝗂𝗅𝖾𝖽:", e)
#--------------------------------------------------------------------------------------------------------------------------------------
def viewtable(con,cur):
    showtables(con,cur)
    table=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗍𝖺𝖻𝗅𝖾 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝗏𝗂𝖾𝗐=")
    print("")
    print(" ")
    query=f"SELECT * FROM {table}"
    try:  # >>> ERROR HANDLING ADDED
        cur.execute(query)
        data = cur.fetchall()
    except Exception as e:  # >>> ERROR HANDLING ADDED
        print("❌ 𝖤𝗋𝗋𝗈𝗋 𝗐𝗁𝗂𝗅𝖾 𝖿𝖾𝗍𝖼𝗁𝗂𝗇𝗀 𝗍𝖺𝖻𝗅𝖾:", e)
        return  # >>> ERROR HANDLING ADDED

    try:  # >>> ERROR HANDLING ADDED
        desc_data = desctable(con,cur,table)
    except Exception as e:  # >>> ERROR HANDLING ADDED
        print("❌ 𝖤𝗋𝗋𝗈𝗋 𝗐𝗁𝗂𝗅𝖾 𝖿𝖾𝗍𝖼𝗁𝗂𝗇𝗀 𝗍𝖺𝖻𝗅𝖾 𝗌𝗍𝗋𝗎𝖼𝗍𝗎𝗋𝖾:", e)
        return  # >>> ERROR HANDLING ADDED

    headings = [row[0] for row in desc_data]
    print("|", end="")
    for heading in headings:
        print(heading, end="|")
    print()    
    total_length = sum(len(h) for h in headings) + len(headings) + 1
    print("-" * total_length)
    for row in data:
        print("|", end="")
        for item in row:
            print(item, end="|")
        print()
    print("-" * total_length)
    print("𝖣𝖾𝗍𝖺𝗂𝗅𝗌 𝗈𝖿 𝖺𝖻𝗈𝗏𝖾 𝗍𝖺𝖻𝗅𝖾.")
#--------------------------------------------------------------------------------------------------------------------------------------
def desctable(con,cur,table):
    query=f"DESC {table}"
    try:
        cur.execute(query)
        a=cur.fetchall()
        return a
    except s.Error as e:
        print("❌ 𝖤𝗋𝗋𝗈𝗋 𝖿𝖾𝗍𝖼𝗁𝗂𝗇𝗀 𝗍𝖺𝖻𝗅𝖾 𝗌𝗍𝗋𝗎𝖼𝗍𝗎𝗋𝖾:", e)
        return None  # Return None instead of crashing
#--------------------------------------------------------------------------------------------------------------------------------------
def viewtablealt(con,cur,table):
    print("")
    print(" ")
    query=f"SELECT * FROM {table}"
    try:  # >>> ERROR HANDLING ADDED
        cur.execute(query)
        data = cur.fetchall()
    except Exception as e:  # >>> ERROR HANDLING ADDED
        print("❌ 𝖤𝗋𝗋𝗈𝗋 𝗐𝗁𝗂𝗅𝖾 𝖿𝖾𝗍𝖼𝗁𝗂𝗇𝗀 𝗍𝖺𝖻𝗅𝖾:", e)
        return  # >>> ERROR HANDLING ADDED

    try:  # >>> ERROR HANDLING ADDED
        desc_data = desctable(con,cur,table)
    except Exception as e:  # >>> ERROR HANDLING ADDED
        print("❌ 𝖤𝗋𝗋𝗈𝗋 𝗐𝗁𝗂𝗅𝖾 𝖿𝖾𝗍𝖼𝗁𝗂𝗇𝗀 𝗍𝖺𝖻𝗅𝖾 𝗌𝗍𝗋𝗎𝖼𝗍𝗎𝗋𝖾:", e)
        return  # >>> ERROR HANDLING ADDED

    headings = [row[0] for row in desc_data]
    print("|", end="")
    for heading in headings:
        print(heading, end="|")
    print()    
    total_length = sum(len(h) for h in headings) + len(headings) + 1
    print("-" * total_length)
    for row in data:
        print("|", end="")
        for item in row:
            print(item, end="|")
        print()
    print("-" * total_length)
    print("𝖣𝖾𝗍𝖺𝗂𝗅𝗌 𝗈𝖿 𝖺𝖻𝗈𝗏𝖾 𝗍𝖺𝖻𝗅𝖾.")
#--------------------------------------------------------------------------------------------------------------------------------------
def showtables(con,cur):
    liss=[]
    query=f"SHOW TABLES"
    try:
        cur.execute(query)
        a=cur.fetchall()
        for i in a:
            for j in i:
                liss.append(j)
        print(liss)
    except EOFError as e:
        return
#--------------------------------------------------------------------------------------------------------------------------------------
def selectrecord(con,cur):
    showtables(con,cur)
    table=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝖺𝖻𝗅𝖾 𝗇𝖺𝗆𝖾=")
    desc_data = desctable(con,cur,table)
    if desc_data is None:  # Table doesn't exist
        return 
    try:
        n=int(input("""𝖤𝗇𝗍𝖾𝗋 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇=
1) 𝖲𝖾𝗅𝖾𝖼𝗍 𝖺𝗅𝗅 𝗋𝖾𝖼𝗈𝗋𝖽𝗌?
2) 𝖲𝖾𝗅𝖾𝖼𝗍 𝗈𝗇𝖾 𝗋𝖾𝖼𝗈𝗋𝖽?
3) 𝖲𝖾𝗅𝖾𝖼𝗍 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝗋𝖾𝖼𝗈𝗋𝖽𝗌?
4) 𝖤𝗑𝗂𝗍
𝖯𝗅𝖾𝖺𝗌𝖾 𝖼𝗁𝗈𝗈𝗌𝖾 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 1-4->"""))
    except ValueError:
        print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
    if n==1:
        query=f"SELECT * FROM {table}"
        cur.execute(query)
        a=cur.fetchall()
        for i in a:
            print(i)
    elif n==2:
        column=input("𝖤𝗇𝗍𝖾𝗋 𝖺 𝖼𝗈𝗅𝗎𝗆𝗇 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝗌𝖾𝖺𝗋𝖼𝗁 𝖽𝖺𝗍𝖺 𝖿𝗈𝗋=")
        query=f"SELECT {column} FROM {table}"
        cur.execute(query)
        b=cur.fetchall()
        for i in b:
            print(i)
    elif n==3:
        lisstr=[]
        try:
            choice=int(input("𝖤𝗇𝗍𝖾𝗋 𝗇𝗎𝗆𝖻𝖾𝗋 𝗈𝖿 𝖼𝗈𝗅𝗎𝗆𝗇𝗌="))
        except ValueError:  # Changed from TypeError
            print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
            return
        for i in range(choice):
            column=input("𝖤𝗇𝗍𝖾𝗋 𝖼𝗈𝗅𝗎𝗆𝗇=")
            lisstr.append(column)
        columns_str = ", ".join(lisstr)  # FIX HERE
        query=f"SELECT {columns_str} FROM {table}"
        try:
            cur.execute(query)
            a=cur.fetchall()
            for i in a:
                print(i)
        except s.Error as e:
            print("❌ 𝖤𝗋𝗋𝗈𝗋:", e)
    elif n==4:
        exit()
    else:
        print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
#--------------------------------------------------------------------------------------------------------------------------------------
def droptable(con,cur):
    showtables(con,cur)
    table=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗍𝖺𝖻𝗅𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖽𝗋𝗈𝗉 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾=")
    desc_data = desctable(con,cur,table)
    if desc_data is None:  # Table doesn't exist
        return
    query=f"DROP TABLE {table}"
    try:
        cur.execute(query)
    except s.Error as e:
        print("❌ 𝖤𝗋𝗋𝗈𝗋:", e)
#--------------------------------------------------------------------------------------------------------------------------------------
def createtable(con,cur):
    columns=[]
    table=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗍𝖺𝖻𝗅𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖼𝗋𝖾𝖺𝗍𝖾 𝗂𝗇 𝗍𝗁𝖾 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾=")
    try:
        n=int(input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝗎𝗆𝖻𝖾𝗋 𝗈𝖿 𝖼𝗈𝗅𝗎𝗆𝗇𝗌 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗁𝖾 𝗍𝖺𝖻𝗅𝖾 𝗍𝗈 𝗁𝖺𝗏𝖾="))
    except ValueError:
        print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
    for i in range(n):
        a="""𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗅𝖾𝖼𝗍 𝖺 𝖽𝖺𝗍𝖺𝗍𝗒𝗉𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖾𝗇𝗍𝖾𝗋. 𝖳𝗁𝖾𝗌𝖾 𝖺𝗋𝖾 𝗍𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍𝗅𝗒 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝗂𝗍𝖾𝗆𝗌. 𝖳𝗁𝖾𝗋𝖾 𝗂𝗌 𝖺𝗅𝗌𝗈 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝗍𝗈 𝖼𝗋𝖾𝖺𝗍𝖾 𝗍𝗁𝖾 𝗍𝖺𝖻𝗅𝖾.
1) 𝖳𝖾𝗑𝗍 (𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖢𝖧𝖠𝖱, 𝖵𝖠𝖱𝖢𝖧𝖠𝖱)
2) 𝖨𝗇𝗍𝖾𝗀𝖾𝗋 (𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖨𝖭𝖳)
3) 𝖣𝖺𝗍𝖾 (𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖣𝖠𝖳𝖤)
4) 𝖢𝗋𝖾𝖺𝗍𝖾 𝗍𝗁𝖾 𝗍𝖺𝖻𝗅𝖾!
5) 𝖤𝗑𝗂𝗍"""
        for i in a:
            print(i,end="")
        print("")
        print(" ")
        try:
            datatype_choice=int(input("𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗅𝖾𝖼𝗍 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 1-5="))
        except ValueError:
            print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
        if datatype_choice==1:
            l="""𝖳𝗁𝖾𝗋𝖾 𝗂𝗌 𝗂𝗇𝗌𝖾𝗋𝗍𝗂𝗈𝗇 𝖺𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖿𝗈𝗋
1) 𝖢𝖧𝖠𝖱(𝖬)
2) 𝖵𝖠𝖱𝖢𝖧𝖠𝖱(𝖬)
3) 𝖤𝗑𝗂𝗍"""
            for i in l:
                print(i,end="")
            print("")
            print(" ")
            try:
                tt=int(input("𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗅𝖾𝖼𝗍 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 1-3="))
            except ValueError:
                print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
            if tt==1:
                M=int(input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝗎𝗆𝖻𝖾𝗋 𝗈𝖿 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗒𝗈𝗎𝗋 𝖢𝖧𝖠𝖱 𝖼𝗈𝗅𝗎𝗆𝗇 𝗍𝗈 𝗁𝗈𝗅𝖽="))
                mm=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝖺𝗆𝖾 𝗈𝖿 𝗍𝗁𝖾 𝖼𝗈𝗅𝗎𝗆𝗇=")
                tup=(mm,f"CHAR({M})")
                columns.append(tup)
            elif tt==2:
                M=int(input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝗎𝗆𝖻𝖾𝗋 𝗈𝖿 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗒𝗈𝗎𝗋 𝖵𝖠𝖱𝖢𝖧𝖠𝖱 𝖼𝗈𝗅𝗎𝗆𝗇 𝗍𝗈 𝗁𝗈𝗅𝖽="))
                mm=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝖺𝗆𝖾 𝗈𝖿 𝗍𝗁𝖾 𝖼𝗈𝗅𝗎𝗆𝗇=")
                tup=(mm,f"VARCHAR({M})")
                columns.append(tup)
            elif tt==3:
                break
            else:
                print("𝖸𝗈𝗎 𝗁𝖺𝗏𝖾 𝖾𝗇𝗍𝖾𝗋𝖾𝖽 𝖺𝗇𝗈𝗍𝗁𝖾𝗋 𝗈𝗉𝗍𝗂𝗈𝗇")
        elif datatype_choice==2:
            mmm="""𝖳𝗁𝖾𝗋𝖾 𝗂𝗌 𝗂𝗇𝗌𝖾𝗋𝗍𝗂𝗈𝗇 𝖺𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖿𝗈𝗋
1) 𝖨𝖭𝖳
2) 𝖤𝗑𝗂𝗍"""
            for i in mmm:
                print(i,end="")
            try:
                ss=int(input("𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗅𝖾𝖼𝗍 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 1-2="))
            except ValueError:
                print("❌ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝗈𝗂𝖼𝖾")
            if ss==1:
                mm=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝖺𝗆𝖾 𝗈𝖿 𝗍𝗁𝖾 𝖼𝗈𝗅𝗎𝗆𝗇=")
                tup=(mm,"INT")
                columns.append(tup)
            elif ss==2:
                break
            else:
                print("𝖸𝗈𝗎 𝗁𝖺𝗏𝖾 𝖾𝗇𝗍𝖾𝗋𝖾𝖽 𝖺𝗇𝗈𝗍𝗁𝖾𝗋 𝗈𝗉𝗍𝗂𝗈𝗇")
        elif datatype_choice==3:  # DATE
            mm=input("𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗇𝖺𝗆𝖾 𝗈𝖿 𝗍𝗁𝖾 𝖼𝗈𝗅𝗎𝗆𝗇=")
            tup=(mm, "DATE")
            columns.append(tup)
        elif datatype_choice==4:  # Finish and create table
            break
        elif datatype_choice==5:  # Exit without creating
            return  
    if not columns:
        print("❌ 𝖭𝗈 𝖼𝗈𝗅𝗎𝗆𝗇𝗌 𝖽𝖾𝖿𝗂𝗇𝖾𝖽!")
        return
    column_defs = ", ".join([f"`{col_name}` {col_type}" for col_name, col_type in columns])
    query = f"CREATE TABLE {table} ({column_defs})"
    try:
        cur.execute(query)
        con.commit()
        print(f"✓ 𝖳𝖺𝖻𝗅𝖾 {table} 𝖼𝗋𝖾𝖺𝗍𝖾𝖽!")
    except s.Error as e:
        print("❌ 𝖤𝗋𝗋𝗈𝗋:", e)    
#--------------------------------------------------------------------------------------------------------------------------------------
for i in range(131):
    print("~",end="")
for i in range(131):
    print("~",end="")
#--------------------------------------------------------------------------------------------------------------------------------------
heading=pyfiglet.figlet_format("Welcome to SQL through Python!", width=150)
print(heading)
#--------------------------------------------------------------------------------------------------------------------------------------
for i in range(131):
    print("~",end="")
for i in range(131):
    print("~",end="")
a="                      𝖳𝗁𝗂𝗌 𝗉𝗋𝗈𝗀𝗋𝖺𝗆 𝗂𝗌 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼𝖺𝗅𝗅𝗒 𝖽𝖾𝗌𝗂𝗀𝗇𝖾𝖽 𝗍𝗈 𝖻𝖾 𝖺𝖻𝗅𝖾 𝗍𝗈 𝖺𝖼𝖼𝖾𝗌𝗌 𝗍𝗁𝖾 𝗆𝗒𝗌𝗊𝗅_𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾, 𝖺𝗇𝖽 𝗒𝗈𝗎 𝖼𝖺𝗇 𝖠𝖽𝖽, 𝖴𝗉𝖽𝖺𝗍𝖾, 𝖨𝗇𝗌𝖾𝗋𝗍 𝖽𝖺𝗍𝖺, 𝖾𝗍𝖼...."
for i in a:
    print(i,end="")
print("")
print(" ")
#--------------------------------------------------------------------------------------------------------------------------------------
while True:
    a="                                                    𝖯𝗅𝖾𝖺𝗌𝖾 𝖼𝗁𝗈𝗈𝗌𝖾 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝗍𝗁𝗂𝗌 𝗅𝗂𝗌𝗍."
    for i in a:
        print(i,end="")
    print("")
    print(" ")
    a="""1)𝖠𝖻𝗈𝗎𝗍 𝗍𝗁𝖾 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋
2)𝖠𝖼𝖼𝖾𝗌𝗌 𝗍𝗁𝖾 𝖯𝗋𝗈𝗀𝗋𝖺𝗆
3)𝖤𝖷𝖨𝖳."""
    for i in a:
        print(i,end="")
    print("")
    print(" ")
    b=int(input("𝖤𝗇𝗍𝖾𝗋 𝖺𝗇 𝗈𝗉𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 1-3 ="))
    if b==1:
        print("")
        print(" ")
        a="""𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: 𝖠𝗄𝖺𝗌𝗁 𝖪𝖺𝗋𝗍𝗁𝗂𝗄𝖾𝗒𝖺𝗇

𝗪𝗵𝗮𝘁 𝗜 𝗠𝗮𝗱𝗲: 𝖳𝗁𝗂𝗌 𝗂𝗌 𝖺 𝖯𝗒𝗍𝗁𝗈𝗇-𝖻𝖺𝗌𝖾𝖽 𝖬𝗒𝖲𝖰𝖫 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝖬𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝖲𝗒𝗌𝗍𝖾𝗆 𝗍𝗁𝖺𝗍 𝗉𝗋𝗈𝗏𝗂𝖽𝖾𝗌 𝖺𝗇 𝗂𝗇𝗍𝖾𝗋𝖺𝖼𝗍𝗂𝗏𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽-𝗅𝗂𝗇𝖾 𝗂𝗇𝗍𝖾𝗋𝖿𝖺𝖼𝖾 𝖿𝗈𝗋 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝗈𝗉𝖾𝗋𝖺𝗍𝗂𝗈𝗇𝗌.
𝖳𝗁𝖾 𝗉𝗋𝗈𝗀𝗋𝖺𝗆 𝗂𝗇𝗍𝖾𝗀𝗋𝖺𝗍𝖾𝗌 𝖯𝗒𝗍𝗁𝗈𝗇 𝗐𝗂𝗍𝗁 𝖬𝗒𝖲𝖰𝖫 𝗎𝗌𝗂𝗇𝗀 𝗍𝗁𝖾 𝗆𝗒𝗌𝗊𝗅.𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗈𝗋 𝗅𝗂𝖻𝗋𝖺𝗋𝗒, 𝖺𝗅𝗅𝗈𝗐𝗂𝗇𝗀 𝗎𝗌𝖾𝗋𝗌 𝗍𝗈 𝗉𝖾𝗋𝖿𝗈𝗋𝗆 𝖢𝖱𝖴𝖣 𝗈𝗉𝖾𝗋𝖺𝗍𝗂𝗈𝗇𝗌 (𝖢𝗋𝖾𝖺𝗍𝖾,𝖱𝖾𝖺𝖽,𝖴𝗉𝖽𝖺𝗍𝖾,𝖣𝖾𝗅𝖾𝗍𝖾)𝗈𝗇 𝗍𝗁𝖾 𝗆𝗒𝗌𝗊𝗅_𝗉𝗋𝗈𝗍𝗈𝗍𝗒𝗉𝖾 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝗍𝗁𝗋𝗈𝗎𝗀𝗁
𝖺𝗇 𝗂𝗇𝗍𝗎𝗂𝗍𝗂𝗏𝖾 𝗆𝖾𝗇𝗎-𝖽𝗋𝗂𝗏𝖾𝗇 𝗌𝗒𝗌𝗍𝖾𝗆.

𝗣𝘂𝗿𝗽𝗼𝘀𝗲: 𝖳𝗁𝖾 𝗉𝗎𝗋𝗉𝗈𝗌𝖾 𝗈𝖿 𝗍𝗁𝗂𝗌 𝗉𝗋𝗈𝗃𝖾𝖼𝗍 𝗂𝗌 𝗍𝗈 𝖽𝖾𝗆𝗈𝗇𝗌𝗍𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝗌𝖾𝖺𝗆𝗅𝖾𝗌𝗌 𝗂𝗇𝗍𝖾𝗀𝗋𝖺𝗍𝗂𝗈𝗇 𝖻𝖾𝗍𝗐𝖾𝖾𝗇 𝖯𝗒𝗍𝗁𝗈𝗇 𝖺𝗇𝖽 𝖬𝗒𝖲𝖰𝖫 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾𝗌, 𝗆𝖺𝗄𝗂𝗇𝗀 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝖺𝖼𝖼𝖾𝗌𝗌𝗂𝖻𝗅𝖾 𝗍𝗁𝗋𝗈𝗎𝗀𝗁 𝖺 𝗎𝗌𝖾𝗋-𝖿𝗋𝗂𝖾𝗇𝖽𝗅𝗒 𝗂𝗇𝗍𝖾𝗋𝖿𝖺𝖼𝖾.
𝖳𝗁𝗂𝗌 𝗍𝗈𝗈𝗅 𝗌𝗂𝗆𝗉𝗅𝗂𝖿𝗂𝖾𝗌 𝖼𝗈𝗆𝗉𝗅𝖾𝗑 𝖲𝖰𝖫 𝗈𝗉𝖾𝗋𝖺𝗍𝗂𝗈𝗇𝗌 𝖻𝗒 𝗉𝗋𝗈𝗏𝗂𝖽𝗂𝗇𝗀 𝖺𝗇 𝗈𝗋𝗀𝖺𝗇𝗂𝗓𝖾𝖽 𝗆𝖾𝗇𝗎 𝗌𝗒𝗌𝗍𝖾𝗆, 𝖾𝗇𝖺𝖻𝗅𝗂𝗇𝗀 𝗎𝗌𝖾𝗋𝗌 𝗍𝗈 𝗂𝗇𝗍𝖾𝗋𝖺𝖼𝗍 𝗐𝗂𝗍𝗁 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗐𝗋𝗂𝗍𝗂𝗇𝗀 𝗋𝖺𝗐 𝖲𝖰𝖫 𝗊𝗎𝖾𝗋𝗂𝖾𝗌. 𝖨𝗍 𝗌𝖾𝗋𝗏𝖾𝗌 𝖺𝗌 𝖻𝗈𝗍𝗁 𝖺 𝗉𝗋𝖺𝖼𝗍𝗂𝖼𝖺𝗅 
𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝗍𝗈𝗈𝗅 𝖺𝗇𝖽 𝖺 𝗅𝖾𝖺𝗋𝗇𝗂𝗇𝗀 𝗋𝖾𝗌𝗈𝗎𝗋𝖼𝖾 𝖿𝗈𝗋 𝗎𝗇𝖽𝖾𝗋𝗌𝗍𝖺𝗇𝖽𝗂𝗇𝗀 𝖯𝗒𝗍𝗁𝗈𝗇-𝖬𝗒𝖲𝖰𝖫 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗏𝗂𝗍𝗒.

𝗞𝗲𝘆 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀:
• 𝖨𝗇𝗍𝖾𝗋𝖺𝖼𝗍𝗂𝗏𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽-𝗅𝗂𝗇𝖾 𝗂𝗇𝗍𝖾𝗋𝖿𝖺𝖼𝖾 𝗐𝗂𝗍𝗁 𝖠𝖲𝖢𝖨𝖨 𝖺𝗋𝗍 𝗉𝗋𝖾𝗌𝖾𝗇𝗍𝖺𝗍𝗂𝗈𝗇
• 𝖬𝗒𝖲𝖰𝖫 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗏𝗂𝗍𝗒 𝖺𝗇𝖽 𝗏𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇
• 𝖬𝖾𝗇𝗎-𝖽𝗋𝗂𝗏𝖾𝗇 𝗇𝖺𝗏𝗂𝗀𝖺𝗍𝗂𝗈𝗇 𝗌𝗒𝗌𝗍𝖾𝗆
• 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖿𝗈𝗋 𝖼𝗈𝗆𝗉𝗅𝖾𝗍𝖾 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝗈𝗉𝖾𝗋𝖺𝗍𝗂𝗈𝗇𝗌
• 𝖢𝗅𝖾𝖺𝗇, 𝖺𝖾𝗌𝗍𝗁𝖾𝗍𝗂𝖼 𝗍𝖾𝗋𝗆𝗂𝗇𝖺𝗅 𝗈𝗎𝗍𝗉𝗎𝗍 𝖽𝖾𝗌𝗂𝗀𝗇"""
        for j in a:
            print(j,end="")
        print("")
        print(" ")
    elif b==2:
        loading_bar_database()
        con = connectionestablisher()
        cur = cursorobject(con)
        options(con,cur)
    elif b==3:
        break
