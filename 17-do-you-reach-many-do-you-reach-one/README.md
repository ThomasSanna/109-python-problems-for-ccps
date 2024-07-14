<body>
    <h1>17. Do you reach many, do you reach one?</h1>
    <pre>
def knight_jump(knight, start, end):
    </pre>
    <p>
        An ordinary chess knight on a two-dimensional board of squares can make an “L–move” into up to eight possible neighbours. However, as has so often been depicted in various works of space opera, higher than us hairless apes and therefore more logical beings can generalize the chessboard to k dimensions from the puny two more suitable for us hairless apes who have barely evolved to come down from swinging from the trees. A natural generalization of the knight’s move while maintaining its spirit is to define the possible moves as some k-tuple of strictly decreasing nonnegative integer offsets. Each one of these k offsets must be used for exactly one dimension of your choice during the move, either as a positive or a negative version, to determine the square where the k-knight will teleport as the unseen hand of the player lifts it there through the dimension k + 1.
    </p>
    <p>
        Given the start and the end positions as k-tuples of integer coordinates, determine whether the knight could legally move from start to end in a single teleporting jump.
    </p>
    <h2>Examples</h2>
    <table border="1">
        <thead>
            <tr>
                <th>Knight</th>
                <th>Start</th>
                <th>End</th>
                <th>Expected result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>(2, 1)</td>
                <td>(12, 10)</td>
                <td>(11, 12)</td>
                <td>True</td>
            </tr>
            <tr>
                <td>(7, 5, 1)</td>
                <td>(15, 11, 16)</td>
                <td>(8, 12, 11)</td>
                <td>True</td>
            </tr>
            <tr>
                <td>(9, 7, 6, 5, 1)</td>
                <td>(19, 12, 14, 11, 20)</td>
                <td>(24, 3, 20, 11, 13)</td>
                <td>False</td>
            </tr>
        </tbody>
    </table>
    <p>
        A quick combinatorial calculation reveals that exactly k! × 2<sup>k</sup> possible neighbours are reachable in a single move, excepting the moves that would jump outside the board. In this notation, the ordinary chess knight is a (2,1)–knight that reaches up to 2! × 2<sup>2</sup> = 8 neighbours in one jump. A 6-dimensional knight could reach a whopping 6! × 2<sup>6</sup> = 46080 different neighbours in one jump! Since the number of possible moves emanating from each position grows exponentially with respect to k, pretty much everything ends up being close to almost everything else in high-dimensional spaces, which gives predators too much of an edge over their prey for life to ever have a prayer in such spaces. Three dimensions feels just right for life to be comfortable and balanced, as all things should be.
    </p>
</body>