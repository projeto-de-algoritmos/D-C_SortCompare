import numpy
from matplotlib.pylab import *
import matplotlib.animation as animation
import random
import time

# insertionsort
def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
  
        while(i >= 0 and a[i] > key):
            a[i+1] = a[i]
            i -= 1
  
            # yield the current position
            # of elements in a
            yield a
        a[i+1] = key
        yield a

# quicksort
def quicksort(a, l, r):
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[l], a[j]= a[j], a[l]
    yield a
 
    yield from quicksort(a, l, j-1)
    yield from quicksort(a, j + 1, r)

# mergeSort
def mergesort(A, start, end):
    if end <= start:
        return
  
    mid = start + ((end - start + 1) // 2) - 1
      
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)

def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1
  
    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1
  
    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1
  
    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1
  
    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A

# BubbleSort
def bubblesort(A):
	swapped = True
	
	for i in range(len(A) - 1):
		if not swapped:
			return
		swapped = False
		
		for j in range(len(A) - 1 - i):
			if A[j] > A[j + 1]:
				A[j], A[j+1] = A[j+1], A[j]
				swapped = True
			yield A

N = 50

A = list(range(1, N + 1))
random.shuffle(A)
B = A.copy()
C = A.copy()
D = A.copy()


# Setup figure and subplots
f0 = subplots(figsize = (12, 8))
# f0.suptitle("Comparador de Ordenadores", fontsize=12)
ax01 = subplot(4, 1, 1)
ax01.set_title('BubbleSort')
ax01.set_xlim(0, N)
ax01.set_ylim(0, N+3)
text01 = ax01.text(0.01, 0.85, "", transform=ax01.transAxes)
bars1 = ax01.bar(range(len(A)), A, align="edge")
n01 = [0]


ax02 = subplot(4, 1, 2)
ax02.set_title('MergeSort')
ax02.set_xlim(0, N)
ax02.set_ylim(0, N+3)
text02 = ax02.text(0.01, 0.85, "", transform=ax02.transAxes)
bars2 = ax02.bar(range(len(B)), B, align="edge")
n02 = [0]

ax03 = subplot(4, 1, 3)
ax03.set_title('Quick Sort')
ax03.set_xlim(0, N)
ax03.set_ylim(0, N+3)
text03 = ax03.text(0.01, 0.85, "", transform=ax03.transAxes)
bars3 = ax03.bar(range(len(C)), C, align="edge")
n03 = [0]

ax04 = subplot(4, 1, 4)
ax04.set_title('Insertion Sort')
ax04.set_xlim(0, N)
ax04.set_ylim(0, N+3)
text04 = ax04.text(0.01, 0.85, "", transform=ax04.transAxes)
bars4 = ax04.bar(range(len(D)), D, align="edge")
n04 = [0]

tight_layout()

def update(arr, rects, iteration, text):
    et = time.time()
    for rect, val in zip(rects, arr):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"operations: {iteration[0]}, time: {round(et-st, 2)}")

st = time.time()

anim = animation.FuncAnimation(
    f0[0],
    func=update,
    fargs=(bars1, n01, text01),
    frames=bubblesort(A),
    repeat=False,
    blit=False,
    interval=80,
)

asd = animation.FuncAnimation(
    f0[0],
    func=update,
    fargs=(bars2, n02, text02),
    frames=mergesort(B, 0, N-1),
    repeat=False,
    blit=False,
    interval=80,
)

qwe = animation.FuncAnimation(
    f0[0],
    func=update,
    fargs=(bars3, n03, text03),
    frames=quicksort(C, 0, N-1),
    repeat=False,
    blit=False,
    interval=80,
)

wer = animation.FuncAnimation(
    f0[0],
    func=update,
    fargs=(bars4, n04, text04),
    frames=insertionsort(D),
    repeat=False,
    blit=False,
    interval=80,
)

plt.show()
