import time

def countdown(func):
    def sleep_time(num_secs):
        func()
        while num_secs:
            mins, secs = divmod(num_secs, 60)
            min_sec_form = '{:02d}:{:02d}'.format(mins, secs)
            print(min_sec_form, end='\n')
            time.sleep(1)
            num_secs -= 1
        print("I'm just a function")
    return sleep_time

def say_time():
    print("Let's take up!")

if __name__ == '__main__':
    say_time = countdown(say_time)
    say_time(5)
