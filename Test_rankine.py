from rankine import rankine

def main():
    # Test Case 1: p_high=8000kPa, p_low=8kPa, x1=1
    rankine_cycle_1 = rankine(p_high=8000, p_low=8, name='Rankine Cycle 1')
    efficiency_1 = rankine_cycle_1.calc_efficiency()

    # Test Case 2: p_high=8000kPa, p_low=8kPa, T1=1.7⋅Tsat
    rankine_cycle_2 = rankine(p_high=8000, p_low=8, t_high=None, name='Rankine Cycle 2')
    efficiency_2 = rankine_cycle_2.calc_efficiency()

    # Print results for Test Case 1
    print("Results for Rankine Cycle 1:")
    print("Efficiency:", efficiency_1)
    rankine_cycle_1.print_summary()

    # Print results for Test Case 2
    print("\nResults for Rankine Cycle 2:")
    print("Efficiency:", efficiency_2)
    rankine_cycle_2.print_summary()

if __name__ == "__main__":
    main()
