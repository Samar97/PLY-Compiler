
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightEQUALSleftORleftANDleftEQUALITYUNEQUALleftLESSERGREATERLESSEREQUALGREATEREQUALleftPLUSMINUSleftTIMESDIVIDErightUMINUSrightAMPERSANDSTARleftIFXleftELSEID NUMBER COMMENT LPAREN RPAREN LBRACE RBRACE SEMICOLON AND OR COMMA PLUS MINUS TIMES DIVIDE EQUALS INT VOID MAIN IF ELSE WHILE LESSER GREATER LESSEREQUAL GREATEREQUAL EQUALITY UNEQUAL\n\tstart : function\n\t\n\tfunction : VOID MAIN LPAREN RPAREN LBRACE statements RBRACE\n\ttype : INT\n\t\t| VOID\t\t\n\t\n\tvar : ID\n\t\n\tconst : NUMBER\n\t\n\tpointer : TIMES pointer %prec STAR\n\t\t\t| TIMES address %prec STAR\n\t\t\t| TIMES var %prec STAR\n\t\n\taddress : AND pointer %prec AMPERSAND\n\t\t\t| AND address %prec AMPERSAND\n\t\t\t| AND var %prec AMPERSAND\n\t\n\tstatements :  statement statements\n\t\t\t\t| \n\tstatement : declaration\n\t\t\t| assignment\n\t\t\t| ifstatement\n\t\t\t| whilestatement\n\t\t\t| COMMENT\n\t\n\tdeclaration : type idlist SEMICOLON\n\t\n\tidlist : pointer COMMA idlist \n\t\t\t| ID COMMA idlist\n\t\t\t| ID\n\t\t\t| pointer\n\t\n\tassignment : pointer EQUALS expression SEMICOLON\n\t\t\t\t| var EQUALS expression SEMICOLON\n\t\n\tcondition :\tcondition LESSER condition\n\t\t\t\t| condition GREATER condition\n\t\t\t\t| condition LESSEREQUAL condition\n\t\t\t\t| condition GREATEREQUAL condition\n\t\t\t\t| condition EQUALITY condition\n\t\t\t\t| condition UNEQUAL condition\n\t\t\t\t| condition AND condition\n\t\t\t\t| condition OR condition\n\t\t\t\t| expression\n\t\n\tcontrolbody : LBRACE statements RBRACE\n\t\t\t| statement\n\t\t\t| SEMICOLON\n\t\n\tifstatement : IF LPAREN condition RPAREN controlbody %prec IFX\n\t\t\t\t| IF LPAREN condition RPAREN controlbody ELSE controlbody\n\t\n\twhilestatement : WHILE LPAREN condition RPAREN controlbody\n\t\n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression TIMES expression\n\t\t\t\t| expression DIVIDE expression\n\t\t\t\t| pointer\n\t\t\t\t| address\n\t\t\t\t| const\n\t\t\t\t| var\n\t\t\t\t| LPAREN expression RPAREN\n\t\n\texpression : MINUS expression %prec UMINUS\n\t'
    
