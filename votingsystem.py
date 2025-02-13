def get_nominees():
    """
    Get the names of the nominees from the user.
    """
    nominees = []
    num_nominees = int(input("Enter the number of nominees: "))
    for i in range(num_nominees):
        name = input(f"Enter the name of nominee {i+1}: ")
        nominees.append(name)
    return nominees

def initialize_votes(nominees):
    """
    Initialize vote counts for each nominee.
    """
    return {nominee: 0 for nominee in nominees}

def get_voter_ids():
    """
    Generate a list of voter IDs.
    """
    num_voters = int(input("Enter the total number of voters: "))
    return list(range(1, num_voters + 1))

def display_results(nominees, votes, total_voters):
    """
    Display the voting results and determine the winner.
    """
    print("\nVoting session is over.")
    print("-----------------------------------")
    print("Voting Results:")
    max_votes = max(votes.values())
    winners = [nominee for nominee, vote in votes.items() if vote == max_votes]

    for nominee, vote in votes.items():
        percent = (vote / total_voters) * 100
        print(f"{nominee}: {vote} votes ({percent:.2f}%)")

    if len(winners) == 1:
        print(f"\n{winners[0]} has won the election!")
    else:
        print("\nIt's a tie between:", ", ".join(winners))

def voting_session(nominees, votes, voter_ids):
    """
    Conduct the voting session.
    """
    while voter_ids:
        try:
            voter = int(input("\nEnter your voter ID: "))
            if voter in voter_ids:
                print("You are eligible to vote.")
                voter_ids.remove(voter)
                print("-----------------------------------")
                for i, nominee in enumerate(nominees, start=1):
                    print(f"To vote for {nominee}, press {i}")
                print("-----------------------------------")

                vote = int(input("Enter your vote: "))
                if 1 <= vote <= len(nominees):
                    votes[nominees[vote - 1]] += 1
                    print(f"Thank you for voting for {nominees[vote - 1]}!")
                else:
                    print("Invalid vote. Please try again.")
            else:
                print("Invalid voter ID or you have already voted.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function to run the voting system.
    """
    print("Welcome to the Voting System!")
    nominees = get_nominees()
    votes = initialize_votes(nominees)
    voter_ids = get_voter_ids()
    total_voters = len(voter_ids)

    print("\nVoting session begins...")
    voting_session(nominees, votes, voter_ids)
    display_results(nominees, votes, total_voters)

# Start the program
if __name__ == "__main__":
    main()