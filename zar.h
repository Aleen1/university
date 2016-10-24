#ifndef ZAR_H
#define ZAR_H

class czar
{
    private:
        int freq[10];
    public:
        czar();
        void vote();
        void reset_freq();
        friend class CTrib;
};


#endif // ZAR_H

