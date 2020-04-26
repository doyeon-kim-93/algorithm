- 재귀식 O() notation 표현



1. ![image-20200426163241310](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426163241310.png)

``` 
*n=0 , T(n) = 1
T(n) = T(n-1)+1
	=T(n-2) +1 +1
	=T(1) +1+...+1
T(n) = O(n)
```



2. ![image-20200426163439348](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426163439348.png)

``` 
*n=0 , T(n) = 1
T(n) = T(n-1)+n
	=T(n-2) +n-1 +n
	=T(1) +1+2+...+n
	n(n+1)/2
T(n) = O(n^2)
```



3. ![image-20200426163911289](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426163911289.png)

```
*n=0 , T(n) = 1
T(n) = T(1) + logn + logn-1 + logn-2 + ... +log2
	<=T(1) + logn + logn + logn + logn + logn + logn
	<=T(1) + nlogn
T(n) = O(nlogn)
```



4. ![image-20200426164250432](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426164250432.png)

```
*n=1 T(n) = 1

T(n) = T(n/2) + 1 
T(n) = T(n/2^2) + 1 + 1
T(n) = T(n/2^k) + k
T(n) = logn + 1
T(n) = O(logn)
```



5. ![image-20200426165546020](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426165546020.png)

``` 
*n=1 T(n) = 1

T(n) = T(n/2) + 1
T(n) = T(n/4) + n/2 + n 
	=T(n/2^k) + n/2^k-1 + n/2 + n
n/2^k = 1 일때
k = logn
	=T(1) + n/2^logn-1 + ... +n/2 + n
	=1+n(1+1/2+1/4+....1/2^logn-1)
	=1+n(1+1)
T(n) = O(n)
```



6. ![image-20200426170515517](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426170515517.png)

``` 
*n=1 T(n) = 1

T(n) = 2T(n/2) + n
	= 2^2T(n/2^2) + n + n
	= 2^3T(n/2^3) + 3n
	= 2^kT(n/2^k)+kn
n/2^k = 1 일때
k = logn
T(n) = 2^kT(1)+kN
T(n) = n+nlogn
O(nlogn)
```



7. ![image-20200426172823034](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426172823034.png)

```
*n=1 T(n) = 1

T(n) = 3T(n/2) + n
	= 3(3T(n/4)+n/2)+n
	= 3(3(3T(n/8)+n/4)+n/2)+n
	=3^kT(n/2^k)+((3/2)^k-1)*N+...+(3/2)n+n
n/2^k = 1 일때
k = logn
등비수열의 합 이용
O(n^log3) .. log밑은 2
```



8. ![image-20200426173503683](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426173503683.png)

```
*n=0 T(n) = 1

T(n) = T(n-1) + 1/n
	= T(n-2) + 1/n + 1/n-1
	= T(n-3) + 1/n + 1/n-1 + 1/n-2
	= T(0) + 시그마 k=1 부터 n까지 1/k
	= 1 + log(n)
T(n) = O(logn)	
```



9. ![image-20200426175448125](%EC%9E%AC%EA%B7%80%EC%8B%9D%20O()%20notation%ED%91%9C%ED%98%84.assets/image-20200426175448125.png)

```
T(n) = O(nlog(log(n)))
```