_lr_action_items = {'LBRACE':([6,63,74,94,],[7,83,83,83,]),'NUMBER':([25,26,34,35,42,44,55,56,57,58,59,60,61,62,64,65,66,67,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'MAIN':([2,],[4,]),'LPAREN':([4,13,22,25,26,34,35,42,44,55,56,57,58,59,60,61,62,64,65,66,67,],[5,25,35,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'EQUALITY':([17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,55,-35,-49,-47,-11,-12,-10,55,-51,-31,-29,-30,-27,55,-32,-28,55,-45,-44,-42,-43,-50,]),'GREATEREQUAL':([17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,57,-35,-49,-47,-11,-12,-10,57,-51,57,-29,-30,-27,57,57,-28,57,-45,-44,-42,-43,-50,]),'SEMICOLON':([17,27,29,30,31,32,33,37,38,39,43,45,46,47,48,49,53,63,68,71,72,74,87,88,89,90,91,94,],[-5,-8,-9,-7,-23,51,-24,-6,-48,-46,-49,-47,70,-11,-12,-10,73,84,-51,-22,-21,84,-45,-44,-42,-43,-50,84,]),'$end':([1,3,24,],[-1,0,-2,]),'COMMA':([17,27,29,30,31,33,47,48,49,],[-5,-8,-9,-7,50,52,-11,-12,-10,]),'MINUS':([17,25,26,27,29,30,34,35,37,38,39,41,42,43,44,45,46,47,48,49,53,55,56,57,58,59,60,61,62,64,65,66,67,68,69,87,88,89,90,91,],[-5,42,42,-8,-9,-7,42,42,-6,-48,-46,67,42,-49,42,-47,67,-11,-12,-10,67,42,42,42,42,42,42,42,42,42,42,42,42,-51,67,-45,-44,-42,-43,-50,]),'RPAREN':([5,17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,69,75,76,77,78,79,80,81,82,87,88,89,90,91,],[6,-5,-8,-9,-7,-6,-48,-46,63,-35,-49,-47,-11,-12,-10,74,-51,91,-31,-29,-30,-27,-33,-32,-28,-34,-45,-44,-42,-43,-50,]),'UNEQUAL':([17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,60,-35,-49,-47,-11,-12,-10,60,-51,-31,-29,-30,-27,60,-32,-28,60,-45,-44,-42,-43,-50,]),'DIVIDE':([17,27,29,30,37,38,39,41,43,45,46,47,48,49,53,68,69,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,64,-49,-47,64,-11,-12,-10,64,-51,64,-45,-44,64,64,-50,]),'IF':([7,9,10,12,15,20,23,51,63,70,73,74,83,84,85,86,92,94,95,96,],[13,-15,-16,-18,-19,-17,13,-20,13,-25,-26,13,13,-38,-37,-39,-41,13,-36,-40,]),'OR':([17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,62,-35,-49,-47,-11,-12,-10,62,-51,-31,-29,-30,-27,-33,-32,-28,-34,-45,-44,-42,-43,-50,]),'GREATER':([17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,61,-35,-49,-47,-11,-12,-10,61,-51,61,-29,-30,-27,61,61,-28,61,-45,-44,-42,-43,-50,]),'ID':([7,8,9,10,12,15,16,18,19,20,23,25,26,28,34,35,42,44,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,70,73,74,83,84,85,86,92,94,95,96,],[17,-4,-15,-16,-18,-19,17,-3,31,-17,17,17,17,17,17,17,17,17,31,-20,31,17,17,17,17,17,17,17,17,17,17,17,17,17,-25,-26,17,17,-38,-37,-39,-41,17,-36,-40,]),'TIMES':([7,8,9,10,12,15,16,17,18,19,20,23,25,26,27,28,29,30,34,35,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,73,74,83,84,85,86,87,88,89,90,91,92,94,95,96,],[16,-4,-15,-16,-18,-19,16,-5,-3,16,-17,16,16,16,-8,16,-9,-7,16,16,-6,-48,-46,65,16,-49,16,-47,65,-11,-12,-10,16,-20,16,65,16,16,16,16,16,16,16,16,16,16,16,16,16,-51,65,-25,-26,16,16,-38,-37,-39,-45,-44,65,65,-50,-41,16,-36,-40,]),'COMMENT':([7,9,10,12,15,20,23,51,63,70,73,74,83,84,85,86,92,94,95,96,],[15,-15,-16,-18,-19,-17,15,-20,15,-25,-26,15,15,-38,-37,-39,-41,15,-36,-40,]),'RBRACE':([7,9,10,11,12,15,20,23,36,51,70,73,83,84,85,86,92,93,95,96,],[-14,-15,-16,24,-18,-19,-17,-14,-13,-20,-25,-26,-14,-38,-37,-39,-41,95,-36,-40,]),'LESSEREQUAL':([17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,56,-35,-49,-47,-11,-12,-10,56,-51,56,-29,-30,-27,56,56,-28,56,-45,-44,-42,-43,-50,]),'PLUS':([17,27,29,30,37,38,39,41,43,45,46,47,48,49,53,68,69,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,66,-49,-47,66,-11,-12,-10,66,-51,66,-45,-44,-42,-43,-50,]),'LESSER':([17,27,29,30,37,38,39,40,41,43,45,47,48,49,54,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[-5,-8,-9,-7,-6,-48,-46,58,-35,-49,-47,-11,-12,-10,58,-51,58,-29,-30,-27,58,58,-28,58,-45,-44,-42,-43,-50,]),'WHILE':([7,9,10,12,15,20,23,51,63,70,73,74,83,84,85,86,92,94,95,96,],[22,-15,-16,-18,-19,-17,22,-20,22,-25,-26,22,22,-38,-37,-39,-41,22,-36,-40,]),'AND':([16,17,25,26,27,28,29,30,34,35,37,38,39,40,41,42,43,44,45,47,48,49,54,55,56,57,58,59,60,61,62,64,65,66,67,68,75,76,77,78,79,80,81,82,87,88,89,90,91,],[28,-5,28,28,-8,28,-9,-7,28,28,-6,-48,-46,59,-35,28,-49,28,-47,-11,-12,-10,59,28,28,28,28,28,28,28,28,28,28,28,28,-51,-31,-29,-30,-27,-33,-32,-28,59,-45,-44,-42,-43,-50,]),'INT':([7,9,10,12,15,20,23,51,63,70,73,74,83,84,85,86,92,94,95,96,],[18,-15,-16,-18,-19,-17,18,-20,18,-25,-26,18,18,-38,-37,-39,-41,18,-36,-40,]),'VOID':([0,7,9,10,12,15,20,23,51,63,70,73,74,83,84,85,86,92,94,95,96,],[2,8,-15,-16,-18,-19,-17,8,-20,8,-25,-26,8,8,-38,-37,-39,-41,8,-36,-40,]),'EQUALS':([14,17,21,27,29,30,47,48,49,],[26,-5,34,-8,-9,-7,-11,-12,-10,]),'ELSE':([9,10,12,15,20,51,70,73,84,85,86,92,95,96,],[-15,-16,-18,-19,-17,-20,-25,-26,-38,-37,94,-41,-36,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'const':([25,26,34,35,42,44,55,56,57,58,59,60,61,62,64,65,66,67,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'expression':([25,26,34,35,42,44,55,56,57,58,59,60,61,62,64,65,66,67,],[41,46,53,41,68,69,41,41,41,41,41,41,41,41,87,88,89,90,]),'type':([7,23,63,74,83,94,],[19,19,19,19,19,19,]),'idlist':([19,50,52,],[32,71,72,]),'ifstatement':([7,23,63,74,83,94,],[20,20,20,20,20,20,]),'var':([7,16,23,25,26,28,34,35,42,44,55,56,57,58,59,60,61,62,63,64,65,66,67,74,83,94,],[21,29,21,43,43,48,43,43,43,43,43,43,43,43,43,43,43,43,21,43,43,43,43,21,21,21,]),'start':([0,],[3,]),'assignment':([7,23,63,74,83,94,],[10,10,10,10,10,10,]),'function':([0,],[1,]),'statements':([7,23,83,],[11,36,93,]),'condition':([25,35,55,56,57,58,59,60,61,62,],[40,54,75,76,77,78,79,80,81,82,]),'address':([16,25,26,28,34,35,42,44,55,56,57,58,59,60,61,62,64,65,66,67,],[27,45,45,47,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'whilestatement':([7,23,63,74,83,94,],[12,12,12,12,12,12,]),'controlbody':([63,74,94,],[86,92,96,]),'pointer':([7,16,19,23,25,26,28,34,35,42,44,50,52,55,56,57,58,59,60,61,62,63,64,65,66,67,74,83,94,],[14,30,33,14,39,39,49,39,39,39,39,33,33,39,39,39,39,39,39,39,39,14,39,39,39,39,14,14,14,]),'statement':([7,23,63,74,83,94,],[23,23,85,85,23,85,]),'declaration':([7,23,63,74,83,94,],[9,9,9,9,9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> function','start',1,'p_start','assign3.py',101),
  ('function -> VOID MAIN LPAREN RPAREN LBRACE statements RBRACE','function',7,'p_function','assign3.py',114),
  ('type -> INT','type',1,'p_function','assign3.py',115),
  ('type -> VOID','type',1,'p_function','assign3.py',116),
  ('var -> ID','var',1,'p_var','assign3.py',122),
  ('const -> NUMBER','const',1,'p_const','assign3.py',128),
  ('pointer -> TIMES pointer','pointer',2,'p_pointer','assign3.py',135),
  ('pointer -> TIMES address','pointer',2,'p_pointer','assign3.py',136),
  ('pointer -> TIMES var','pointer',2,'p_pointer','assign3.py',137),
  ('address -> AND pointer','address',2,'p_address','assign3.py',143),
  ('address -> AND address','address',2,'p_address','assign3.py',144),
  ('address -> AND var','address',2,'p_address','assign3.py',145),
  ('statements -> statement statements','statements',2,'p_statements','assign3.py',151),
  ('statements -> <empty>','statements',0,'p_statements','assign3.py',152),
  ('statement -> declaration','statement',1,'p_statements','assign3.py',153),
  ('statement -> assignment','statement',1,'p_statements','assign3.py',154),
  ('statement -> ifstatement','statement',1,'p_statements','assign3.py',155),
  ('statement -> whilestatement','statement',1,'p_statements','assign3.py',156),
  ('statement -> COMMENT','statement',1,'p_statements','assign3.py',157),
  ('declaration -> type idlist SEMICOLON','declaration',3,'p_declaration','assign3.py',163),
  ('idlist -> pointer COMMA idlist','idlist',3,'p_idlist','assign3.py',169),
  ('idlist -> ID COMMA idlist','idlist',3,'p_idlist','assign3.py',170),
  ('idlist -> ID','idlist',1,'p_idlist','assign3.py',171),
  ('idlist -> pointer','idlist',1,'p_idlist','assign3.py',172),
  ('assignment -> pointer EQUALS expression SEMICOLON','assignment',4,'p_assignment','assign3.py',178),
  ('assignment -> var EQUALS expression SEMICOLON','assignment',4,'p_assignment','assign3.py',179),
  ('condition -> condition LESSER condition','condition',3,'p_condition','assign3.py',188),
  ('condition -> condition GREATER condition','condition',3,'p_condition','assign3.py',189),
  ('condition -> condition LESSEREQUAL condition','condition',3,'p_condition','assign3.py',190),
  ('condition -> condition GREATEREQUAL condition','condition',3,'p_condition','assign3.py',191),
  ('condition -> condition EQUALITY condition','condition',3,'p_condition','assign3.py',192),
  ('condition -> condition UNEQUAL condition','condition',3,'p_condition','assign3.py',193),
  ('condition -> condition AND condition','condition',3,'p_condition','assign3.py',194),
  ('condition -> condition OR condition','condition',3,'p_condition','assign3.py',195),
  ('condition -> expression','condition',1,'p_condition','assign3.py',196),
  ('controlbody -> LBRACE statements RBRACE','controlbody',3,'p_controlbody','assign3.py',202),
  ('controlbody -> statement','controlbody',1,'p_controlbody','assign3.py',203),
  ('controlbody -> SEMICOLON','controlbody',1,'p_controlbody','assign3.py',204),
  ('ifstatement -> IF LPAREN condition RPAREN controlbody','ifstatement',5,'p_ifstatement','assign3.py',210),
  ('ifstatement -> IF LPAREN condition RPAREN controlbody ELSE controlbody','ifstatement',7,'p_ifstatement','assign3.py',211),
  ('whilestatement -> WHILE LPAREN condition RPAREN controlbody','whilestatement',5,'p_whilestatement','assign3.py',217),
  ('expression -> expression PLUS expression','expression',3,'p_expression','assign3.py',225),
  ('expression -> expression MINUS expression','expression',3,'p_expression','assign3.py',226),
  ('expression -> expression TIMES expression','expression',3,'p_expression','assign3.py',227),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','assign3.py',228),
  ('expression -> pointer','expression',1,'p_expression','assign3.py',229),
  ('expression -> address','expression',1,'p_expression','assign3.py',230),
  ('expression -> const','expression',1,'p_expression','assign3.py',231),
  ('expression -> var','expression',1,'p_expression','assign3.py',232),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','assign3.py',233),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','assign3.py',250),
]