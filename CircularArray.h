#ifndef CircularArray_h
#define CircularArray_h

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
  int size;


public:
  CircularArray(int s) {
    size = s;
    elems = new T[size];
    for(int i = 0; i < size; i++) {
      elems[i] = 0;
    }
    start = 0;
    index = 0;
    end = 0;
  };

  ~CircularArray() {
    delete elems;
  }

  T& operator[](int index) {
    return elems[index];
  }

  void operator=(T temp) {
    for(int i = 0; i < size; i++) {
      elems[i] = temp;
    }
  }

  T& next() {
    return elems[index++];
  }

  void put(T temp) {
    elems[index++] = temp;
  }

};

#endif
