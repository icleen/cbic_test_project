// #include "CircularArray.h"
#include <iostream>
#include <iomanip>

using namespace std;

template<class T> class MyCircularArray {

private:
  T *elems;
  int starti;
  int endi;
  int num_elems;
  int size;


  class Iterator {
    T* data;
    int index;
    int size;
  public:
    Iterator(T* _data, int _index, int _size) {
        data = _data;
        index = _index;
        size = _size;
      }

    T& operator*() {
      return data[index];
    }

    Iterator& operator++() {
      index = (index+1)%size;
      return *this;
    }

    bool operator!=(const Iterator& it) const {
      return index != it.index;
    }

  };


public:
  MyCircularArray()
  {
    size = 5;
    elems = new T[size];
    starti = 0;
    endi = -1;
    num_elems = 0;
  };

  ~MyCircularArray()
  {
    delete elems;
  }

  Iterator begin() {
    return {elems, starti, size};
  }

  Iterator end() {
    return {elems, endi, size};
  }

  void push(T temp)
  {
    if(endi == starti) {
// you are trying to put an element into a full array
// so put the array into a bigger array
      int i, nsize;
      nsize = size*2;
      T *nelems = new T[nsize];
      for(i = 0; i < nsize; i++) {
        nelems[i] = 0;
      }
      i = starti;
      for(i = 0; i < size; i++) {
        nelems[i] = elems[(i+starti)%size];
      }
      elems = nelems;
      starti = 0;
      endi = size;
      size = nsize;
    }
    if(endi < 0) {
      endi = 0;
    }
    elems[endi] = temp;
    endi = (endi+1)%size;
    num_elems++;
  }

  T& pop()
  {
    if(endi < 0) {
      // the array is empty, so return null
      return elems[0];
    }
    int i = starti;
    starti = (starti+1)%size;
    if(starti == endi) {
      // this pop empties the array, so mark it as such
      endi = -1;
      starti = 0;
    }
    num_elems--;
    return elems[i];
  }

  T& operator[](int ind)
  {
    ind = (starti+ind)%size;
    return elems[ind];
  }

  int length()
  {
    return num_elems;
  }

  void print_arr()
  {
    for(int i = 0; i < size; i++) {
      cout << elems[i] << ' ';
    }
    cout << '\n';
  }

  void printElements()
  {
    if(num_elems < 1) {
      cout << "Empty\n";
      return;
    }
    for(int i = 0; i < num_elems; i++) {
      cout << elems[(i+starti)%size] << ' ';
    }
    cout << '\n';
  }

};

int main() {

  MyCircularArray<char> carr;

  cout << "test simple push\n";
  carr.push('a');
  carr.print_arr();
  carr.printElements();

  cout << "test push to full\n";
  carr.push('b');
  carr.push('c');
  carr.push('d');
  carr.push('e');
  carr.print_arr();
  carr.printElements();

  cout << "test simple pop\n";
  carr.pop();
  carr.print_arr();
  carr.printElements();

  cout << "test push/pop\n";
  carr.push('f');
  carr.pop();
  carr.print_arr();
  carr.printElements();

  cout << "test rearrange\n";
  carr.pop();
  carr.pop();
  carr.push('g');
  carr.push('h');
  carr.push('a');
  carr.pop();
  carr.pop();
  carr.pop();
  carr.pop();
  carr.push('b');
  carr.push('c');
  carr.print_arr();
  carr.printElements();

  cout << "test overfill\n";
  carr.push('d');
  carr.push('e');
  carr.print_arr();
  carr.printElements();
  carr.push('f');
  carr.push('g');
  carr.push('h');
  carr.print_arr();
  carr.printElements();

  cout << "test empty\n";
  carr.pop();
  carr.pop();
  carr.pop();
  carr.pop();
  carr.pop();
  carr.pop();
  carr.pop();
  carr.pop();
  carr.print_arr();
  carr.printElements();

  cout << "test refill\n";
  carr.push('x');
  carr.push('y');
  carr.push('z');
  carr.print_arr();
  carr.printElements();

  cout << "test range for loop\n";
  for (auto item : carr) // access by value, the type of i is int
    std::cout << item << ' ';
  std::cout << '\n';

  cout << "End of Program\n";

  return 0;
}
/*
I test my system by testing the simple cases of push and pop,
as well as testing wether it can handle a series of pushes and
pops that would put the elements in random positions within the
underlying array. I also test how it deals with an empty array
as well as how it does when I push too much data into it
(it handles this by copying the data into a larger underlying array).
The class could further be tested by checking how it deals with other
data classes, bound testing, white/black box testing, etc.
I am showing how the array works above by printing out the results twice.
The first prints out the entire underlying array, while the second only
prints out the elements that are supposed to be on the array. Note that
I never bother changing any of the values when I pop, but instead just
leave them, so when I call print_arr it shows the elements that have
been popped but not overwritten.
*/
