import personalprject
import create_graph

if __name__ == '__main__':
    pop_size_dict = personalprject.csv_demographic_scorer('citydataset.csv')
    demographic_dict = personalprject.csv_demographic_scorer('citydataset.csv')
    gdp_dict = personalprject.csv_gdp_scorer('citydataset.csv')
    temp_dict = personalprject.csv_temp_scorer('citydataset.csv')
    sunny_dict = personalprject.csv_sunny_scorer('citydataset.csv')
    young_dict = personalprject.csv_young_people_scorer('citydataset.csv')
    tourism_dict = personalprject.csv_tourism_scorer('citydataset.csv')
    density_dict = personalprject.csv_density_scorer('citydataset.csv')
    crime_dict = personalprject.csv_crimerate_scorer('citydataset.csv')
    water_access_dict = personalprject.csv_water_access_scorer('citydataset.csv')
    college_dict = personalprject.csv_college_ed_scorer('citydataset.csv')
    religiousity_dict = personalprject.csv_religiousity_scorer('citydataset.csv')

    accumulator_dict = {}
    for ele in demographic_dict:
        accumulator_dict[ele] = demographic_dict[ele]
    for ele in pop_size_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += pop_size_dict[ele]
    for ele in gdp_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += gdp_dict[ele]
    for ele in temp_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += temp_dict[ele]
    for ele in sunny_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += sunny_dict[ele]
    for ele in young_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += young_dict[ele]
    for ele in tourism_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += tourism_dict[ele]
    for ele in density_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += density_dict[ele]
    for ele in crime_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += crime_dict[ele]
    for ele in water_access_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += water_access_dict[ele]
    for ele in college_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += college_dict[ele]
    for ele in religiousity_dict:
        for ele2 in accumulator_dict:
            if ele == ele2:
                accumulator_dict[ele] += religiousity_dict[ele]

    sorted_dict = personalprject.sort_dictionary(accumulator_dict)
    print(sorted_dict)
    final_dict = personalprject.dict_of_neighbours(sorted_dict, 1.0)
    print(final_dict)
    graph1 = create_graph.create_graph_and_nodes(sorted_dict)
    graph2 = create_graph.add_edges(graph1, final_dict)
    print("The city with the most edges is: " + create_graph.max_node_centrality(graph2))
    create_graph.display_graph(graph2)
