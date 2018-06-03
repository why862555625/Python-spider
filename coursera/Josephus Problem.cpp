/***************************
@coding: utf-8
@Time    : 2018/6/3
@Author  : A1058420631
@FileName: Josephus Problem
@Software: Clion
***************************/
#include<iostream>
#include<cstdio>
using namespace std;
typedef struct node {
	int data;
	node* next;
}cLinkList;
int main()
{
	cLinkList *head, *p, *s, *temp;
	int i=1, n, m;
	cin >> n >> m;

	head = new cLinkList;
	p = head;
	p->next = p;
	p->data = i;

	for (i = 2; i <= n; ++i)
	{
		s = new cLinkList;
		s->next = p->next;
		p->next = s;
		s->data = i;
		p = s;
	}
	p = head;
	while (n--)
	{
		for (i = 1; i < m - 1; ++i)
			p = p->next;
		temp = p->next;
		if(n==0) cout << temp->data;
		p->next = temp->next;
		delete temp;
		p = p->next;
	}
	return 0;
}
