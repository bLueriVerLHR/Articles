# 设计模式

## 抽象工厂

### 目的

- 提供创建一族有关的或者有依赖关系的对象的接口
- 为不同平台生成特定一套对象以适应不同情况
  - 减少对 `#ifdef` 的使用
  - 平台指操作系统，数据库或者前端框架等
- 直接进行 `new` 比较危险

### 结构

``` plantuml
@startuml
Abstract Class1

interface  AbstractProductOne
interface  AbstractProductTwo
interface  AbstractPlatform

Class1 -down-> AbstractProductOne
Class1 -down-> AbstractProductTwo
Class1 -right-> AbstractPlatform

together {
  class PlatformOne {
    +makeProductOne()
    +makeProductTwo()
  }
  class PlatformTwo
}

PlatformOne --|> AbstractPlatform
PlatformTwo --|> AbstractPlatform

note right of PlatformOne::makeProductOne
  return new ProductOnePlatformOne();
end note

note right of PlatformOne::makeProductTwo
  return new ProductTwoPlatformOne();
end note

together {
  class ProductOnePlatformOne
  class ProductOnePlatformTwo
}

together {
  class ProductTwoPlatformOne 
  class ProductTwoPlatformTwo
}

ProductOnePlatformOne -up-|> AbstractProductOne
ProductOnePlatformTwo -up-|> AbstractProductOne
ProductTwoPlatformOne -up-|> AbstractProductTwo
ProductTwoPlatformTwo -up-|> AbstractProductTwo
@enduml
```

### 举例

``` c++
extern "C" int printf(const char *__restrict__ __format, ...);

class Shape {
public:
  Shape() { id_ = total_++; }
  virtual void draw() = 0;

protected:
  int id_;
  static int total_;
};
int Shape::total_ = 0;

class Circle : public Shape {
public:
  void draw() { printf("circle %d: draw\n", id_); }
};
class Square : public Shape {
public:
  void draw() { printf("square %d: draw\n", id_); }
};

class Ellipse : public Shape {
public:
  void draw() { printf("ellipse %d: draw\n", id_); }
};
class Rectangle : public Shape {
public:
  void draw() { printf("rectangle %d: draw\n", id_); }
};

class Factory {
public:
  virtual Shape *createCurvedInstance() = 0;
  virtual Shape *createStraightInstance() = 0;
};

class SimpleShapeFactory : public Factory {
public:
  Shape *createCurvedInstance() { return new Circle; }
  Shape *createStraightInstance() { return new Square; }
};

class RobustShapeFactory : public Factory {
public:
  Shape *createCurvedInstance() { return new Ellipse; }
  Shape *createStraightInstance() { return new Rectangle; }
};

int main() {
#ifdef SIMPLE
  Factory *factory = new SimpleShapeFactory;
#elif ROBUST
  Factory *factory = new RobustShapeFactory;
#endif
  Shape *shapes[3];

  shapes[0] = factory->createCurvedInstance();   // shapes[0] = new Ellipse;
  shapes[1] = factory->createStraightInstance(); // shapes[1] = new Rectangle;
  shapes[2] = factory->createCurvedInstance();   // shapes[2] = new Ellipse;

  for (int i = 0; i < 3; i++) {
    shapes[i]->draw();
  }
}
```