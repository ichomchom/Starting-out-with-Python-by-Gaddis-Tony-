def main():
    file = open('web.html', 'w')
    name = input('Enter your name: ')
    desc = input('Describe yourself: ')
    top ="""<html>
<head>
</head>
<body>
    <center>
        <h1>"""

    
    mid ="""</h1>
    </center>
        <hr />"""
    bot = """
        <hr />
</body>
</html>"""
    file.write(top)
    file.write(name)
    file.write(mid)
    file.write(desc)
    file.write(bot)
main()    
