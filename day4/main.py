import logging

logging.basicConfig(filename='day4.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

with open('input.txt') as f:
    lines = f.read().splitlines()

couples = [tuple(tuple(map(int, elf.split('-'))) for elf in line.split(',')) for line in lines]
logging.debug(couples)
pair_count = 0
partial_count = 0
for couple in couples:
    logging.debug(couple)
    elf1, elf2 = couple
    elf1_l, elf1_r = elf1
    elf2_l, elf2_r = elf2
    if elf1_l < elf2_l:
        if elf1_r >= elf2_r:
            pair_count += 1
            partial_count += 1
            logging.debug('Found pair - elf1 contains elf2')
        elif elf1_r >= elf2_l:
            partial_count += 1
            logging.debug("Found partial overlap - elf1_r >= elf2_l")
        else:
            continue
    elif elf2_l < elf1_l:
        if elf2_r >= elf1_r:
            pair_count += 1
            partial_count += 1
            logging.debug('Found pair - elf2 contains elf1')
        elif elf2_r >= elf1_l:
            partial_count += 1
            logging.debug("Found partial overlap - elf2_r >= elf1_l")
        else:
            continue
    else:
        pair_count += 1
        partial_count += 1
        logging.debug("Found pair? Theoretically if still here and two left values are equal, then there's overlap.")
print(f'The number of pairs with a complete overlap is {pair_count}')
print(f'The number of pairs with a partial overlap is {partial_count}')

    
        