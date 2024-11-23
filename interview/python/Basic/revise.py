import os
import json


class Practice():
    def __init__(self, q_type):
        self.q_type = q_type
        self.base_dir = os.path.dirname(__file__)
        self.q_source_file = os.path.join(self.base_dir, self.q_type + ".json")
        if os.path.exists(self.q_source_file):
            self.practice_dir = self.create_practice_dir()
            self.create_practice_bundle()
        else:
            print(f"Unable to find {self.q_source_file}")

    def create_practice_dir(self):
        postfix = 1
        practice_root_dir = ''
        while True:
            practice_root_dir = os.path.join(
                self.base_dir, f'practice_{self.q_type}_{postfix}')
            if not os.path.isdir(practice_root_dir):
                os.mkdir(practice_root_dir)
                break
            else:
                postfix += 1

        return practice_root_dir

    def get_questions_from_file(self):
        questions = []
        with open(self.q_source_file, 'r') as f:
            questions = json.load(f)
        return questions

    def create_practice_file(self, file_name, content):
        new_q_file = os.path.join(self.practice_dir, file_name)
        with open(new_q_file, "a+") as f:
            f.write("'''\n")
            f.write(content)
            f.write("'''\n")

    def create_question_content(self, question_obj):

        q_num = question_obj.get("q_num", "")
        q_type = question_obj.get("type", "")
        q_subtype = question_obj.get("sub_type", "")
        q_description = question_obj.get("description", "")
        q_example = question_obj.get("example", "")
        q_sol_at = question_obj.get("solution", "")
        q_ref = os.path.join(self.base_dir, q_sol_at)

        q_str = f"""
Type: {q_type} - {q_subtype}

{q_num}. {q_description}

{q_example}

Solution @ file://{q_ref}
"""
        return q_str

    def create_practice_bundle(self):
        for question in self.get_questions_from_file():
            q_contents = self.create_question_content(question)
            q_file_name = question["type"]+str(question["q_num"])+".py"

            self.create_practice_file(q_file_name, q_contents)

    def get_readable(self):
        questions = self.get_questions_from_file()
        new_file_name = os.path.join(self.base_dir, self.q_type + "__")
        with open(new_file_name, "a+") as f:
            f.write("'''\n")
            for q in questions:
                f.write(f"{q['q_num']}. {q['description']}")
                f.write(f"file://{self.base_dir}/{q['solution']}")
                f.write("\n\n\n")


if __name__ == "__main__":

    Practice("ds")

    Practice("algo")
