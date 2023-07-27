def draw_line(ch,l):
    for i in range(l):
        print(ch,end=" ")
    print()

def main():
    draw_line("*",20)
    draw_line("$",10)
    draw_line(l=5,ch="#")

main()