def q10(matrix, vector):

    def det(matrix):
        if len(matrix) == 1:
            return int(matrix[0][0])
        else:
            sum = 0
            for j in range(0, len(matrix)):
                a_0j = matrix[j][0]
                s_j = (-1)**j
                matrix_j = [column for column in matrix if column != matrix[j]]
                matrix_0 = [matrix_j[i][1::] for i in range(0, len(matrix_j))]
                sum += s_j * a_0j * det(matrix_0)
            return sum

    def cramer(matrix, vector):
        values = list()
        for j in range(0, len(matrix)):
            A_j = matrix.copy()
            A = matrix
            A_j[j] = vector
            det_A = det(A)
            if det_A == 0:
                return None
            x_j = det(A_j) / det_A
            values.append(x_j)
        return values

    return cramer(matrix, vector)
