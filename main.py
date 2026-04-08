import json
import os
import sys

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = int(answer)

    def display(self, index):
        print(f"\n문제 {index}. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}) {choice}")

    def is_correct(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

class QuizGame:
    def __init__(self):
        self.file_path = "state.json"
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def load_data(self):
        default_quizzes = [
            {"question": "리눅스나 터미널 환경에서 파일을 다른 디렉토리로 이동시키거나 이름을 변경할 때 사용하는 명령어는?", "choices": ["cp", "rm", "ls", "mv"], "answer": 4},
            {"question": "현재 디렉토리 내의 모든 파일과 하위 폴더를 포함하여 강제로 삭제하고 싶을 때 사용하는 명령어로 가장 적절한 것은 무엇인가?", "choices": ["cp -a", "rm -rf*", "mkdir -p", "dekete --all"], "answer": 2},
            {"question": "Docker에서 이미지를 기반으로 새로운 컨테이너를 생성하고 실행하는 명령어는 무엇인가?", "choices": ["docker run", "docker build", "docker pull", "docker ps"], "answer": 1},
            {"question": "SGitHub와 같은 원격 저장소에 로컬에서 작업한 커밋(Commit) 내역을 업로드할 때 사용하는 Git 명령어는 무엇인가?", "choices": ["git clone", "git pull", "git push", "git commit"], "answer": 3},
            {"question": "Git에서 새로운 변경 사항을 스테이징 영역(Staging Area)에 추가하기 위해 사용하는 명령어는 무엇인가?", "choices": ["git init", "git checkout", "git add", "git status"], "answer": 3}
        ]

    def play_game(self):
        if not self.quizzes:
            print("\n출제할 문제가 없습니다. 문제를 추가해주세요.")
            return

        score = 0
        print("\n--- 퀴즈를 시작합니다! ---")
        for i, q in enumerate(self.quizzes, 1):
            q.display(i)
            ans = self.safe_input("정답 번호 입력: ", 1, 4)
            if q.is_correct(ans):
                print("정답입니다!")
                score += 1
            else:
                print(f"틀렸습니다. 정답은 {q.answer}번입니다.")

        print(f"\n최종 점수: {score} / {len(self.quizzes)}")
        if score > self.best_score:
            print(f"축하합니다! 최고 기록 달성 (이전: {self.best_score})")
            self.best_score = score
            self.save_data()

    def run(self):
        while True:
            print("\n===== 퀴즈 게임 메뉴 =====")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 등록")
            print("3. 퀴즈 목록")
            print("4. 최고 점수 확인")
            print("5. 종료")
            print("==========================")
            
            choice = self.safe_input("메뉴 선택: ", 1, 5)
            
            if choice == 1: self.play_game()
            elif choice == 2: self.add_quiz()
            elif choice == 3: self.show_list()
            elif choice == 4: self.show_best_score()
            elif choice == 5:
                print("게임을 종료합니다.")
                self.save_data()
                break       