from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    playing = True
    results = 0
    tie = 0
    total = 0

    while playing:
        player = None
        player = input("Enter your choice (rock, paper, scissors) : ")
        total += 1
        if player not in options:
            print("you choose an invalid option")
        else:
            print(f"Computer choose : {computer}")
            if player == computer:
                print("Match is TIE!")
            elif player == "rock" and computer == "scissors":
                print("You win!")
                results += 1
            elif player == "paper" and computer == "rock":
                print("You win!")
                results += 1
            elif player == "scissors" and computer == "paper":
                print("You win!")
                results += 1
            else:
                print("You lose!")
            player = input("Want to play again (y/n) : ")
            if player == "y":
                playing
            else:
                playing = False
    print()
    print("------------Final Result--------------")
    print()
    if playing == False:
        print(f"You won {results} time(s)")
        print(f"Win rate {results / total * 100:.2f}%")

    return render_template("app-index.html", result=results, tie=tie, player=player, computer=computer)

if __name__ == "__main__":
    app.run(debug=True)
