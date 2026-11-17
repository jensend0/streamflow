import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    # Read the CSV file
    data = np.genfromtxt(
        filename, delimiter=",", skip_header=1, dtype=str
    )

    # Slice the array
    x = data[:, 0].astype("datetime64[m]")
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


def summarize(dates, flows, sites):
    # Excel check for 10163000: max = 131 cfs, average = 57 cfs
    print(f"{'Gauge':<12}{'Max (cfs)':>10}   {'Date of max':<16}{'Min (cfs)':>10}{'Avg (cfs)':>10}")

    with open("streamflow_summary.csv", "w") as file:
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

        for i, site in enumerate(sites):
            gauge_flows = flows[:, i]
            max_index = np.argmax(gauge_flows)
            max_flow = np.max(gauge_flows)
            max_date = np.datetime_as_string(dates[max_index], unit="m")
            min_flow = np.min(gauge_flows)
            avg_flow = np.mean(gauge_flows)

            print(
                f"{site:<12}{max_flow:>10.1f}   {max_date:<16}"
                f"{min_flow:>10.1f}{avg_flow:>10.1f}"
            )
            file.write(
                f"{site},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n"
            )


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
x, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(x, flows, sites)
summarize(x, flows, sites)