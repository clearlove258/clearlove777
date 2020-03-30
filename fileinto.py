int saddle(int m, int n, int a[][3], int ***q)

{

	int **res;

	res=(int**)malloc(sizeof(int*)*(m>n?n:m));

	int i,j,k,min,min_index,b,s=0;

	for(i=0;i<m;i++){

		min=a[i][0];

		min_index=0;

		for(j=1;j<n;j++){

			if(a[i][j]<min){

				min=a[i][j];

				min_index=j;

			}

		}

		for(k=0;k<m;k++){

			if(a[k][min_index]>min) break;

		}

		if (k==m){

			res[s]=(int*)malloc(sizeof(int)*2);

			res[s][0]=i;

			res[s][1]=min_index;

			s++;

		}

	}

	*q=res;

	return s;

}


