# Mystery Module

Bu depo, ikinci dereceden denklemlerin koklerini hesaplayan kucuk bir Python modulu icerir.

## Modulin Amaci

`mystery_module.py` dosyasindaki `fn_x(a, b, c)` fonksiyonu, su denklemin reel koklerini hesaplar:

- `a*x^2 + b*x + c = 0`

Fonksiyon diskriminant yaklasimi ile calisir:

- `d = b^2 - 4ac`
- `d < 0` ise reel kok olmadigi icin `None` doner
- `d >= 0` ise `(x1, x2)` seklinde iki kok doner

## Hızlı Kullanim

```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)
print(roots)  # (2.0, 1.0)
```

## API Dokumani

### `fn_x(a, b, c)`

Ikinci dereceden denklemin reel koklerini hesaplar.

Parametreler:

- `a` (int | float): x^2 katsayisi
- `b` (int | float): x katsayisi
- `c` (int | float): sabit terim

Donus degeri:

- `tuple[float, float]`: Reel kokler `(x1, x2)`
- `None`: Diskriminant negatifse (reel kok yok)

## Ornekler

Reel koklu durum:

```python
print(fn_x(1, -5, 6))
# (3.0, 2.0)
```

Tekrarlanan kok durumu (`d = 0`):

```python
print(fn_x(1, -2, 1))
# (1.0, 1.0)
```

Reel kok olmayan durum:

```python
print(fn_x(1, 0, 1))
# None
```

## Bilinen Kisıtlar

- `a = 0` icin fonksiyon ikinci dereceden denklem kontrolu yapmaz.
- `a = 0` verilirse sifira bolme hatasi olusabilir.
- Tip kontrolu (sayisal degilse hata) fonksiyon icinde acikca yapilmiyor.

## Gelistirme Onerileri

- `fn_x` yerine daha acik bir isim (or. `solve_quadratic`) kullanin.
- Girdi dogrulamasi ekleyin (`a != 0`, sayisal tip kontrolu).
- Negatif diskriminantta `None` yerine acik bir ozel hata sinifi dusunulebilir.
- Fonksiyon icine docstring ve type hint ekleyin.

## Gereksinimler

- Python 3.x
- Standart kutuphane `math`

## Lisans

Bu calisma egitim amacli bir sandbox icerigidir.
