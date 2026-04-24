import copy

def is_consistent(h, x):
    return all(h[i] == '?' or h[i] == x[i] for i in range(len(h)))

def more_general(h1, h2):
    return all(h1[i] == '?' or h1[i] == h2[i] for i in range(len(h1)))

def remove_duplicates(hypotheses):
    unique = []
    for h in hypotheses:
        if h not in unique:
            unique.append(h)
    return unique

def candidate_elimination(df):
    n = len(df.columns) - 1

    S = [['∅'] * n]
    G = [['?'] * n]

    for _, row in df.iterrows():
        x = row[:-1].tolist()
        y = row['Result']

        # =========================
        # POSITIVE EXAMPLE
        # =========================
        if y == 'Yes':
            # Remove inconsistent hypotheses from G
            G = [g for g in G if is_consistent(g, x)]

            # Generalize S minimally
            for s in S:
                for i in range(n):
                    if s[i] == '∅':
                        s[i] = x[i]
                    elif s[i] != x[i]:
                        s[i] = '?'

        # =========================
        # NEGATIVE EXAMPLE
        # =========================
        else:
            new_G = []

            for g in G:
                if is_consistent(g, x):
                    for i in range(n):
                        if g[i] == '?':
                            values = df.iloc[:, i].unique()

                            for val in values:
                                if val != x[i]:
                                    new_h = g.copy()
                                    new_h[i] = val

                                    # Must be more general than S
                                    valid = True
                                    for j in range(n):
                                        if S[0][j] != '∅' and new_h[j] != '?' and new_h[j] != S[0][j]:
                                            valid = False
                                            break

                                    if valid:
                                        new_G.append(new_h)
                else:
                    new_G.append(g)

            G = new_G

        # Cleanup
        G = remove_duplicates(G)

    return S, G