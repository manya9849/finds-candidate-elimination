from src.find_s import find_s
from src.candidate_elimination import candidate_elimination
import pandas as pd

def main():
    df = pd.read_csv("data/dataset.csv")

    h = find_s(df)
    S, G = candidate_elimination(df)

    output_lines = []

    output_lines.append("Dataset:\n" + df.to_string())
    output_lines.append("\nFind-S Hypothesis:\n" + str(h))
    output_lines.append("\nSpecific Boundary (S):\n" + str(S))

    output_lines.append("\nGeneral Boundary (G):")
    for g in G:
        output_lines.append(str(g))

    # Write to file
    with open("results/output.txt", "w") as f:
        for line in output_lines:
            f.write(line + "\n")

    # Also print (optional)
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()