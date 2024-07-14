<body>
    <h1>16. The card that wins the trick</h1>
    <pre>
def winning_card(cards, trump=None):
    </pre>
    <p>
        Playing cards are represented as tuples of (rank, suit) as in the cardproblems.py lecture example program. In trick-taking games such as whist or bridge, each one of the four players plays one card from their hands into the trick. Starting from the player who leads into the trick by playing the first card, the remaining players play their cards sequentially so that each player has to play his card only after having seen the cards that the previous players played into that trick. The following rules determine which one of the four cards played to the trick wins the trick:
    </p>
    <ol>
        <li>If one or more cards of the trump suit have been played to the trick, the trick is won by the highest-ranking trump card, regardless of the other cards played.</li>
        <li>If no trump cards have been played to the trick, the trick is won by the highest card of the suit of the first card played to the trick. Cards of any other suits, regardless of their rank, are powerless to win that trick.</li>
        <li>Ace is the highest card in each suit.</li>
    </ol>
    <p>
        This function should return the winning card for the list of cards played to the trick. Note that the order in which the cards are played to the trick greatly affects the outcome of that trick, since the first card dictates which suits have the potential to win the trick after that lead.
    </p>
    <table border="1">
        <thead>
            <tr>
                <th>Cards</th>
                <th>Trump</th>
                <th>Expected Result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[('three', 'spades'), ('ace', 'diamonds'), ('jack', 'spades'), ('eight', 'spades')]</td>
                <td>None</td>
                <td>('jack', 'spades')</td>
            </tr>
            <tr>
                <td>[('ace', 'diamonds'), ('ace', 'hearts'), ('ace', 'spades'), ('two', 'clubs')]</td>
                <td>'clubs'</td>
                <td>('two', 'clubs')</td>
            </tr>
            <tr>
                <td>[('two', 'clubs'), ('ace', 'diamonds'), ('ace', 'hearts'), ('ace', 'spades')]</td>
                <td>None</td>
                <td>('two', 'clubs')</td>
            </tr>
            <tr>
                <td>[('six', 'hearts'), ('ace', 'spades'), ('three', 'hearts'), ('jack', 'hearts')]</td>
                <td>'hearts'</td>
                <td>('jack', 'hearts')</td>
            </tr>
            <tr>
                <td>[('jack', 'spades'), ('queen', 'spades'), ('eight', 'spades'), ('two', 'diamonds')]</td>
                <td>'diamonds'</td>
                <td>('two', 'diamonds')</td>
            </tr>
            <tr>
                <td>[('jack', 'spades'), ('queen', 'spades'), ('eight', 'spades'), ('two', 'diamonds')]</td>
                <td>'clubs'</td>
                <td>('queen', 'spades')</td>
            </tr>
        </tbody>
    </table>
</body>