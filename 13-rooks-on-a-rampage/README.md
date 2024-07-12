<body>
    <h1>13. Rooks on a rampage</h1>
    <pre>
def safe_squares_rooks(n, rooks):
    </pre>
    <p>
        A generalized n-by-n chessboard has been invaded by a parliament of rooks, each rook represented as a two-tuple (row, column) of the row and the column of the square that the rook is in. Since we are now computer programmers instead of chess players and other healthy and normal folks, our rows and columns are numbered from 0 to n - 1. A chess rook covers all squares that are in the same row or in the same column. Given the board size n and the list of rooks on that board, count the number of empty squares that are safe, that is, are not covered by any rook.
    </p>
    <p>
        To achieve this in reasonable time and memory, you should count separately how many rows and columns on the board are safe from any rook. Because permuting the rows and columns does not change the answer to this question, you can imagine all these safe rows and columns to have been permuted to form an empty rectangle at the top left corner of the board. The area of that safe rectangle is then obviously the product of its known width and height.
    </p>
    <table border="1">
        <thead>
            <tr>
                <th>n</th>
                <th>rooks</th>
                <th>Expected result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>10</td>
                <td>[]</td>
                <td>100</td>
            </tr>
            <tr>
                <td>4</td>
                <td>[(2, 3), (0, 1)]</td>
                <td>4</td>
            </tr>
            <tr>
                <td>8</td>
                <td>[(1, 1), (3, 5), (7, 0), (7, 6)]</td>
                <td>20</td>
            </tr>
            <tr>
                <td>2</td>
                <td>[(1, 1)]</td>
                <td>1</td>
            </tr>
            <tr>
                <td>6</td>
                <td>[(r, r) for r in range(6)]</td>
                <td>0</td>
            </tr>
            <tr>
                <td>100</td>
                <td>[(r, (r*(r-1))%100) for r in range(0, 100, 2)]</td>
                <td>3900</td>
            </tr>
            <tr>
                <td>10**6</td>
                <td>[(r, r) for r in range(10**6)]</td>
                <td>0</td>
            </tr>
        </tbody>
    </table>
</body>