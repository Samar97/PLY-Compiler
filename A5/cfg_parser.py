#!/usr/bin/python3

from __future__ import print_function
import sys
import ply.lex as lex
import ply.yacc as yacc

import glob

tokens = (
		'ID','TEMPVAR','NUMBER','FLOATNUM',
		'LPAREN', 'RPAREN', 'BLOCK',
		'AMPERSAND', 'COMMA',
		'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 
		'IF', 'ELSE', 'RETURN','GOTO',
		'LT','GT','LE','GE','EQ','NE','NOT','AND', 'OR'
)

t_ignore = " \t"

def t_newline(t):
	r'\n|\r\n'

t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'\!\='
t_NOT = r'\!'
t_LT = r'<'
t_GT = r'>'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_AMPERSAND = r'\&'
t_COMMA = r','

reserved = {
	'if'	: 'IF',
	'else'	: 'ELSE',
	'goto' : 'GOTO',
	'return' : 'RETURN',
	'bb' : 'BLOCK'
}

def t_TEMPVAR(t):
	r't[0-9]+'
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t


def t_FLOATNUM(t):
	r'\d+\.\d+'
	try:
		t.value = float(t.value)
	except ValueError:
		print("Float value too precise %d", t.value)
		t.value = 0
	return t

def t_NUMBER(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Integer value too large %d", t.value)
		t.value = 0
	return t

def t_error(t): 
	print("Illegal character %s" % t.value[0])
	t.lexer.skip(1)

# Parsing rules
precedence = (
	('right', 'EQUALS'),
	('left', 'OR'),
	('left', 'AND'),
	('left', 'EQ', 'NE','NOT'),
	('left', 'LT', 'GT', 'LE', 'GE'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('right', 'AMPERSAND','STAR'),
)

def yaccprint(p):
	for x in p: print(x)
	print("\n")

####################### RULES ###################

def p_statement(p):
	'''
	statement : label 
			| assignment
			| ifstmt
			| elsestmt
			| gotostmt
			| returnstmt
			| funcall
			|
	'''
	pass

def p_pointer(p):
	'''
	pointer : TIMES pointer %prec STAR
			| TIMES address %prec STAR
			| TIMES ID %prec STAR
	'''
	if p[2][0] == 'A':
		p[0] = ('P',p[2][1],p[2][2]+1)
	elif p[2][0] == 'P':
		p[0] = ('P',p[2][1],p[2][2]+1)
	else:
		p[0] = ('P',p[2],1)
		

def p_address(p):
	'''
	address : AMPERSAND ID
	'''
	p[0] = ('A',p[2],-1)


def p_var_id(p):
	'''
	var : ID
	'''
	p[0] = ('I',p[1],0)

def p_var_tempvar(p):
	'''
	var : TEMPVAR
	'''
	p[0] = ('T',p[1],0)

def p_var_const_int(p):
	'''
	var : const_int
	'''
	p[0] = ('C',p[1],0)

def p_var_const_float(p):
	'''
	var : const_float
	'''
	p[0] = ('F',p[1],0)

def p_var_pointer(p):
	'''
	var : pointer
	'''
	p[0] = p[1]

def p_const_float(p):
	'''
	const_float : FLOATNUM
	'''
	p[0] = p[1]

def p_const_int(p):
	'''
	const_int : NUMBER
	'''
	p[0] = p[1]


def p_label(p):
	'''
	label : LT BLOCK NUMBER GT
	'''
	print(glob.label%int(p[3]),file=globals()['rfile'])

def p_assignment(p):
	'''
	assignment : unassign
			| binassign
			| funassign
	'''
	pass

def p_funassign(p):
	'''
	funassign : var EQUALS funcall
	'''
	reg = glob.registers.fetch_register()
	print(glob.move_from_v1%(reg),file=rfile)
	analyse_lhs(p[1][0],p[1][1],p[1][2],reg)
	glob.registers.free_register(reg)

def p_funcall(p):
	'''
	funcall : var LPAREN params RPAREN
	params : var paramcomp
			|
	'''
	def get_size(v):
		rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
		if v[0] == 'F':
			size = 8
		elif v[0] == 'C':
			size = 4
		elif v[0] == 'T':
			if glob.registers.is_float(v[1]): 
				size = 8
			else: 
				size = 4 
		elif v[0] == 'P' or v[0] == 'I':
			is_float = None
			if v[1] in rt.globals:
				is_float = rt.is_float_variable(v[1],v[2])
			else:
				is_float = ft.is_float_variable(v[1],v[2])
			if is_float : 
				size = 8
			else: 
				size = 4
		if size == 4: 
			return (size,False)
		else:
			return (size,True)

	if len(p) == 3:
		p[2].insert(0,p[1])
		p[0] = p[2]	
	elif len(p) == 0:
		p[0] = []
	else:
		print(glob.set_act_rec,file=rfile)
		size = 0
		for v in p[3]:
			size += get_size(v)[0]

		offset = -size 
		for v in p[3]:
			(vsize,is_float) = get_size(v)
			offset += vsize
			rhs_func = globals()['rhs_functions'][v[0]]
			reg = rhs_func(v[1],v[2])
			print(glob.sw_map[is_float]%(reg,offset,'sp'),file=rfile)
			glob.registers.free_register(reg)

		print(glob.sp_sub%(size),file=rfile)
		print(glob.jal%p[1][1],file=rfile)
		print(glob.sp_add%(size),file=rfile)

def p_paramcomp(p):
	'''
	paramcomp : COMMA var paramcomp
			|
	'''
	if len(p) == 1:
		p[0] = []
	else:
		p[3].insert(0,p[2])
		p[0] = p[3]	

def p_unassign(p):
	'''
	unassign : var EQUALS var
			| var EQUALS MINUS var
			| var EQUALS NOT var
			| var EQUALS address
	'''
	rfile=globals()['rfile']
	try:
		rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
		if len(p) == 4:
			## var EQUALS address ##
			rhs_func = globals()['rhs_functions'][p[3][0]]
			r_reg = rhs_func(p[3][1],p[3][2])

			analyse_lhs(p[1][0],p[1][1],p[1][2],r_reg)
			glob.registers.free_register(r_reg)
			
		else:
			## Assuming temporaries on both sides ##
			if p[3] == '!':
				r_reg = glob.registers.get_mapping(p[4][1])
				l_reg = glob.registers.fetch_register()
				print(glob.xori%(l_reg,r_reg,1),file=rfile)
				glob.registers.clear_mapping(p[4][1])
				analyse_lhs(p[1][0],p[1][1],p[1][2],l_reg)
				glob.registers.free_register(l_reg)

			elif p[3] == '-':
				rhs_func = globals()['rhs_functions'][p[4][0]]
				r_reg = rhs_func(p[4][1],p[4][2])
				r_reg = print_negu(r_reg)

				analyse_lhs(p[1][0],p[1][1],p[1][2],r_reg)
				glob.registers.free_register(r_reg)

	except:
		print(p[1],p[2],p[3])
		print("Error in unary assignment")
		pass

def p_binassign(p):
	'''
	binassign : condassign
			| arithassign 
	'''
	pass

def p_condassign(p):
	'''
	condassign : var EQUALS var condop var
	'''
	rfile = globals()['rfile']
	rhs_func1,rhs_func2 = globals()['rhs_functions'][p[3][0]],globals()['rhs_functions'][p[5][0]]
	r_reg1 = rhs_func1(p[3][1],p[3][2])
	r_reg2 = rhs_func2(p[5][1],p[5][2])

	r_reg = glob.registers.fetch_register()
	if not glob.registers.is_float_reg(r_reg1):
		if p[4] in glob.conditional:
			print(glob.conditional[p[4]]%(r_reg,r_reg1,r_reg2),file = rfile)
		else:
			if p[4] == '>':
				print(glob.slt%(r_reg,r_reg2,r_reg1),file = rfile)
			else:
				print(glob.sle%(r_reg,r_reg2,r_reg1),file = rfile)		
	else:
		c = glob.float_cond_num
		if p[4] in glob.float_conditional:
			print(glob.float_conditional[p[4]]%(r_reg1,r_reg2,c,r_reg,c,c,r_reg,c),file = rfile)
		else:
			if p[4] == '>':
				print(glob.c_lt_s%(r_reg2,r_reg1,c,r_reg,c,c,r_reg,c),file = rfile)
			else:
				print(glob.c_le_s%(r_reg2,r_reg1,c,r_reg,c,c,r_reg,c),file = rfile)
		glob.float_cond_num+=1

	glob.registers.free_register(r_reg1)
	glob.registers.free_register(r_reg2)

	analyse_lhs(p[1][0],p[1][1],p[1][2],r_reg)
	glob.registers.free_register(r_reg)

def p_arithassign(p):
	'''
	arithassign : var EQUALS var arithop var
	'''
	rfile = globals()['rfile']
	rhs_func1,rhs_func2 = globals()['rhs_functions'][p[3][0]],globals()['rhs_functions'][p[5][0]]
	r_reg1 = rhs_func1(p[3][1],p[3][2])
	r_reg2 = rhs_func2(p[5][1],p[5][2])

	if not glob.registers.is_float_reg(r_reg1):
		r_reg = glob.registers.fetch_register()
		if p[4] in glob.arithmetic:
			print(glob.arithmetic[p[4]]%(r_reg,r_reg1,r_reg2),file = rfile)
		else:
			print(glob.div%(r_reg1,r_reg2),file = rfile)
			print(glob.mflo%(r_reg),file=rfile)
	else:
		r_reg = glob.registers.fetch_register(is_float=True)
		print(glob.float_arithmetic[p[4]]%(r_reg,r_reg1,r_reg2),file = rfile)

	glob.registers.free_register(r_reg1)
	glob.registers.free_register(r_reg2)
	analyse_lhs(p[1][0],p[1][1],p[1][2],r_reg)
	glob.registers.free_register(r_reg)

def p_condop(p):
	'''
	condop : LT
			| GT
			| GE
			| LE
			| EQ
			| NE
			| AND
			| OR
	'''
	p[0] = p[1]

def p_arithop(p):
	'''
	arithop : PLUS
			| MINUS
			| TIMES
			| DIVIDE
	'''
	p[0] = p[1]

def p_ifstmt(p):
	'''
	ifstmt : IF LPAREN TEMPVAR RPAREN GOTO LT BLOCK NUMBER GT
	'''
	rfile = globals()['rfile']
	reg = glob.registers.get_mapping(p[3])
	print(glob.bne%(reg,p[8]),file = rfile)
	glob.registers.clear_mapping(p[3])


def p_elsestmt(p):
	'''
	elsestmt : ELSE gotostmt
	'''
	pass

def p_gotostmt(p):
	'''
	gotostmt : GOTO LT BLOCK NUMBER GT
	'''
	print(glob.jump_statement%int(p[4]),file=globals()['rfile'])

def p_returnstmt(p):
	'''
	returnstmt : RETURN
			| RETURN var
			| RETURN address
	'''
	glob.stmtreturn = True
	if len(p) == 3:
		rhs_func = globals()['rhs_functions'][p[2][0]]
		reg = rhs_func(p[2][1],p[2][2])
		print(glob.move_to_v1%(reg),file=rfile)
		glob.registers.free_register(reg)
	print(glob.jump_epilogue%globals()['fname'],file=globals()['rfile'])

def p_error(p):
	if p:
		print("Syntax error at '{0}' line no  '{1}'".format(p.value,glob.line_number))
	else:
		print("Syntax error at EOF")


def lhs_is_pointer(var_name,indirection,r_reg):
	rfile=globals()['rfile']
	rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
	is_float_reg = glob.registers.is_float_reg(r_reg)

	l_reg = glob.registers.fetch_register()
	if var_name in rt.globals:
		print(glob.lw_glob%(l_reg,var_name),file=rfile)
	else:
		offset = ft.var_offset(var_name,indirection)
		print(glob.lw%(l_reg,offset,'sp'),file=rfile)
	
	for i in  range(indirection - 1):
		t_reg = glob.registers.fetch_register()
		print(glob.lw%(t_reg,0,l_reg),file=rfile)
		glob.registers.free_register(l_reg)
		l_reg = t_reg

	print(glob.sw_map[is_float_reg]%(r_reg,0,l_reg),file=rfile)
	glob.registers.free_register(l_reg)

def lhs_is_temporary(var_name,r_reg):
	rfile=globals()['rfile']
	rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
	is_float_reg = glob.registers.is_float_reg(r_reg)
	l_reg = glob.registers.add_mapping(var_name,is_float=is_float_reg)
	print(glob.move_map[is_float_reg]%(l_reg,r_reg),file=rfile)

def lhs_is_id(var_name,indirection,r_reg):
	rfile=globals()['rfile']
	rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
	is_float_reg = glob.registers.is_float_reg(r_reg)
	if var_name in rt.globals:
		print(glob.sw_glob_map[is_float_reg]%(r_reg,'global_'+var_name),file=rfile)
	else:
		offset = ft.var_offset(var_name, indirection)
		print(glob.sw_map[is_float_reg]%(r_reg,offset,'sp'),file=rfile)

def print_negu(r_reg):
	rfile=globals()['rfile']
	is_float_reg = glob.registers.is_float_reg(r_reg)
	l_reg = glob.registers.fetch_register(is_float = is_float_reg)
	print(glob.negu_map[is_float_reg]%(l_reg,r_reg),file=rfile)
	glob.registers.free_register(r_reg)
	return l_reg

def rhs_pointer(var_name,indirection):
	rfile=globals()['rfile']
	rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
	
	r_reg = glob.registers.fetch_register()
	is_float_var = None

	if var_name in rt.globals:
		is_float_var = rt.is_float_variable(var_name,indirection)
		print(glob.lw_glob%(r_reg,var_name),file=rfile)
	else:
		is_float_var = ft.is_float_variable(var_name,indirection)
		offset = ft.var_offset(var_name, indirection)
		print(glob.lw%(r_reg,offset,'sp'),file=rfile)
	
	for i in range(indirection-1):
		temp_reg = glob.registers.fetch_register()
		print(glob.lw%(temp_reg,0,r_reg),file=rfile)
		glob.registers.free_register(r_reg)
		r_reg = temp_reg

	temp_reg = glob.registers.fetch_register(is_float=is_float_var)
	print(glob.lw_map[is_float_var]%(temp_reg,0,r_reg),file=rfile)
	glob.registers.free_register(r_reg)
	r_reg = temp_reg

	return r_reg

def rhs_temporary(var_name,indirection):
	return glob.registers.get_mapping(var_name)

def rhs_id(var_name,indirection):
	rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
	r_reg = None
	if var_name in rt.globals:
		#Address is always integer
		r_reg = glob.registers.fetch_register()
		print(glob.lw_glob%(r_reg,var_name),file=rfile)
		
		# is_float_var = rt.is_float_variable(var_name,indirection)
		# temp_reg = glob.registers.fetch_register(is_float=is_float_var)
		# print(glob.lw_map[is_float_var]%(temp_reg,0,r_reg),file=rfile)
		# glob.registers.free_register(r_reg)
		# r_reg = temp_reg
	else:
		is_float_var = ft.is_float_variable(var_name,indirection)
		r_reg = glob.registers.fetch_register(is_float=is_float_var)
		offset = ft.var_offset(var_name, indirection)
		print(glob.lw_map[is_float_var]%(r_reg,offset,'sp'),file=rfile) 

	return r_reg

def rhs_const(num,indirection):
	reg = glob.registers.fetch_register()
	print(glob.li%(reg,num),file=globals()['rfile'])
	return reg

def rhs_float(num,indirection):
	reg = glob.registers.fetch_register(is_float=True)
	print(glob.li_s%(reg,num),file=globals()['rfile'])
	return reg

def rhs_address(var_name,indirection):
	rt,ft = glob.root_table, glob.root_table.funclist[globals()['fname']]
	r_reg = glob.registers.fetch_register()
	if var_name in rt.globals:
		print(glob.lw_glob%(r_reg,var_name),file=rfile)
	else:
		offset = ft.var_offset(var_name, indirection)
		print(glob.addi%(r_reg,'sp',offset),file=rfile)
	return r_reg 

def analyse_lhs(token,var_name,indirection,r_reg):
	if token == 'P': lhs_is_pointer(var_name,indirection,r_reg)
	elif token == 'T': lhs_is_temporary(var_name,r_reg)
	elif token == 'I': lhs_is_id(var_name,indirection,r_reg)

def generate_body(data,fname,rfile):
	# print(data)
	globals()['fname'] = fname
	globals()['rfile'] = rfile
	globals()['rhs_functions'] = {
		'P' : rhs_pointer,
		'T' : rhs_temporary,
		'I' : rhs_id,
		'C' : rhs_const,
		'F' : rhs_float,
		'A' : rhs_address
	}
	lex.lex()
	yacc.yacc(debug = False, write_tables = False)
	yacc.parse(data)