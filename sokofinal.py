class Sokoban:
	
#variables globales
	
	mapa=[[2,2,2,2,2,2,2,2],
	
	[2,1,1,1,1,1,1,2],
	
	[2,0,1,1,3,1,1,2],
	
	[2,1,3,4,1,1,1,2],
	[2,1,1,1,1,1,4,2],

	[2,1,1,1,1,1,1,2],
	[2,1,1,1,1,1,1,2],	
	[2,2,2,2,2,2,2,2]]

	fila_monito=2	
	columna_monito=1

	pasar=1
	num_metas=0
	jala=False	
	def  __init__(self): 
		
		print 'Sokoban'

	
	def imprimir_mapa(self):#imprimir mapa
		
	
		for f in range (8):
			
			linea=''
			
			for c in range (8):
				
				linea = linea+'  '+str(self.mapa [f][c])
		
			print linea
	
	def contar_metas(self):
			for fila in range(8):
				for columna in range(8):
					if self.mapa[fila][columna]==4:
						self.num_metas+=1
						

	def mover_derecha(self):
		
		if self.mapa [self.fila_monito][self.columna_monito+1]==1:
			
			self.mapa [self.fila_monito][self.columna_monito+1]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito+=1

			self.pasar=1		
		elif self.mapa [self.fila_monito][self.columna_monito+1]==3 and self.mapa [self.fila_monito][self.columna_monito+2]==1:
		
			self.mapa [self.fila_monito][self.columna_monito+1]=0
			
			self.mapa [self.fila_monito][self.columna_monito+2]=3			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito+=1


			self.pasar=1
		elif self.mapa [self.fila_monito][self.columna_monito+1]==3 and self.mapa [self.fila_monito][self.columna_monito+2]==4:
		
			self.mapa [self.fila_monito][self.columna_monito+1]=0
			
			self.mapa [self.fila_monito][self.columna_monito+2]=5			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito+=1


			self.pasar=1
			self.num_metas-=1
		elif self.mapa [self.fila_monito][self.columna_monito+1]==4:
			
			self.mapa [self.fila_monito][self.columna_monito+1]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito+=1

			self.pasar=4	
	def mover_izquierda(self):
		
		if self.mapa [self.fila_monito][self.columna_monito-1]==1: 
	
			self.mapa [self.fila_monito][self.columna_monito-1]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito-=1
	
			self.pasar=1	
		elif self.mapa [self.fila_monito][self.columna_monito-1]==3 and self.mapa [self.fila_monito][self.columna_monito-2]==1:
			
			self.mapa [self.fila_monito][self.columna_monito-1]=0
			
			self.mapa [self.fila_monito][self.columna_monito-2]=3
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito-=1
			self.pasar=1
		elif self.mapa [self.fila_monito][self.columna_monito-1]==3 and self.mapa [self.fila_monito][self.columna_monito-2]==4:
			
			self.mapa [self.fila_monito][self.columna_monito-1]=0
			
			self.mapa [self.fila_monito][self.columna_monito-2]=5			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito-=1
			self.pasar=1
			self.num_metas-=1
		elif self.mapa [self.fila_monito][self.columna_monito-1]==4: 
	
			self.mapa [self.fila_monito][self.columna_monito-1]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.columna_monito-=1
	
			self.pasar=4	

	def mover_arriba(self):
		
		if self.mapa [self.fila_monito-1][self.columna_monito]==1:
			
			self.mapa [self.fila_monito-1][self.columna_monito]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.fila_monito-=1

			self.pasar=1
		elif self.mapa [self.fila_monito-1][self.columna_monito]==3 and self.mapa [self.fila_monito-2][self.columna_monito]==1:
			
			self.mapa [self.fila_monito-1][self.columna_monito]=0
			
			self.mapa [self.fila_monito-2][self.columna_monito]=3
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.fila_monito-=1

			self.pasar=1
		elif self.mapa [self.fila_monito-1][self.columna_monito]==3 and self.mapa [self.fila_monito-2][self.columna_monito]==4:
			
			self.mapa [self.fila_monito-1][self.columna_monito]=0
			
			self.mapa [self.fila_monito-2][self.columna_monito]=5			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.fila_monito-=1
	
			self.pasar=1
			self.num_metas-=1
		elif self.mapa [self.fila_monito-1][self.columna_monito]==4:
			
			self.mapa [self.fila_monito-1][self.columna_monito]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.fila_monito-=1

			self.pasar=4
	
	def mover_abajo(self):
		
		if self.mapa [self.fila_monito+1][self.columna_monito]==1:
			
			self.mapa [self.fila_monito+1][self.columna_monito]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.fila_monito+=1
	
			self.pasar=1
		
		elif self.mapa [self.fila_monito+1][self.columna_monito]==3 and self.mapa [self.fila_monito+2][self.columna_monito]==1:
			
			self.mapa [self.fila_monito+1][self.columna_monito]=0
			
			self.mapa [self.fila_monito+2][self.columna_monito]=3
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar
			
			self.fila_monito+=1



			self.pasar=1
		elif self.mapa [self.fila_monito+1][self.columna_monito]==3 and self.mapa [self.fila_monito+2][self.columna_monito]==4:
			
			self.mapa [self.fila_monito+1][self.columna_monito]=0
			
			self.mapa [self.fila_monito+2][self.columna_monito]=5			
			self.mapa [self.fila_monito][self.columna_monito]=self.pasar			
			self.fila_monito+=1

			self.pasar=1
			self.num_metas-=1
		elif self.mapa [self.fila_monito+1][self.columna_monito]==4:
			
			self.mapa [self.fila_monito+1][self.columna_monito]=0
			
			self.mapa[self.fila_monito][self.columna_monito]=self.pasar			
			self.fila_monito+=1
	
			self.pasar=4
	def jala_caja(self):
		if self.mapa [self.fila_monito][self.columna_monito-1]==1 and self.mapa[self.fila_monito][self.columna_monito+1]==3:
			self.jala=True
			if self.jala==True:	
				self.mapa [self.fila_monito][self.columna_monito-1]=0			
				self.mapa [self.fila_monito][self.columna_monito+1]=1			
				self.mapa[self.fila_monito][self.columna_monito]=3			
				self.columna_monito-=1

	
		elif self.mapa [self.fila_monito][self.columna_monito+1]==1 and self.mapa[self.fila_monito][self.columna_monito-1]==3:
			self.jala=True
			if self.jala==True:	
				self.mapa [self.fila_monito][self.columna_monito+1]=0			
				self.mapa [self.fila_monito][self.columna_monito-1]=1			
				self.mapa[self.fila_monito][self.columna_monito]=3			
				self.columna_monito+=1

	
		elif self.mapa [self.fila_monito-1][self.columna_monito]==1 and self.mapa[self.fila_monito+1][self.columna_monito]==3:
			self.jala=True
			if self.jala==True:	
				self.mapa [self.fila_monito-1][self.columna_monito]=0			
				self.mapa [self.fila_monito+1][self.columna_monito]=1			
				self.mapa[self.fila_monito][self.columna_monito]=3			
				self.fila_monito-=1


		elif self.mapa [self.fila_monito+1][self.columna_monito]==1 and self.mapa[self.fila_monito-1][self.columna_monito]==3:
			self.jala=True
			if self.jala==True:	
				self.mapa [self.fila_monito+1][self.columna_monito]=0			
				self.mapa [self.fila_monito-1][self.columna_monito]=1			
				self.mapa[self.fila_monito][self.columna_monito]=3			
				self.fila_monito+=1

	
			
objeto=Sokoban()
objeto.contar_metas()

while True:
	objeto.imprimir_mapa()
	print 'metas son: '+str(objeto.num_metas)
	
	movimiento=raw_input('a - d -aa - ao - j: ')
	
	if movimiento=='d':
		
		objeto.mover_derecha()
	
	elif movimiento=='a':
		
		objeto.mover_izquierda()
	
	elif movimiento=='aa':
		
		objeto.mover_arriba()
	
	elif movimiento=='ao':
		
		objeto.mover_abajo()
	elif movimiento=='j':
		objeto.jala_caja()

	if objeto.num_metas==0:
		print 'fin del juego'
		break



	