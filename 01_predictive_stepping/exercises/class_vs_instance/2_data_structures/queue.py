#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to back

    def dequeue(self):
        if self.items:
            return self.items.pop(0)  # Remove from front
        return None

    def peek(self):
        if self.items:
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0


# Create a queue instance
print_jobs = Queue()

# Enqueue some print jobs
print_jobs.enqueue("CV")
print_jobs.enqueue("Resumé")
print_jobs.enqueue("Portfolio")

# Process & print a couple of jobs
print_jobs.dequeue()
print_jobs.dequeue()

# Peek at the current print  job
current_job = print_jobs.peek()

# Final state of the printer queue
print("Next job:", current_job)
print("Remaining jobs:", print_jobs.items)


# Create a queue instance
internet_requests = Queue()

# Enqueue some page navigations
internet_requests.enqueue("duckduckgo.com")
internet_requests.enqueue("emergingtalent.mit.edu")
internet_requests.enqueue("badgerbadgerbadger.com")
internet_requests.enqueue("youtube.com")
internet_requests.enqueue("moc.com")

# Process & navigate to a couple of sites
internet_requests.dequeue()
internet_requests.dequeue()
internet_requests.dequeue()

# Peek at the current request
current_site = internet_requests.peek()

# Final state of the internet requests queue
print("Next Site:", current_site)
print("Remaining jobs:", internet_requests.items)
