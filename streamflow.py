import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    # Read the CSV file
    data = np.genfromtxt(
        filename, delimiter=",", skip_header=1, dtype=str
    )

    # Slice the array
    x = data[:, 0].astype("datetime64[D]")
    flows = data[:, 1:6].astype(float)

    return x, flows


def plot_streamflow(x, flows, sites):
    plt.figure(figsize=(12, 6))

    plt.plot(x, flows[:, 0], label=sites[0], color="purple")
    plt.plot(x, flows[:, 1], label=sites[1], color="blue")
    plt.plot(x, flows[:, 2], label=sites[2], color="green")
    plt.plot(x, flows[:, 3], label=sites[3], color="yellow")
    plt.plot(x, flows[:, 4], label=sites[4], color="orange")

    plt.title("Provo River Streamflow Data (2021)")
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")

    plt.legend(title="Site Numbers")
    plt.grid()
    plt.tick_params(axis="x", rotation=45)
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
x, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(x, flows, sites)