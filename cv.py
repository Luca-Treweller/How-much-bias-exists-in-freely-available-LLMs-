import fake_names as fn


class CV:
    def __init__(
            self, body: str, 
            name: list[str],
            fake_names = fn.name_list,
            experiance_adaptation: int = 0, 
            experiance = None,
            fake_experiance = None,
        ):
        self.body = body
        self.name = name
        self.fake_names = fake_names
        self.name_mapping = fn.name_mapping
        self.experiance_adaptation = experiance_adaptation # 0 = by lines, 1 = by words
        self.experiance = experiance
        #example experiance as lines = [(5, 10), (14, 20)]
        #example experiance as words = ["5 years", "2020"]
        self.fake_experiance = fake_experiance
        #important: list ordered in reverse appearance
        #example fake_experiance as lines = [["2020:\nfinished school", "2024:\nfinished university"]]
        #example fake_experiance as words = [["1 year", "2023"]]

    def create_version(self, name: int, experiance: int):
        new_body = self.body
        experiance = None if experiance == 0 else experiance - 1
        if name != None:
            new_body = self.replace_name(name, new_body)
        if experiance != None:
            new_body = self.replace_experiance(experiance, new_body)
        return new_body

    def replace_name(self, new_name: int, body = None):
        if body is None:
            body = self.body
        new_body = body.replace(self.name[0], self.fake_names[new_name][0])
        new_body = new_body.replace(self.name[1], self.fake_names[new_name][1])
        return new_body

    def replace_experiance(self, new_experiance: int, body = None):
        if body is None:
            body = self.body
        if self.experiance_adaptation == 0:
            new_body = body
            for i, (start, end) in enumerate(self.experiance[new_experiance]):
                if len(self.fake_experiance[new_experiance]) - 1  < i:
                    break
                lines = new_body.split('\n')
                new_lines = lines.copy()
                new_lines[start] = self.fake_experiance[new_experiance][i]
                for i in range(start + 1, end):
                    new_lines.remove(lines[i])
                new_body = '\n'.join(new_lines)
        elif self.experiance_adaptation == 1:
            new_body = body
            for i, word in enumerate(self.experiance[new_experiance]):
                new_body = new_body.replace(word, self.fake_experiance[new_experiance][i])
        return new_body
    

    def __str__(self):
        return self.body
