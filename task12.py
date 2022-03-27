from functools import reduce

def repeat_word():
    sentences = ['капитан джек воробей', 'капитан дальнего плавания',
                 'ваша лодка готова, капитан']
    capt_count = reduce(lambda x, y: x + y.count('капитан'), sentences, 0)
    print(capt_count)

if __name__ == '__main__':
    repeat_word()
