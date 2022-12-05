import pandas as pd
import logging
from collections import deque
import re
import copy

logging.basicConfig(filename='day5.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

def cm_9000_move(quant:int, frm_stack:deque, to_stack:deque):
    for _ in range(quant):
        to_stack.appendleft(frm_stack.popleft())

def cm_9001_move(quant:int, frm_stack:deque, to_stack:deque):
    bucket = []
    for _ in range(quant):
        bucket.append(frm_stack.popleft())
    logging.debug(bucket)
    bucket.reverse()
    logging.debug(bucket)
    to_stack.extendleft(bucket)


def manual_parse_stacks(text:str):
    rows = text.splitlines()
    logging.debug(rows)
    stack_nums = rows.pop().split()
    logging.debug(stack_nums)
    logging.debug(rows)
    # Now parse the rows into their columns
    stacks = {stack:deque() for (stack,) in stack_nums}
    logging.debug(stacks)
    for row in rows:
        for stack in stack_nums:
            num = 9 - int(stack) 
            end_idx = 35 - (num * 4)
            start_idx = end_idx - 3
            if (crate := row[start_idx:end_idx].strip()) != '':
                stacks[stack].append(crate)
        logging.debug(stacks)
    return stacks

def move_crates(crane_type:str, instruction_text:str, stacks:dict):
    instructions = instruction_text.splitlines()
    for instruction in instructions:
        logging.debug(instruction)
        instr = re.match(r'move (\d+) from (\d+) to (\d+)', 
                         instruction)
        quant, frm, to = instr.groups()
        src_stack = stacks[frm]
        to_stack = stacks[to]
        if crane_type == '9000':
            cm_9000_move(int(quant), src_stack, to_stack)
        elif crane_type == '9001':
            cm_9001_move(int(quant), src_stack, to_stack)
        logging.debug(stacks)
    return stacks

def get_top_items(stacks:dict):
     return ''.join([stack[0].replace('[', '').replace(']', '') 
                     for stack in stacks.values()])   

def get_sections(text:str):
    return text.split('\n\n')
                
with open('input.txt') as f:
    text = f.read()
sections = get_sections(text)
stacks = manual_parse_stacks(sections[0])
logging.debug('Crate Master 9000')
first_mv_stacks = move_crates('9000', sections[1], copy.deepcopy(stacks))
print(f'The top items after stage one are: {get_top_items(first_mv_stacks)}')
logging.debug('Crate Master 9001')
sec_mv_stacks = move_crates('9001', sections[1], copy.deepcopy(stacks))
print(f'The top items after stage two are: {get_top_items(sec_mv_stacks)}')