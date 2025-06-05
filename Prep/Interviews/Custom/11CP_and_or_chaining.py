'''
Build out a search functionality for a service catalog. A service catalog in this case is a list of service objects which contain the following fields:
- ID
- Name
- Description
- Label

The function should allow the user to search through any combination of these fields excluding ID. The fields to filter on will be a list of fields, values, and operations. Assume that the filter input will always be valid.
'''

import json
from enum import Enum
from time import time
from typing import Dict, List

ID = '_id'
NAME = '_name'
DESCRIPTION = '_description'
LABEL = '_label'


class Op(Enum):
    AND = 'and'
    OR = 'or'


class Service:
    def __init__(self, id: str, name: str, description: str, label: str):
        self.id = id
        self.name = name
        self.description = description
        self.label = label

    def to_json(self) -> str:
        return {
            ID: self.id,
            NAME: self.name,
            DESCRIPTION: self.description,
            LABEL: self.label,
        }


class Solution:
    def _contains(self, term: str, field: str, service: Service) -> bool:
        if field == NAME:
            return term in service.name
        elif field == DESCRIPTION:
            return term in service.description
        elif field == LABEL:
            return term in service.label
        else:
            return False

    def _and_chain(self, prev_bool: bool, curr_bool: str) -> bool:
        return prev_bool and curr_bool

    def _or_chain(self, prev_bool: bool, curr_bool: str) -> bool:
        return prev_bool or curr_bool

    def keep_service(self, service: Service, filter_on: List[str]) -> bool:
        OPS = {Op.AND, Op.OR}
        FIELDS = {NAME, DESCRIPTION, LABEL}
        # For building filter mapping
        OP = '_op'
        FIELD = '_field'
        f_map = {}
        # Combined boolean result
        res = None
        for f in filter_on:
            if f in OPS:
                f_map[OP] = f
            elif f in FIELDS:
                f_map[FIELD] = f
            elif OP in f_map and f_map[OP] == Op.AND:
                # Value found, compute AND chain
                res = self._and_chain(
                    res, self._contains(f, f_map[FIELD], service)
                )
            elif OP in f_map and f_map[OP] == Op.OR:
                # Value found, compute OR chain
                res = self._or_chain(
                    res, self._contains(f, f_map[FIELD], service)
                )
            else:
                # Value found, compute boolean
                res = self._contains(f, f_map[FIELD], service)

        return res

    def search(
        self, services: List[Service], filter_on: List[str]
    ) -> List[Dict]:
        res = []
        for service in services:
            # Decide whether to keep service or not
            if self.keep_service(service, filter_on):
                res.append(service.to_json())

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(json.dumps(self.search(*case), indent=2))
                else:
                    self.search(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            [
                Service('001', 'name-001', 'description-001', 'label-001'),
                Service('002', 'name-002', 'description-002', 'label-002'),
                Service('003', 'name-003', 'description-003', 'label-003'),
            ],
            [NAME, '001'],
        ),
        (
            [
                Service('001', 'name-001', 'description-001', 'label-001'),
                Service('002', 'name-002', 'description-002', 'label-002'),
                Service('003', 'name-003', 'description-003', 'label-003'),
            ],
            [NAME, '01', Op.AND, DESCRIPTION, '02'],
        ),
        (
            [
                Service('001', 'name-001', 'description-001', 'label-001'),
                Service('002', 'name-002', 'description-002', 'label-002'),
                Service('003', 'name-003', 'description-003', 'label-003'),
            ],
            [NAME, '01', Op.OR, DESCRIPTION, '02'],
        ),
        (
            [
                Service('001', 'name-001', 'description-001', 'label-001'),
                Service('002', 'name-002', 'description-002', 'label-002'),
                Service('003', 'name-003', 'description-003', 'label-003'),
            ],
            [NAME, '01', Op.AND, DESCRIPTION, '02', Op.OR, LABEL, 'label'],
        ),
    ]
    test.quantify(test_cases)
