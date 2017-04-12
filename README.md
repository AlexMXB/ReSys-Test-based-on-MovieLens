# ReSys-Test-based-on-MovieLens
Reconmendation-System-in-python                                                                                                           
1.Base on python Surprise package and MovieLens 100k dataset to make Rating Prediction:Evaluate the performance by RMSE and MAE   
output like this:                                                                                                       
Computing the pearson similarity matrix...
Done computing similarity matrix.
user: 1          item: 1          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 1          item: 2          r_ui = 4.00   est = 3.06   {u'actual_k': 40, u'was_impossible': False}
user: 1          item: 3          r_ui = 4.00   est = 3.07   {u'actual_k': 40, u'was_impossible': False}
user: 1          item: 4          r_ui = 4.00   est = 3.67   {u'actual_k': 40, u'was_impossible': False}
user: 1          item: 5          r_ui = 4.00   est = 2.99   {u'actual_k': 40, u'was_impossible': False}
user: 1          item: 6          r_ui = 4.00   est = 3.68   {u'actual_k': 22, u'was_impossible': False}
user: 1          item: 7          r_ui = 4.00   est = 3.90   {u'actual_k': 40, u'was_impossible': False}
user: 1          item: 8          r_ui = 4.00   est = 3.35   {u'actual_k': 40, u'was_impossible': False}
user: 1          item: 9          r_ui = 4.00   est = 4.38   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 1          r_ui = 4.00   est = 4.05   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 2          r_ui = 4.00   est = 3.11   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 3          r_ui = 4.00   est = 2.96   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 4          r_ui = 4.00   est = 3.60   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 5          r_ui = 4.00   est = 3.34   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 6          r_ui = 4.00   est = 3.83   {u'actual_k': 23, u'was_impossible': False}
user: 2          item: 7          r_ui = 4.00   est = 4.04   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 8          r_ui = 4.00   est = 3.91   {u'actual_k': 40, u'was_impossible': False}
user: 2          item: 9          r_ui = 4.00   est = 3.98   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 1          r_ui = 4.00   est = 4.10   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 2          r_ui = 4.00   est = 3.24   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 3          r_ui = 4.00   est = 2.89   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 4          r_ui = 4.00   est = 3.42   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 5          r_ui = 4.00   est = 3.43   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 6          r_ui = 4.00   est = 3.38   {u'actual_k': 16, u'was_impossible': False}
user: 3          item: 7          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 8          r_ui = 4.00   est = 4.04   {u'actual_k': 40, u'was_impossible': False}
user: 3          item: 9          r_ui = 4.00   est = 3.97   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 1          r_ui = 4.00   est = 4.07   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 2          r_ui = 4.00   est = 3.06   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 3          r_ui = 4.00   est = 2.88   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 4          r_ui = 4.00   est = 3.34   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 5          r_ui = 4.00   est = 3.27   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 6          r_ui = 4.00   est = 3.84   {u'actual_k': 14, u'was_impossible': False}
user: 4          item: 7          r_ui = 4.00   est = 3.62   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 8          r_ui = 4.00   est = 4.04   {u'actual_k': 40, u'was_impossible': False}
user: 4          item: 9          r_ui = 4.00   est = 3.53   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 1          r_ui = 4.00   est = 3.84   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 2          r_ui = 4.00   est = 2.94   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 3          r_ui = 4.00   est = 2.98   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 4          r_ui = 4.00   est = 3.75   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 5          r_ui = 4.00   est = 3.20   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 6          r_ui = 4.00   est = 3.84   {u'actual_k': 23, u'was_impossible': False}
user: 5          item: 7          r_ui = 4.00   est = 3.88   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 8          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 5          item: 9          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 1          r_ui = 4.00   est = 3.90   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 2          r_ui = 4.00   est = 2.99   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 3          r_ui = 4.00   est = 2.84   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 4          r_ui = 4.00   est = 3.78   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 5          r_ui = 4.00   est = 3.19   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 6          r_ui = 4.00   est = 3.72   {u'actual_k': 25, u'was_impossible': False}
user: 6          item: 7          r_ui = 4.00   est = 3.35   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 8          r_ui = 4.00   est = 4.23   {u'actual_k': 40, u'was_impossible': False}
user: 6          item: 9          r_ui = 4.00   est = 4.14   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 1          r_ui = 4.00   est = 3.71   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 2          r_ui = 4.00   est = 3.20   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 3          r_ui = 4.00   est = 2.79   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 4          r_ui = 4.00   est = 4.04   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 5          r_ui = 4.00   est = 3.20   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 6          r_ui = 4.00   est = 3.36   {u'actual_k': 22, u'was_impossible': False}
user: 7          item: 7          r_ui = 4.00   est = 3.99   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 8          r_ui = 4.00   est = 4.39   {u'actual_k': 40, u'was_impossible': False}
user: 7          item: 9          r_ui = 4.00   est = 4.30   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 1          r_ui = 4.00   est = 3.63   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 2          r_ui = 4.00   est = 3.08   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 3          r_ui = 4.00   est = 3.10   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 4          r_ui = 4.00   est = 3.71   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 5          r_ui = 4.00   est = 3.08   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 6          r_ui = 4.00   est = 3.48   {u'actual_k': 19, u'was_impossible': False}
user: 8          item: 7          r_ui = 4.00   est = 3.46   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 8          r_ui = 4.00   est = 3.90   {u'actual_k': 40, u'was_impossible': False}
user: 8          item: 9          r_ui = 4.00   est = 3.93   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 1          r_ui = 4.00   est = 4.07   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 2          r_ui = 4.00   est = 3.36   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 3          r_ui = 4.00   est = 3.24   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 4          r_ui = 4.00   est = 3.51   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 5          r_ui = 4.00   est = 3.47   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 6          r_ui = 4.00   est = 4.04   {u'actual_k': 16, u'was_impossible': False}
user: 9          item: 7          r_ui = 4.00   est = 3.21   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 8          r_ui = 4.00   est = 4.01   {u'actual_k': 40, u'was_impossible': False}
user: 9          item: 9          r_ui = 4.00   est = 3.96   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 1          r_ui = 4.00   est = 3.63   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 2          r_ui = 4.00   est = 3.24   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 3          r_ui = 4.00   est = 2.90   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 4          r_ui = 4.00   est = 3.68   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 5          r_ui = 4.00   est = 3.30   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 6          r_ui = 4.00   est = 3.85   {u'actual_k': 21, u'was_impossible': False}
user: 10         item: 7          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 8          r_ui = 4.00   est = 3.93   {u'actual_k': 40, u'was_impossible': False}
user: 10         item: 9          r_ui = 4.00   est = 3.74   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 1          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 2          r_ui = 4.00   est = 3.27   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 3          r_ui = 4.00   est = 3.04   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 4          r_ui = 4.00   est = 3.55   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 5          r_ui = 4.00   est = 3.30   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 6          r_ui = 4.00   est = 3.73   {u'actual_k': 22, u'was_impossible': False}
user: 11         item: 7          r_ui = 4.00   est = 3.73   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 8          r_ui = 4.00   est = 4.06   {u'actual_k': 40, u'was_impossible': False}
user: 11         item: 9          r_ui = 4.00   est = 4.51   {u'actual_k': 40, u'was_impossible': False}
user: 12         item: 1          r_ui = 4.00   est = 3.81   {u'actual_k': 40, u'was_impossible': False}
user: 12         item: 2          r_ui = 4.00   est = 3.36   {u'actual_k': 40, u'was_impossible': False}
user: 12         item: 3          r_ui = 4.00   est = 3.06   {u'actual_k': 35, u'was_impossible': False}
user: 12         item: 4          r_ui = 4.00   est = 3.78   {u'actual_k': 40, u'was_impossible': False}
user: 12         item: 5          r_ui = 4.00   est = 3.51   {u'actual_k': 40, u'was_impossible': False}
user: 12         item: 6          r_ui = 4.00   est = 3.22   {u'actual_k': 11, u'was_impossible': False}
user: 12         item: 7          r_ui = 4.00   est = 3.71   {u'actual_k': 40, u'was_impossible': False}
user: 12         item: 8          r_ui = 4.00   est = 3.93   {u'actual_k': 40, u'was_impossible': False}
user: 12         item: 9          r_ui = 4.00   est = 3.74   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 1          r_ui = 4.00   est = 3.88   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 2          r_ui = 4.00   est = 3.09   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 3          r_ui = 4.00   est = 3.00   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 4          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 5          r_ui = 4.00   est = 2.91   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 6          r_ui = 4.00   est = 3.75   {u'actual_k': 25, u'was_impossible': False}
user: 13         item: 7          r_ui = 4.00   est = 3.48   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 8          r_ui = 4.00   est = 3.93   {u'actual_k': 40, u'was_impossible': False}
user: 13         item: 9          r_ui = 4.00   est = 3.87   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 1          r_ui = 4.00   est = 3.85   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 2          r_ui = 4.00   est = 3.42   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 3          r_ui = 4.00   est = 2.77   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 4          r_ui = 4.00   est = 3.81   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 5          r_ui = 4.00   est = 3.10   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 6          r_ui = 4.00   est = 4.24   {u'actual_k': 18, u'was_impossible': False}
user: 14         item: 7          r_ui = 4.00   est = 4.06   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 8          r_ui = 4.00   est = 4.40   {u'actual_k': 40, u'was_impossible': False}
user: 14         item: 9          r_ui = 4.00   est = 4.02   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 1          r_ui = 4.00   est = 3.17   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 2          r_ui = 4.00   est = 3.27   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 3          r_ui = 4.00   est = 3.07   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 4          r_ui = 4.00   est = 3.60   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 5          r_ui = 4.00   est = 3.26   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 6          r_ui = 4.00   est = 3.30   {u'actual_k': 16, u'was_impossible': False}
user: 15         item: 7          r_ui = 4.00   est = 3.13   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 8          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 15         item: 9          r_ui = 4.00   est = 3.94   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 1          r_ui = 4.00   est = 4.21   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 2          r_ui = 4.00   est = 3.33   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 3          r_ui = 4.00   est = 2.92   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 4          r_ui = 4.00   est = 3.75   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 5          r_ui = 4.00   est = 3.17   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 6          r_ui = 4.00   est = 3.55   {u'actual_k': 19, u'was_impossible': False}
user: 16         item: 7          r_ui = 4.00   est = 4.16   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 8          r_ui = 4.00   est = 4.16   {u'actual_k': 40, u'was_impossible': False}
user: 16         item: 9          r_ui = 4.00   est = 4.19   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 1          r_ui = 4.00   est = 4.37   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 2          r_ui = 4.00   est = 3.13   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 3          r_ui = 4.00   est = 2.90   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 4          r_ui = 4.00   est = 3.81   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 5          r_ui = 4.00   est = 3.12   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 6          r_ui = 4.00   est = 3.63   {u'actual_k': 16, u'was_impossible': False}
user: 17         item: 7          r_ui = 4.00   est = 4.18   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 8          r_ui = 4.00   est = 3.90   {u'actual_k': 40, u'was_impossible': False}
user: 17         item: 9          r_ui = 4.00   est = 4.10   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 1          r_ui = 4.00   est = 4.10   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 2          r_ui = 4.00   est = 3.14   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 3          r_ui = 4.00   est = 2.72   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 4          r_ui = 4.00   est = 3.63   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 5          r_ui = 4.00   est = 3.20   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 6          r_ui = 4.00   est = 3.96   {u'actual_k': 20, u'was_impossible': False}
user: 18         item: 7          r_ui = 4.00   est = 3.81   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 8          r_ui = 4.00   est = 4.23   {u'actual_k': 40, u'was_impossible': False}
user: 18         item: 9          r_ui = 4.00   est = 4.38   {u'actual_k': 40, u'was_impossible': False}
user: 19         item: 1          r_ui = 4.00   est = 3.88   {u'actual_k': 40, u'was_impossible': False}
user: 19         item: 2          r_ui = 4.00   est = 3.34   {u'actual_k': 40, u'was_impossible': False}
user: 19         item: 3          r_ui = 4.00   est = 2.81   {u'actual_k': 33, u'was_impossible': False}
user: 19         item: 4          r_ui = 4.00   est = 4.04   {u'actual_k': 40, u'was_impossible': False}
user: 19         item: 5          r_ui = 4.00   est = 3.35   {u'actual_k': 40, u'was_impossible': False}
user: 19         item: 6          r_ui = 4.00   est = 3.75   {u'actual_k': 13, u'was_impossible': False}
user: 19         item: 7          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 19         item: 8          r_ui = 4.00   est = 4.61   {u'actual_k': 40, u'was_impossible': False}
user: 19         item: 9          r_ui = 4.00   est = 4.15   {u'actual_k': 40, u'was_impossible': False}
user: 20         item: 1          r_ui = 4.00   est = 3.73   {u'actual_k': 40, u'was_impossible': False}
user: 20         item: 2          r_ui = 4.00   est = 3.33   {u'actual_k': 40, u'was_impossible': False}
user: 20         item: 3          r_ui = 4.00   est = 2.78   {u'actual_k': 35, u'was_impossible': False}
user: 20         item: 4          r_ui = 4.00   est = 3.31   {u'actual_k': 40, u'was_impossible': False}
user: 20         item: 5          r_ui = 4.00   est = 3.48   {u'actual_k': 35, u'was_impossible': False}
user: 20         item: 6          r_ui = 4.00   est = 4.06   {u'actual_k': 8, u'was_impossible': False}
user: 20         item: 7          r_ui = 4.00   est = 3.77   {u'actual_k': 40, u'was_impossible': False}
user: 20         item: 8          r_ui = 4.00   est = 4.37   {u'actual_k': 40, u'was_impossible': False}
user: 20         item: 9          r_ui = 4.00   est = 3.73   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 1          r_ui = 4.00   est = 4.22   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 2          r_ui = 4.00   est = 3.06   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 3          r_ui = 4.00   est = 3.10   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 4          r_ui = 4.00   est = 3.67   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 5          r_ui = 4.00   est = 3.08   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 6          r_ui = 4.00   est = 3.63   {u'actual_k': 24, u'was_impossible': False}
user: 21         item: 7          r_ui = 4.00   est = 4.35   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 8          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 21         item: 9          r_ui = 4.00   est = 4.47   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 1          r_ui = 4.00   est = 3.62   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 2          r_ui = 4.00   est = 2.97   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 3          r_ui = 4.00   est = 2.94   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 4          r_ui = 4.00   est = 3.85   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 5          r_ui = 4.00   est = 3.19   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 6          r_ui = 4.00   est = 3.72   {u'actual_k': 24, u'was_impossible': False}
user: 22         item: 7          r_ui = 4.00   est = 3.87   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 8          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 22         item: 9          r_ui = 4.00   est = 4.05   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 1          r_ui = 4.00   est = 4.05   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 2          r_ui = 4.00   est = 3.15   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 3          r_ui = 4.00   est = 2.68   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 4          r_ui = 4.00   est = 3.66   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 5          r_ui = 4.00   est = 3.19   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 6          r_ui = 4.00   est = 3.88   {u'actual_k': 26, u'was_impossible': False}
user: 23         item: 7          r_ui = 4.00   est = 3.80   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 8          r_ui = 4.00   est = 4.24   {u'actual_k': 40, u'was_impossible': False}
user: 23         item: 9          r_ui = 4.00   est = 4.16   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 1          r_ui = 4.00   est = 3.72   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 2          r_ui = 4.00   est = 3.09   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 3          r_ui = 4.00   est = 2.91   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 4          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 5          r_ui = 4.00   est = 3.04   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 6          r_ui = 4.00   est = 3.54   {u'actual_k': 22, u'was_impossible': False}
user: 24         item: 7          r_ui = 4.00   est = 3.57   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 8          r_ui = 4.00   est = 4.16   {u'actual_k': 40, u'was_impossible': False}
user: 24         item: 9          r_ui = 4.00   est = 4.36   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 1          r_ui = 4.00   est = 4.22   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 2          r_ui = 4.00   est = 3.23   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 3          r_ui = 4.00   est = 3.09   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 4          r_ui = 4.00   est = 3.69   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 5          r_ui = 4.00   est = 3.27   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 6          r_ui = 4.00   est = 3.76   {u'actual_k': 13, u'was_impossible': False}
user: 25         item: 7          r_ui = 4.00   est = 3.61   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 8          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 25         item: 9          r_ui = 4.00   est = 4.00   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 1          r_ui = 4.00   est = 3.65   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 2          r_ui = 4.00   est = 3.05   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 3          r_ui = 4.00   est = 2.93   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 4          r_ui = 4.00   est = 3.70   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 5          r_ui = 4.00   est = 3.21   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 6          r_ui = 4.00   est = 3.63   {u'actual_k': 23, u'was_impossible': False}
user: 26         item: 7          r_ui = 4.00   est = 3.96   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 8          r_ui = 4.00   est = 3.99   {u'actual_k': 40, u'was_impossible': False}
user: 26         item: 9          r_ui = 4.00   est = 4.32   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 1          r_ui = 4.00   est = 3.89   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 2          r_ui = 4.00   est = 3.29   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 3          r_ui = 4.00   est = 2.72   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 4          r_ui = 4.00   est = 3.68   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 5          r_ui = 4.00   est = 3.10   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 6          r_ui = 4.00   est = 4.24   {u'actual_k': 17, u'was_impossible': False}
user: 27         item: 7          r_ui = 4.00   est = 3.77   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 8          r_ui = 4.00   est = 4.15   {u'actual_k': 40, u'was_impossible': False}
user: 27         item: 9          r_ui = 4.00   est = 4.24   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 1          r_ui = 4.00   est = 3.79   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 2          r_ui = 4.00   est = 3.22   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 3          r_ui = 4.00   est = 2.99   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 4          r_ui = 4.00   est = 3.98   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 5          r_ui = 4.00   est = 3.09   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 6          r_ui = 4.00   est = 3.35   {u'actual_k': 16, u'was_impossible': False}
user: 28         item: 7          r_ui = 4.00   est = 4.19   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 8          r_ui = 4.00   est = 3.90   {u'actual_k': 40, u'was_impossible': False}
user: 28         item: 9          r_ui = 4.00   est = 3.67   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 1          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 2          r_ui = 4.00   est = 3.14   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 3          r_ui = 4.00   est = 2.88   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 4          r_ui = 4.00   est = 3.59   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 5          r_ui = 4.00   est = 3.15   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 6          r_ui = 4.00   est = 3.54   {u'actual_k': 20, u'was_impossible': False}
user: 29         item: 7          r_ui = 4.00   est = 3.83   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 8          r_ui = 4.00   est = 3.89   {u'actual_k': 40, u'was_impossible': False}
user: 29         item: 9          r_ui = 4.00   est = 4.19   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 1          r_ui = 4.00   est = 3.99   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 2          r_ui = 4.00   est = 3.14   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 3          r_ui = 4.00   est = 3.09   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 4          r_ui = 4.00   est = 3.67   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 5          r_ui = 4.00   est = 3.18   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 6          r_ui = 4.00   est = 3.47   {u'actual_k': 21, u'was_impossible': False}
user: 30         item: 7          r_ui = 4.00   est = 3.65   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 8          r_ui = 4.00   est = 3.75   {u'actual_k': 40, u'was_impossible': False}
user: 30         item: 9          r_ui = 4.00   est = 3.86   {u'actual_k': 40, u'was_impossible': False}
user: 31         item: 1          r_ui = 4.00   est = 3.91   {u'actual_k': 40, u'was_impossible': False}
user: 31         item: 2          r_ui = 4.00   est = 2.97   {u'actual_k': 40, u'was_impossible': False}
user: 31         item: 3          r_ui = 4.00   est = 2.49   {u'actual_k': 37, u'was_impossible': False}
user: 31         item: 4          r_ui = 4.00   est = 3.80   {u'actual_k': 40, u'was_impossible': False}
user: 31         item: 5          r_ui = 4.00   est = 3.35   {u'actual_k': 39, u'was_impossible': False}
user: 31         item: 6          r_ui = 4.00   est = 3.00   {u'actual_k': 13, u'was_impossible': False}
user: 31         item: 7          r_ui = 4.00   est = 4.11   {u'actual_k': 40, u'was_impossible': False}
user: 31         item: 8          r_ui = 4.00   est = 4.13   {u'actual_k': 40, u'was_impossible': False}
user: 31         item: 9          r_ui = 4.00   est = 4.16   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 1          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 2          r_ui = 4.00   est = 3.29   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 3          r_ui = 4.00   est = 3.23   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 4          r_ui = 4.00   est = 3.37   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 5          r_ui = 4.00   est = 3.23   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 6          r_ui = 4.00   est = 3.14   {u'actual_k': 20, u'was_impossible': False}
user: 32         item: 7          r_ui = 4.00   est = 4.01   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 8          r_ui = 4.00   est = 3.99   {u'actual_k': 40, u'was_impossible': False}
user: 32         item: 9          r_ui = 4.00   est = 3.78   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 1          r_ui = 4.00   est = 3.96   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 2          r_ui = 4.00   est = 3.19   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 3          r_ui = 4.00   est = 3.02   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 4          r_ui = 4.00   est = 3.70   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 5          r_ui = 4.00   est = 3.62   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 6          r_ui = 4.00   est = 3.32   {u'actual_k': 12, u'was_impossible': False}
user: 33         item: 7          r_ui = 4.00   est = 3.91   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 8          r_ui = 4.00   est = 3.73   {u'actual_k': 40, u'was_impossible': False}
user: 33         item: 9          r_ui = 4.00   est = 4.05   {u'actual_k': 40, u'was_impossible': False}
user: 34         item: 1          r_ui = 4.00   est = 4.08   {u'actual_k': 40, u'was_impossible': False}
user: 34         item: 2          r_ui = 4.00   est = 3.32   {u'actual_k': 40, u'was_impossible': False}
user: 34         item: 3          r_ui = 4.00   est = 2.93   {u'actual_k': 34, u'was_impossible': False}
user: 34         item: 4          r_ui = 4.00   est = 3.61   {u'actual_k': 40, u'was_impossible': False}
user: 34         item: 5          r_ui = 4.00   est = 3.25   {u'actual_k': 32, u'was_impossible': False}
user: 34         item: 6          r_ui = 4.00   est = 3.41   {u'actual_k': 16, u'was_impossible': False}
user: 34         item: 7          r_ui = 4.00   est = 3.60   {u'actual_k': 40, u'was_impossible': False}
user: 34         item: 8          r_ui = 4.00   est = 3.97   {u'actual_k': 40, u'was_impossible': False}
user: 34         item: 9          r_ui = 4.00   est = 4.14   {u'actual_k': 40, u'was_impossible': False}
user: 35         item: 1          r_ui = 4.00   est = 4.11   {u'actual_k': 40, u'was_impossible': False}
user: 35         item: 2          r_ui = 4.00   est = 3.19   {u'actual_k': 39, u'was_impossible': False}
user: 35         item: 3          r_ui = 4.00   est = 3.11   {u'actual_k': 37, u'was_impossible': False}
user: 35         item: 4          r_ui = 4.00   est = 3.59   {u'actual_k': 40, u'was_impossible': False}
user: 35         item: 5          r_ui = 4.00   est = 3.87   {u'actual_k': 25, u'was_impossible': False}
user: 35         item: 6          r_ui = 4.00   est = 3.69   {u'actual_k': 4, u'was_impossible': False}
user: 35         item: 7          r_ui = 4.00   est = 3.68   {u'actual_k': 40, u'was_impossible': False}
user: 35         item: 8          r_ui = 4.00   est = 4.02   {u'actual_k': 40, u'was_impossible': False}
user: 35         item: 9          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 36         item: 1          r_ui = 4.00   est = 4.03   {u'actual_k': 40, u'was_impossible': False}
user: 36         item: 2          r_ui = 4.00   est = 3.56   {u'actual_k': 22, u'was_impossible': False}
user: 36         item: 3          r_ui = 4.00   est = 3.31   {u'actual_k': 18, u'was_impossible': False}
user: 36         item: 4          r_ui = 4.00   est = 3.49   {u'actual_k': 40, u'was_impossible': False}
user: 36         item: 5          r_ui = 4.00   est = 3.55   {u'actual_k': 18, u'was_impossible': False}
user: 36         item: 6          r_ui = 4.00   est = 3.70   {u'actual_k': 7, u'was_impossible': False}
user: 36         item: 7          r_ui = 4.00   est = 3.70   {u'actual_k': 40, u'was_impossible': False}
user: 36         item: 8          r_ui = 4.00   est = 4.25   {u'actual_k': 38, u'was_impossible': False}
user: 36         item: 9          r_ui = 4.00   est = 3.74   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 1          r_ui = 4.00   est = 3.96   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 2          r_ui = 4.00   est = 3.17   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 3          r_ui = 4.00   est = 3.04   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 4          r_ui = 4.00   est = 3.85   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 5          r_ui = 4.00   est = 3.20   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 6          r_ui = 4.00   est = 3.80   {u'actual_k': 19, u'was_impossible': False}
user: 37         item: 7          r_ui = 4.00   est = 3.57   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 8          r_ui = 4.00   est = 4.07   {u'actual_k': 40, u'was_impossible': False}
user: 37         item: 9          r_ui = 4.00   est = 4.06   {u'actual_k': 40, u'was_impossible': False}
user: 38         item: 1          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 38         item: 2          r_ui = 4.00   est = 3.38   {u'actual_k': 40, u'was_impossible': False}
user: 38         item: 3          r_ui = 4.00   est = 3.11   {u'actual_k': 39, u'was_impossible': False}
user: 38         item: 4          r_ui = 4.00   est = 3.78   {u'actual_k': 40, u'was_impossible': False}
user: 38         item: 5          r_ui = 4.00   est = 3.32   {u'actual_k': 40, u'was_impossible': False}
user: 38         item: 6          r_ui = 4.00   est = 2.98   {u'actual_k': 5, u'was_impossible': False}
user: 38         item: 7          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 38         item: 8          r_ui = 4.00   est = 4.12   {u'actual_k': 40, u'was_impossible': False}
user: 38         item: 9          r_ui = 4.00   est = 3.48   {u'actual_k': 40, u'was_impossible': False}
user: 39         item: 1          r_ui = 4.00   est = 3.77   {u'actual_k': 40, u'was_impossible': False}
user: 39         item: 2          r_ui = 4.00   est = 3.32   {u'actual_k': 40, u'was_impossible': False}
user: 39         item: 3          r_ui = 4.00   est = 3.25   {u'actual_k': 30, u'was_impossible': False}
user: 39         item: 4          r_ui = 4.00   est = 3.63   {u'actual_k': 40, u'was_impossible': False}
user: 39         item: 5          r_ui = 4.00   est = 3.73   {u'actual_k': 33, u'was_impossible': False}
user: 39         item: 6          r_ui = 4.00   est = 3.24   {u'actual_k': 9, u'was_impossible': False}
user: 39         item: 7          r_ui = 4.00   est = 3.49   {u'actual_k': 40, u'was_impossible': False}
user: 39         item: 8          r_ui = 4.00   est = 3.70   {u'actual_k': 40, u'was_impossible': False}
user: 39         item: 9          r_ui = 4.00   est = 3.70   {u'actual_k': 40, u'was_impossible': False}
user: 40         item: 1          r_ui = 4.00   est = 4.18   {u'actual_k': 40, u'was_impossible': False}
user: 40         item: 2          r_ui = 4.00   est = 3.41   {u'actual_k': 40, u'was_impossible': False}
user: 40         item: 3          r_ui = 4.00   est = 3.22   {u'actual_k': 33, u'was_impossible': False}
user: 40         item: 4          r_ui = 4.00   est = 3.55   {u'actual_k': 40, u'was_impossible': False}
user: 40         item: 5          r_ui = 4.00   est = 3.57   {u'actual_k': 32, u'was_impossible': False}
user: 40         item: 6          r_ui = 4.00   est = 3.45   {u'actual_k': 10, u'was_impossible': False}
user: 40         item: 7          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 40         item: 8          r_ui = 4.00   est = 3.93   {u'actual_k': 40, u'was_impossible': False}
user: 40         item: 9          r_ui = 4.00   est = 3.71   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 1          r_ui = 4.00   est = 4.06   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 2          r_ui = 4.00   est = 3.32   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 3          r_ui = 4.00   est = 3.07   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 4          r_ui = 4.00   est = 3.65   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 5          r_ui = 4.00   est = 3.31   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 6          r_ui = 4.00   est = 3.60   {u'actual_k': 23, u'was_impossible': False}
user: 41         item: 7          r_ui = 4.00   est = 3.50   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 8          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 41         item: 9          r_ui = 4.00   est = 3.39   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 1          r_ui = 4.00   est = 4.30   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 2          r_ui = 4.00   est = 3.67   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 3          r_ui = 4.00   est = 2.97   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 4          r_ui = 4.00   est = 3.74   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 5          r_ui = 4.00   est = 3.30   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 6          r_ui = 4.00   est = 3.67   {u'actual_k': 16, u'was_impossible': False}
user: 42         item: 7          r_ui = 4.00   est = 3.84   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 8          r_ui = 4.00   est = 4.23   {u'actual_k': 40, u'was_impossible': False}
user: 42         item: 9          r_ui = 4.00   est = 3.68   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 1          r_ui = 4.00   est = 4.19   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 2          r_ui = 4.00   est = 3.31   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 3          r_ui = 4.00   est = 2.53   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 4          r_ui = 4.00   est = 3.58   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 5          r_ui = 4.00   est = 3.41   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 6          r_ui = 4.00   est = 3.30   {u'actual_k': 19, u'was_impossible': False}
user: 43         item: 7          r_ui = 4.00   est = 3.59   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 8          r_ui = 4.00   est = 4.00   {u'actual_k': 40, u'was_impossible': False}
user: 43         item: 9          r_ui = 4.00   est = 3.92   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 1          r_ui = 4.00   est = 3.85   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 2          r_ui = 4.00   est = 2.98   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 3          r_ui = 4.00   est = 2.93   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 4          r_ui = 4.00   est = 3.47   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 5          r_ui = 4.00   est = 3.19   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 6          r_ui = 4.00   est = 3.35   {u'actual_k': 19, u'was_impossible': False}
user: 44         item: 7          r_ui = 4.00   est = 4.07   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 8          r_ui = 4.00   est = 4.00   {u'actual_k': 40, u'was_impossible': False}
user: 44         item: 9          r_ui = 4.00   est = 4.28   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 1          r_ui = 4.00   est = 4.29   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 2          r_ui = 4.00   est = 3.09   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 3          r_ui = 4.00   est = 2.97   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 4          r_ui = 4.00   est = 3.69   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 5          r_ui = 4.00   est = 3.11   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 6          r_ui = 4.00   est = 3.88   {u'actual_k': 21, u'was_impossible': False}
user: 45         item: 7          r_ui = 4.00   est = 3.37   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 8          r_ui = 4.00   est = 4.16   {u'actual_k': 40, u'was_impossible': False}
user: 45         item: 9          r_ui = 4.00   est = 4.30   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 1          r_ui = 4.00   est = 3.60   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 2          r_ui = 4.00   est = 2.99   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 3          r_ui = 4.00   est = 2.97   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 4          r_ui = 4.00   est = 3.53   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 5          r_ui = 4.00   est = 3.18   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 6          r_ui = 4.00   est = 3.74   {u'actual_k': 20, u'was_impossible': False}
user: 46         item: 7          r_ui = 4.00   est = 3.82   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 8          r_ui = 4.00   est = 3.87   {u'actual_k': 40, u'was_impossible': False}
user: 46         item: 9          r_ui = 4.00   est = 4.12   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 1          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 2          r_ui = 4.00   est = 3.25   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 3          r_ui = 4.00   est = 3.06   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 4          r_ui = 4.00   est = 3.66   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 5          r_ui = 4.00   est = 3.05   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 6          r_ui = 4.00   est = 3.08   {u'actual_k': 18, u'was_impossible': False}
user: 47         item: 7          r_ui = 4.00   est = 3.83   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 8          r_ui = 4.00   est = 3.88   {u'actual_k': 40, u'was_impossible': False}
user: 47         item: 9          r_ui = 4.00   est = 4.06   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 1          r_ui = 4.00   est = 3.84   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 2          r_ui = 4.00   est = 3.38   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 3          r_ui = 4.00   est = 3.09   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 4          r_ui = 4.00   est = 3.58   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 5          r_ui = 4.00   est = 3.12   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 6          r_ui = 4.00   est = 3.27   {u'actual_k': 16, u'was_impossible': False}
user: 48         item: 7          r_ui = 4.00   est = 3.53   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 8          r_ui = 4.00   est = 4.08   {u'actual_k': 40, u'was_impossible': False}
user: 48         item: 9          r_ui = 4.00   est = 3.62   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 1          r_ui = 4.00   est = 3.36   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 2          r_ui = 4.00   est = 2.91   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 3          r_ui = 4.00   est = 2.86   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 4          r_ui = 4.00   est = 3.54   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 5          r_ui = 4.00   est = 3.03   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 6          r_ui = 4.00   est = 3.63   {u'actual_k': 23, u'was_impossible': False}
user: 49         item: 7          r_ui = 4.00   est = 3.88   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 8          r_ui = 4.00   est = 3.93   {u'actual_k': 40, u'was_impossible': False}
user: 49         item: 9          r_ui = 4.00   est = 4.12   {u'actual_k': 40, u'was_impossible': False}
user: 50         item: 1          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 50         item: 2          r_ui = 4.00   est = 3.07   {u'actual_k': 40, u'was_impossible': False}
user: 50         item: 3          r_ui = 4.00   est = 3.26   {u'actual_k': 40, u'was_impossible': False}
user: 50         item: 4          r_ui = 4.00   est = 3.44   {u'actual_k': 40, u'was_impossible': False}
user: 50         item: 5          r_ui = 4.00   est = 3.11   {u'actual_k': 36, u'was_impossible': False}
user: 50         item: 6          r_ui = 4.00   est = 2.91   {u'actual_k': 10, u'was_impossible': False}
user: 50         item: 7          r_ui = 4.00   est = 3.76   {u'actual_k': 40, u'was_impossible': False}
user: 50         item: 8          r_ui = 4.00   est = 3.88   {u'actual_k': 40, u'was_impossible': False}
user: 50         item: 9          r_ui = 4.00   est = 3.97   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 1          r_ui = 4.00   est = 3.75   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 2          r_ui = 4.00   est = 3.34   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 3          r_ui = 4.00   est = 3.15   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 4          r_ui = 4.00   est = 3.61   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 5          r_ui = 4.00   est = 3.16   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 6          r_ui = 4.00   est = 4.08   {u'actual_k': 9, u'was_impossible': False}
user: 51         item: 7          r_ui = 4.00   est = 3.90   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 8          r_ui = 4.00   est = 3.78   {u'actual_k': 40, u'was_impossible': False}
user: 51         item: 9          r_ui = 4.00   est = 3.70   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 1          r_ui = 4.00   est = 3.75   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 2          r_ui = 4.00   est = 3.34   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 3          r_ui = 4.00   est = 3.01   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 4          r_ui = 4.00   est = 3.43   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 5          r_ui = 4.00   est = 3.37   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 6          r_ui = 4.00   est = 3.64   {u'actual_k': 20, u'was_impossible': False}
user: 52         item: 7          r_ui = 4.00   est = 4.26   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 8          r_ui = 4.00   est = 3.86   {u'actual_k': 40, u'was_impossible': False}
user: 52         item: 9          r_ui = 4.00   est = 3.99   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 1          r_ui = 4.00   est = 3.81   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 2          r_ui = 4.00   est = 3.30   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 3          r_ui = 4.00   est = 2.90   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 4          r_ui = 4.00   est = 3.46   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 5          r_ui = 4.00   est = 3.26   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 6          r_ui = 4.00   est = 3.77   {u'actual_k': 21, u'was_impossible': False}
user: 53         item: 7          r_ui = 4.00   est = 3.23   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 8          r_ui = 4.00   est = 3.95   {u'actual_k': 40, u'was_impossible': False}
user: 53         item: 9          r_ui = 4.00   est = 4.31   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 1          r_ui = 4.00   est = 3.78   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 2          r_ui = 4.00   est = 3.07   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 3          r_ui = 4.00   est = 3.01   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 4          r_ui = 4.00   est = 3.48   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 5          r_ui = 4.00   est = 3.10   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 6          r_ui = 4.00   est = 3.97   {u'actual_k': 21, u'was_impossible': False}
user: 54         item: 7          r_ui = 4.00   est = 3.57   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 8          r_ui = 4.00   est = 3.98   {u'actual_k': 40, u'was_impossible': False}
user: 54         item: 9          r_ui = 4.00   est = 3.96   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 1          r_ui = 4.00   est = 3.61   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 2          r_ui = 4.00   est = 3.18   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 3          r_ui = 4.00   est = 3.32   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 4          r_ui = 4.00   est = 3.63   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 5          r_ui = 4.00   est = 3.22   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 6          r_ui = 4.00   est = 3.96   {u'actual_k': 12, u'was_impossible': False}
user: 55         item: 7          r_ui = 4.00   est = 3.19   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 8          r_ui = 4.00   est = 3.89   {u'actual_k': 40, u'was_impossible': False}
user: 55         item: 9          r_ui = 4.00   est = 3.97   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 1          r_ui = 4.00   est = 3.78   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 2          r_ui = 4.00   est = 3.22   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 3          r_ui = 4.00   est = 3.07   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 4          r_ui = 4.00   est = 3.73   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 5          r_ui = 4.00   est = 3.40   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 6          r_ui = 4.00   est = 3.44   {u'actual_k': 17, u'was_impossible': False}
user: 56         item: 7          r_ui = 4.00   est = 4.20   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 8          r_ui = 4.00   est = 4.26   {u'actual_k': 40, u'was_impossible': False}
user: 56         item: 9          r_ui = 4.00   est = 3.63   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 1          r_ui = 4.00   est = 4.39   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 2          r_ui = 4.00   est = 3.20   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 3          r_ui = 4.00   est = 2.71   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 4          r_ui = 4.00   est = 3.53   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 5          r_ui = 4.00   est = 3.28   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 6          r_ui = 4.00   est = 3.61   {u'actual_k': 19, u'was_impossible': False}
user: 57         item: 7          r_ui = 4.00   est = 3.56   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 8          r_ui = 4.00   est = 3.90   {u'actual_k': 40, u'was_impossible': False}
user: 57         item: 9          r_ui = 4.00   est = 4.07   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 1          r_ui = 4.00   est = 4.03   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 2          r_ui = 4.00   est = 3.06   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 3          r_ui = 4.00   est = 2.75   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 4          r_ui = 4.00   est = 3.61   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 5          r_ui = 4.00   est = 3.02   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 6          r_ui = 4.00   est = 3.61   {u'actual_k': 24, u'was_impossible': False}
user: 58         item: 7          r_ui = 4.00   est = 4.12   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 8          r_ui = 4.00   est = 4.00   {u'actual_k': 40, u'was_impossible': False}
user: 58         item: 9          r_ui = 4.00   est = 4.18   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 1          r_ui = 4.00   est = 3.57   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 2          r_ui = 4.00   est = 3.12   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 3          r_ui = 4.00   est = 3.23   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 4          r_ui = 4.00   est = 3.82   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 5          r_ui = 4.00   est = 3.13   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 6          r_ui = 4.00   est = 3.74   {u'actual_k': 22, u'was_impossible': False}
user: 59         item: 7          r_ui = 4.00   est = 4.22   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 8          r_ui = 4.00   est = 4.07   {u'actual_k': 40, u'was_impossible': False}
user: 59         item: 9          r_ui = 4.00   est = 4.13   {u'actual_k': 40, u'was_impossible': False}
[Finished in 3.2s]
2.Coding in Python to Simply implement UserCF and ItemCF algorithms and Movielens latest dataset to make Top-N recommendation:Evaluate the performance by precision,recall,coverage,and popularity
output like this:
Welcome to use ItembasedCF Test System
Similar movie number = 20
Recommended movie number = 10
loading ml-latest-small/ratings.csv(0)
loading ml-latest-small/ratings.csv(100000)
load ml-latest-small/ratings.csv succ
split training set and test set succ
train set = 69948
test set = 30056
counting movies number and popularity...
count movies number and popularity succ
total movie number = 8030
building co-rated users matrix...
build co-rated users matrix succ
calculating movie similarity matrix...
calculating movie similarity factor(2000000)
calculating movie similarity factor(4000000)
calculating movie similarity factor(6000000)
calculating movie similarity factor(8000000)
calculating movie similarity factor(10000000)
calculating movie similarity factor(12000000)
calculate movie similarity matrix(similarity factor) succ
Total similarity factor number = 13535044
Evaluation start...
recommended for 0 users
recommended for 500 users
precision=0.2863	recall=0.0639	coverage=0.0857	popularity=4.4215
[Finished in 212.0s]                                                                                                                     AND                                                                                                                                     Welcome to UserBasedCF Test System
Similar user number = 20
recommended movie number = 10
loading linesml-latest-small/ratings.csv(0)
loading linesml-latest-small/ratings.csv(10000)
loading linesml-latest-small/ratings.csv(20000)
loading linesml-latest-small/ratings.csv(30000)
loading linesml-latest-small/ratings.csv(40000)
loading linesml-latest-small/ratings.csv(50000)
loading linesml-latest-small/ratings.csv(60000)
loading linesml-latest-small/ratings.csv(70000)
loading linesml-latest-small/ratings.csv(80000)
loading linesml-latest-small/ratings.csv(90000)
loading linesml-latest-small/ratings.csv(100000)
load ml-latest-small/ratings.csv succ
split training set and test set succ
train set = 50050
test set = 49954
building movie-users inverse table...
build movie-users inverse table success
total movie number = 7118
building user co-rated movies matrix...
build user co-rated movies matrix success
calculating user similarity matrix...
calculating user similarity factor(100000)
calculating user similarity factor(200000)
calculating user similarity factor(300000)
calculate user similarity matrix(similarity factor) succ
Total similarity factor number = 300752
Evaluation start...
recommending for 0
recommending for 50
recommending for 100
recommending for 150
recommending for 200
recommending for 250
recommending for 300
recommending for 350
recommending for 400
recommending for 450
recommending for 500
recommending for 550
recommending for 600
recommending for 650
precision=0.3671	recall=0.0493	coverage=0.0580	popularity=4.4403
[Finished in 4.8s]
