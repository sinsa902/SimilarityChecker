class SimilarityChecker:
    def __init__(self):
        self.char_score = 0
        self.len_score = 0
        self.score = 0

    def getScore(self):
        return self.score

    def run(self, param):
        self._set_inputs(param)
        self._calc_and_update_len_score()
        self._calc_and_update_char_score()
        self._update_total_score()

    def _calc_and_update_len_score(self):
        max_len = max(len(self.input1), len(self.input2))
        min_len = min(len(self.input1), len(self.input2))

        if max_len >= min_len * 2:
            self.len_score = 0
            self.invalid = True
            return

        gap = max_len - min_len
        self.len_score = (1 - gap / min_len) * 60

    def _calc_and_update_char_score(self):
        self.char_score = 40

    def _update_total_score(self):
        self.score = 0
        if self.invalid:
            self.score = 0
            return
        self.score = self.len_score + self.char_score

    def _set_inputs(self, param):
        self.invalid = False
        self.input1 = param[0]
        self.input2 = param[1]
