with open('input.txt', 'r') as f:
    data = f.read().replace('seeds: ', '').replace('seed-to-soil map:\n', '').replace('soil-to-fertilizer map:\n', '').replace('fertilizer-to-water map:\n', '').replace('water-to-light map:\n', '').replace('light-to-temperature map:\n', '').replace('temperature-to-humidity map:\n', '').replace('humidity-to-location map:\n', '').split('\n\n')
    seeds = data[0].split(' ')
    translation_sets = [data[1].split('\n'), data[2].split('\n'), data[3].split('\n'), data[4].split('\n'), data[5].split('\n'), data[6].split('\n'), data[7].split('\n')]
    
    def prepare_seeds(seeds):
        seed_ranges = []
        seed_start = 0
        seed_end = 0
        for i in range(len(seeds)):
            seeds[i] = int(seeds[i])
        for i in range(len(seeds)):
            if not (i + 1) % 2 == 0:
                seed_start = seeds[i]
            else:
                seed_end = seed_start + seeds[i]
                seed_ranges.append([seed_start, seed_end])
        return seed_ranges
    
    def prepare_translation_sets(translation_sets):
        for i in range(len(translation_sets)):
            for j in range(len(translation_sets[i])):
                translation_sets[i][j] = translation_sets[i][j].split(' ')
                for k in range(len(translation_sets[i][j])):
                    translation_sets[i][j][k] = int(translation_sets[i][j][k])
                translation_sets[i][j][2] += translation_sets[i][j][1]
        return(translation_sets)
    
    def process(seeds, translation_sets, n):
        if n == 7:
            seeds.sort()
            print(min(seeds)[0])
            return()
        ts = translation_sets[n]
        processed = []
        changed = False
        i = 0
        while i < len(seeds):
            changed = False
            for j in range(len(ts)):
                if seeds[0][0] < ts[j][1] <= ts[j][2] < seeds[0][1]:
                    changed = True
                    processed.append([ts[j][1] + (ts[j][0] - ts[j][1]), ts[j][2] + (ts[j][0] - ts[j][1])])
                    seeds.append([seeds[0][0], ts[j][1] - 1])
                    seeds.append([ts[j][2] + 1, seeds[0][1]])
                    break
                elif ts[j][1] <= seeds[0][0] <= seeds[0][1] <= ts[j][2]:
                    changed = True
                    processed.append([seeds[0][0] + (ts[j][0] - ts[j][1]), seeds[0][1] + (ts[j][0] - ts[j][1])])
                    break
                elif seeds[0][0] < ts[j][1] <= seeds[0][1] < ts[j][2]:
                    changed = True
                    seeds.append([seeds[0][0], ts[j][1] - 1])
                    processed.append([ts[j][1] + (ts[j][0] - ts[j][1]), seeds[0][1] + (ts[j][0] - ts[j][1])])
                    break
                elif ts[j][1] < seeds[0][0] <= ts[j][2] < seeds[0][1]:
                    changed = True
                    processed.append([seeds[0][0] + (ts[j][0] - ts[j][1]), ts[j][2] + (ts[j][0] - ts[j][1])])
                    seeds.append([ts[j][2] + 1, seeds[0][1]])
                    break
            if changed is False:
                processed.append(seeds[0])
            del seeds[0]
        seeds.clear()
        for j in range(len(processed)):
            seeds.append(processed[j])
        n += 1
        process(seeds, translation_sets, n)
            
    seeds = prepare_seeds(seeds)
    translation_sets = prepare_translation_sets(translation_sets)
    
    translated = []
    n = 0
    process(seeds, translation_sets, n)