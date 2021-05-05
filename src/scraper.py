from typing import List
import requests as _requests
import bs4 as _bs4


def _generate_month_url(month: str, day: int) -> str:
    '''
    # 특정 Parameter: month, day 입력후 해당 str으로 반환
    '''
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url


def _get_page(url: str) -> _bs4.BeautifulSoup:
    '''
    입력 받은 url 파라미터를 request객체의 get요청으로 page객체 생성
    Beautifulsoup의 첫번째 매개변수로 두면서 content속성을 호출합니다.  파서는 html.parser를 사용합니다.
    '''
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def events_of_the_day(month: str, day: int) -> List[str]:
    '''
    _get_page로 받환 받은 soup객체인 page를 find_all을 통해 추출합니다.
    '''
    url = _generate_month_url(month, day)
    page = _get_page(url)
    raw_events = page.find_all('li', attrs={'class': 'event'})
    events = [event.text for event in raw_events]
    return events


events_of_the_day('february', 24)
