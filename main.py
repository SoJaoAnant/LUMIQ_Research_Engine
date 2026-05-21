from agent.graphs import graph


def main():
    query = input("Enter your research query: ")

    initial_state = {
        "query": query,
        "search_results": [],
        "scraped_contents": [],
        "final_report": "",
        "logs": []
    }

    final_state = None

    print("\n======== AGENT LOGS ========\n")

    for event in graph.stream(initial_state):

        for node_name, state in event.items():

            final_state = state

            latest_logs = state.get("logs", [])

            # Print only the newest log
            if latest_logs:
                print(latest_logs[-1])

    print("\n======== DONE ========\n")

    if final_state:
        print(final_state.get("final_report", ""))

    print("\nReport generated successfully!")


if __name__ == "__main__":
    main()