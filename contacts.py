contacts = {#dictionary
    "number":4,#Key:Value
    "students":#Key:Array list
    [    #{"Key":"Value", "Key":"Value"},
        {"name":"Sarah Holderness", "email":"Sarah194@example.com"},
        {"name":"Joseph Yeon", "email":"Jyeono94@example.com"},
        {"name":"iLucke", "email":"ilucke94@example.com"},
        {"name":"Poop", "email":"pooper94@example.com"}
    ]
}
    #variable in dictionary calls list
for student in contacts ["students"]:
    print(student["email"]) 