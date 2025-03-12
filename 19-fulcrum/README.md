<body>
    <h1>19. Fulcrum</h1>
    <pre>
def can_balance(items):
    </pre>
    <p>
        Each element in items is a positive integer, in this problem considered to be a physical weight. Your task is to find a fulcrum position in this list of weights so that when balanced on that position, the total torque of the items to the left of that position equals the total torque of the items to the right of that position. The item on the fulcrum is assumed to be centered symmetrically on the fulcrum, and so does not participate in the torque calculation.
    </p>
    <p>
        In physics, the torque of an item with respect to the fulcrum equals its weight times distance from the fulcrum. If a fulcrum position exists, return that position. Otherwise return –1 to artificially indicate that the given items cannot be balanced, at least without rearranging them.
    </p>
    <p>
        The problem of finding the fulcrum position when rearranging elements is allowed would be an interesting but a more advanced problem suitable for motivated students in a third year computer science course. However, this algorithm could be already built based on what we have learned so far in an effective (although not as efficient) brute force fashion around this function by using the generator permutations in the Python standard library module itertools to try out all possible permutations in an outer loop until the inner loop finds one permutation that balances. (In fact, quite a few problems of this style can be solved with this “generate and test” approach without having to resort to the general backtracking algorithm taught in the third year.)
    </p>
    <h2>Examples</h2>
    <table border="1">
        <thead>
            <tr>
                <th>items</th>
                <th>Expected result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[6, 1, 10, 5, 4]</td>
                <td>2</td>
            </tr>
            <tr>
                <td>[10, 3, 3, 2, 1]</td>
                <td>1</td>
            </tr>
            <tr>
                <td>[7, 3, 4, 2, 9, 7, 4]</td>
                <td>-1</td>
            </tr>
            <tr>
                <td>[42]</td>
                <td>0</td>
            </tr>
        </tbody>
    </table>
</body>