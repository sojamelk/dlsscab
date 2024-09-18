import random
import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dlsscab():
    while True:
        user_name = ""
        user_score = 0
        ai_score = 0
        if user_name == "":
            slow_print('진행자 : 잠시만요! \'dlsscap\'게임을 시작하기 전 닉네임 선택 및 설명은 필수입니다.', 0.05)
            slow_print('진행자 : 만약 dlsscap 게임에 경험이 있다면 닉네임을 정하신 후, \'스킵\'하셔도 상관없습니다.', 0.05)
            user_name = input('진행자 : 닉네임을 정해주세요. : ')
            user_skip = input('진행자 : 스킵하실 기회입니다. : ')
            while True:
                if user_skip == '스킵':
                    while True:
                        if user_score == 2:
                            slow_print('진행자 : 유저 최종적 승리!', 0.05)
                            return
                        elif ai_score == 2:
                            slow_print('진행자 : AI 최종적 승리!', 0.05)
                            return
                        user_choice = input('진행자 : 가위바위보를 통해 순서를 정하세요 (예시 : 가위, 바위, 보, 설명, 나가기): ')
                        if user_choice not in ['가위', '바위', '보', '설명', '나가기']:
                            slow_print('진행자 : 잘못된 문구입니다. (예시 : 가위, 바위, 보, 나가기)', 0.05)
                        elif user_choice in ['가위', '바위', '보']:
                            ai_choice = random.choice(['가위', '바위', '보'])
                            slow_print(f'AI = {ai_choice}', 0.05)
                            if (user_choice, ai_choice) in [('가위', '보'), ('바위', '가위'), ('보', '바위')]:
                                slow_print(f'진행자 : 가위바위보의 결과로 \'{user_name}\'유저가 기회를 얻습니다.', 0.05)
                                x = random.randint(1, 10)
                                try:
                                    user_choice2 = int(input('선정할 숫자를 입력하세요 (1, 10) : '))
                                    if x == user_choice2:
                                        slow_print('진행자 : 유저 1승!', 0.05)
                                        user_score += 1
                                    else:
                                        slow_print(f'진행자 : 맞춰진 값은 {x}이며, 맞지 않았기에 다시 가위바위보를 합니다.', 0.05)
                                except ValueError:
                                    slow_print('진행자 : 숫자를 입력해주세요.', 0.05)
                            elif (ai_choice, user_choice) in [('가위', '보'), ('바위', '가위'), ('보', '바위')]:
                                slow_print('진행자 : 가위바위보의 결과로 AI가 기회를 얻습니다.', 0.05)
                                x = random.randint(1, 10)
                                ai_choice2 = random.randint(1, 10)
                                slow_print(f'AI의 선택 : {ai_choice2}', 0.05)
                                if x == ai_choice2:
                                    slow_print('진행자 : AI 1승!', 0.05)
                                    ai_score += 1
                                else:
                                    slow_print(f'진행자 : 맞춰진 값은 {x}이며, 맞지 않았기에 다시 가위바위보를 합니다.', 0.05)
                            elif ai_choice == user_choice:
                                slow_print('진행자 : 가위바위보가 비겼습니다. 다시 가위바위보를 하여 결정권을 가집니다.', 0.05)
                        elif user_choice == '나가기':
                            slow_print('진행자 : AI 판정 승', 0.05)
                            return
                        else:
                            slow_print('system : 잘못된 길입니다!', 0.05)
                            return
                else:
                    slow_print(f'진행자 : dlsscab에 오신 {user_name} 유저분 진심으로 환영합니다!', 0.05)
                    slow_print('진행자 : dlsscab은 개발자의 이름의 일부분을 영어로 옮긴 dls를 딱지치기 scab에 붙인 말입니다.', 0.05)
                    slow_print('진행자 : 게임은 3전 2선승제이며, 룰은 다음과 같습니다.', 0.05)
                    slow_print('진행자 : 가위바위보로 ai와 유저중 누가 먼저할지를 고른 후, 해당 순서인 결정자가 숫자를 선택,', 0.05)
                    slow_print('진행자 : 만약 선택된 숫자가 정해진 숫자와 같은 시, 그 결정자가 승리. 아닐경우 순서는 가위바위보로 다시 결정합니다.', 0.05)
                    slow_print('진행자 : 이 룰로 반복이 될것이며, 끝날 시 게임은 자동적으로 마무리됩니다.', 0.05)
                    slow_print('진행자 : 그럼 행운을 빕니다.', 0.05)
                    user_skip = '스킵'
                    continue

dlsscab()
