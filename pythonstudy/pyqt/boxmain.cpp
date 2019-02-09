#include <QApplication>
#include <QDialog>
#include <QPushButton>
#include <QFont>
#include <QVBoxLayout>
#include <QSlider>
#include <QLCDNumber>


int main(int argc, char **argv)
{
    QApplication app(argc,argv);

    QDialog w;
    w.resize(400,300);
    w.setMinimumSize(400,300);
    w.setMaximumSize(400,300);
    w.setGeometry(100,100,200,120);

    QPushButton *qt=new QPushButton("quit",&w);
    qt->setGeometry(62,40,75,30);
    qt->setFont(QFont("Times",18,QFont::Bold));
    QObject::connect(qt,SIGNAL(clicked()),&app,SLOT(quit()));

    QLCDNumber *lcd=new QLCDNumber(2,&w);
    QSlider *slider=new QSlider(Qt::Horizontal,&w);
    slider->setRange(0,99);
    slider->setValue(0);
    QObject::connect(slider,SIGNAL(valueChanged(int)),lcd,SLOT(display(int)));

    

    QVBoxLayout box;
    box.addWidget(qt);
    box.addWidget(lcd);
    box.addWidget(slider);
    w.setLayout(&box);
    w.show();
    return app.exec();
}

