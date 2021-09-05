# Chapter06-05
# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# Futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL(Global Interface Lock) : 두 개 이상의 스레드가 동시에 실행 될 때, 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
# GIL이 실행됨, 리스스 전체에 lock이 걸린다 -> Context Switch(문맥 교환)
# GIL : 멀티프로세싱 사용, CPython 이용

from concurrent import futures
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [40000, 4000000, 400000, 40000000] # 안에 함수 넣어도 됨

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)

def sum_generator(n):
    return sum(n for n in range(n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # start time
    start_time = time.time()
    # Futures
    futures_list = []

    result = []
    # 결과 건수
    # ProcessPoolExecutor or ThreadPoolExecutor 둘다 가능
    with ProcessPoolExecutor() as excutor:
        # map -> 작업 순서를 유지하고 즉시 실행
        # result = excutor.map(sum_generator, WORK_LIST)
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print("Scheduled for {} : {}".format(work, future))
            print()
        
        # # wait 결과 출력
        # result = wait(futures_list, timeout = 2)
        # # 성공
        # print('Completed Task: ' + str(result.done))
        # # 실패
        # print('Pending ones after waiting for 2sec: ' + str(result.not_done))
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result(all)
            done = future.done()
            cancelled = future.cancelled()

        # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))


    # time taken
    taken_time = time.time() - start_time
    msg = '\n Time : {:.2f}s'

    print(msg.format(taken_time))


# 실행
if __name__ == '__main__':
    main()