// #include "CircularArray.h"
#include <iostream>
#include <iomanip>

using namespace std;


template<class T>
class CircularArray {

private:
  T *elems;
  int start;
  int index;
  int end;
  int num_elems;
  int size;

public:
  CircularArray()
  {
    size = 10;
    elems = new T[size];
    start = 0;
    index = 0;
    end = -1;
    num_elems = 0;
  };

  ~CircularArray()
  {
    delete elems;
  }

  void push(T temp)
  {
    if(end == start) {
// you are trying to put an element into a full array
// so put the array into a bigger array
      int i, nsize;
      nsize = size*2;
      T *nelems = new T[nsize];
      for(i = 0; i < nsize; i++) {
        nelems[i] = 0;
      }
      i = start;
      j = 0;
      for(i = 0; i < size; i++) {
        nelems[i] = elems[(i+start)%size];
      }
      elems = nelems;
      start = 0;
      end = size;
      size = nsize;
    }
    if(end < 0) {
      end = 0;
    }
    elems[end] = temp;
    end = (end+1)%size;
    num_elems++;
  }

  T& pop()
  {
    if(end < 0) {
      // the array is empty, so return null
      return NULL;
    }
    int i = start;
    start = (start+1)%size;
    if(start == end) {
      // this pop empties the array, so mark it as such
      end = -1;
      start = 0;
      index = 0;
    }
    num_elems--;
    return elems[i];
  }

  T& next()
  {
    int i = index;
    index = (index+1)%size;
    if(index == end) {
      index = start;
    }
    return elems[i];
  }

  T& operator[](int ind) {
    ind = (start+ind)%size;
    return elems[ind];
  }

  int size() {
    return num_elems;
  }

};

int main() {

  CircularArray<int> carr(n);

  for(i = 0; i < carr.size(); i++) {
    cout << carr[i] << ' ';
  }
  cout << '\n';

  // for (auto i : v) // access by value, the type of i is int
  //       std::cout << i << ' ';
  //   std::cout << '\n';

  return 0;
}
