import queue


def main(filename, part2=True) -> int:
    trail = open(filename).read().strip()
    crawler = queue.Queue(maxsize:=14 if part2 else 4)
    grab, drop, crumbs = lambda crumb: crawler.put(crumb), lambda: crawler.get(), lambda: crawler.queue
    [grab(crumb) for crumb in trail[:maxsize]]
    
    for step, crumb in enumerate(trail):
        unique = True
        for _ in range(maxsize):
            if (inspect := drop()) in crumbs():
                unique = False
            grab(inspect)
        if unique:
            return step
        drop()
        grab(crumb)

filepath = "2022/resources/input_6.txt"
print(f'part1: {main(filepath, False)} \n'
      f'part2: {main(filepath)}')