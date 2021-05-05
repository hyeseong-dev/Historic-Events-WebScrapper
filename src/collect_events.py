from tqdm import tqdm
import os as _os
import json as _json
import time as _time
from typing import Iterator, Dict
import datetime as _dt

import scraper as _scraper


def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    for n in tqdm(range(int((end_date - start_date).days)), desc='진행율'):
        yield start_date + _dt.timedelta(n)


def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for date in _date_range(start_date, end_date):
        
        month = date.strftime('%B').lower()
        if month not in events:
            events[month] = dict()
        events[month][date.day] = _scraper.events_of_the_day(month, date.day)

    return events


if __name__ == '__main__':
    _os.makedirs('result', exist_ok=True)
    events = create_events_dict()
    with open('./result/events.json', mode='w', encoding='utf-8-sig') as events_file:
        _json.dump(events, events_file, ensure_ascii=False)
