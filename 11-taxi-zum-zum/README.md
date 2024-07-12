<body>
    <h1>11. Taxi Zum Zum</h1>
    <pre>
def taxi_zum_zum(moves):
    </pre>
    <p>
        🎶 The sole spot of light in the night, blinks on the roof of the taxi... 🎶 that is casually cruising in the street grid of the dusky Manhattan, the city we know and love from classic hard boiled film noir works such as 
        <a href="https://en.wikipedia.org/wiki/Blast_of_Silence">Blast of Silence</a>. The taxicab starts its journey at the origin (0, 0) of the infinite two-dimensional integer grid, denoted by Z². Fitting in the gaunt and angular spirit of the time that tolerates few deviations or gray areas, the taxicab is at all times headed straight in one of the four main axis directions, initially north.
    </p>
    <p>
        This taxicab then executes the given sequence of moves, given as a string of characters 'L' for turning 90 degrees left while standing in place (just in case we are making a turn backwards, in case you spotted some glad rags or some out-of-town palooka looking to be taken for a ride), 'R' for turning 90 degrees right (ditto), and 'F' for moving one block forward to current heading. This function should return the final position of the taxicab on this infinitely spanning Manhattan that has no borders. (As someone hypothesized, the rest of the world simulates it with mirrors.)
    </p>
    <table border="1">
        <thead>
            <tr>
                <th>moves</th>
                <th>Expected result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>'RFRL'</td>
                <td>(1, 0)</td>
            </tr>
            <tr>
                <td>'LFFLF'</td>
                <td>(-2, -1)</td>
            </tr>
            <tr>
                <td>'LLFLFLRLF'</td>
                <td>(1, 0)</td>
            </tr>
            <tr>
                <td>'FR' * 1729</td>
                <td>(0, 1)</td>
            </tr>
            <tr>
                <td>'FFLLLFRLFRLFRRL'</td>
                <td>(3, 2)</td>
            </tr>
        </tbody>
    </table>
    <p>
        As an aside, why do these problems always seem to take place in Manhattan and evoke nostalgic visuals of Jackie Mason or that Woodsy Allen fellow with the grumpy immigrant cabbie and various colourful bystander characters, instead of being set in, say, the mile high city of Denver whose street grid is cleverly rotated 45 degrees from the main compass axes to equalize the amount of daily sunlight on streets in both orientations? That ought to make for an interesting variation to many problems of this spirit. Unfortunately, diagonal moves always maintain the total parity of the coordinates, which makes it impossible to reach any coordinate pair of opposite parity in this manner, as in that old joke with the punchline “Gee... I don’t think that you can get there from here.”
    </p>
</body>
