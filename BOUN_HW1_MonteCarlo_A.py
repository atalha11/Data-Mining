import numpy as np
from scipy.stats import chi2

# Parametreler
population_mean = 50  
population_std = 10   
sample_size = 9        
confidence_level = 0.95         # Confidence Interval seviyesi (1 - alpha)
alpha = 1 - confidence_level    # Alpha değeri
NR = 1000                       # Yineleme sayısı (10k yapınca epey tutarlı oluyor)

count = 0
for _ in range(NR):
    # Random bi sample oluşturalım şimdi:
    sample = np.random.normal(population_mean, population_std, sample_size)
    
    # Oluşturduğumuz random sample'ın varyansını hesaplayalım:
    sample_variance = np.var(sample, ddof=1)
    
    # Degree of freedom: n-1 
    df = sample_size - 1
    
    # Chi square için alt ve üst kritik değerleri bulalım:
    chi_square_lower = chi2.ppf(alpha / 2, df)
    chi_square_upper = chi2.ppf(1 - alpha / 2, df)
    
    # Lower ve Upper Confidence Level:
    LCL = df * sample_variance / chi_square_upper
    UCL = df * sample_variance / chi_square_lower
    
    # Gerçek varyansın güven aralığı içinde olup olmadığını kontrol edelim:
    if LCL <= population_std**2 <= UCL:
        count += 1

# Olasılığı hesaplayalım:
probability = count / NR

# Yazdıralım:
print(f"Gerçek varyansın güven aralıklarına düşme olasılığı: {probability}")
