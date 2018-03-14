
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightEQUALSleftORleftANDleftEQNENOTleftLTGTLEGEleftPLUSMINUSleftTIMESDIVIDErightUMINUSrightAMPERSANDSTARleftIFXleftELSEID NUMBER COMMENT LPAREN RPAREN LBRACE RBRACE SEMICOLON AMPERSAND COMMA PLUS MINUS TIMES DIVIDE EQUALS INT VOID FLOAT MAIN IF ELSE WHILE LT GT LE GE EQ NE NOT AND OR\n\tprogram : declarations funcdefs\n\t\n\tfuncdefs : function funcdefs\n\t\t\t| function\n\t\n\tdeclarations : declarations declaration\n\t\t\t\t|\n\t\n\tfunction : type fname LPAREN args RPAREN LBRACE statements RBRACE\n\t\n\ttype : INT\n\t\t| VOID\n\t\t| FLOAT\n\t\n\tfname : ID\n\t\t  | MAIN\n\t\n\targs : arg argcomp\n\t\t|\n\targcomp : COMMA arg argcomp\n\t\t|  \n\t\n\targ : type param\n\tparam : var \n\t\t| pointer \n\t\t| address\n\t\n\tvar : ID\n\t\n\tconst : NUMBER\n\t\t| FLOAT\n\t\n\tpointer : TIMES pointer %prec STAR\n\t\t\t| TIMES address %prec STAR\n\t\t\t| TIMES var %prec STAR\n\t\n\taddress : AMPERSAND pointer\n\t\t\t| AMPERSAND address\n\t\t\t| AMPERSAND var\n\t\n\tvoidfuncall : funcall SEMICOLON\n\t\n\tfuncall : var LPAREN params RPAREN\n\tparams : callparam paramcomp\n\t\t\t|\n\tparamcomp : COMMA callparam paramcomp\n\t\t\t| \n\tcallparam : param\n\t\t\t| const\n\t\n\tstatements :  statement statements\n\t\t\t\t| COMMENT statements\n\t\t\t\t| declaration statements\n\t\t\t\t| voidfuncall statements\n\t\t\t\t| \n\tstatement : assignment\n\t\t\t| ifstatement\n\t\t\t| whilestatement\n\t\n\tdeclaration : type idlist SEMICOLON\n\t\n\tidlist : pointer COMMA idlist \n\t\t\t| var COMMA idlist\n\t\t\t| var\n\t\t\t| pointer\n\t\n\tassignment : pointer EQUALS expression SEMICOLON\n\t\t\t\t| var EQUALS expression SEMICOLON\n\t\n\tcondition :\texpression LT expression\n\t\t\t\t| expression GT expression\n\t\t\t\t| expression LE expression\n\t\t\t\t| expression GE expression\n\t\t\t\t| expression EQ expression\n\t\t\t\t| expression NE expression\n\t\t\t\t| condition AND condition\n\t\t\t\t| condition OR condition\n\t\t\t\t| NOT condition\n\t\t\t\t| LPAREN condition RPAREN\n\t\n\tcontrolbody : LBRACE statements RBRACE\n\t\t\t| statement\n\t\t\t| SEMICOLON\n\t\n\tifstatement : IF LPAREN condition RPAREN controlbody %prec IFX\n\t\t\t\t| IF LPAREN condition RPAREN controlbody ELSE controlbody\n\t\n\twhilestatement : WHILE LPAREN condition RPAREN controlbody\n\t\n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression TIMES expression\n\t\t\t\t| expression DIVIDE expression\n\t\t\t\t| pointer\n\t\t\t\t| address\n\t\t\t\t| const\n\t\t\t\t| var\n\t\t\t\t| funcall\n\t\t\t\t| LPAREN expression RPAREN\n\t\n\texpression : MINUS expression %prec UMINUS\n\t'
    
_lr_action_items = {'VOID':([0,2,3,8,20,27,38,44,50,51,54,55,56,57,59,61,62,110,111,119,120,121,123,136,140,141,],[-5,6,6,-4,-45,6,6,6,6,-44,6,6,-42,6,-43,-6,-29,-50,-51,-64,-67,-63,6,-65,-62,-66,]),'NUMBER':([63,64,66,67,71,75,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,113,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'WHILE':([20,44,50,51,54,55,56,57,59,62,96,110,111,115,119,120,121,123,136,139,140,141,],[-45,48,48,-44,48,48,-42,48,-43,-29,48,-50,-51,48,-64,-67,-63,48,-65,48,-62,-66,]),'MINUS':([23,24,25,26,30,31,32,63,64,66,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,92,94,95,97,99,100,101,102,103,104,105,106,107,108,109,114,117,125,126,127,128,129,130,131,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,75,75,75,75,-21,-76,-72,75,-75,75,-73,-74,-22,75,108,75,108,108,-78,108,75,75,75,75,75,75,75,75,75,75,75,75,108,-30,-77,108,-71,108,108,108,108,108,-68,-70,-69,]),'RBRACE':([20,44,46,50,51,54,55,56,57,59,62,65,68,69,70,110,111,119,120,121,123,136,137,140,141,],[-45,-41,61,-41,-44,-41,-41,-42,-41,-43,-29,-38,-40,-37,-39,-50,-51,-64,-67,-63,-41,-65,140,-62,-66,]),'COMMENT':([20,44,50,51,54,55,56,57,59,62,110,111,119,120,121,123,136,140,141,],[-45,50,50,-44,50,50,-42,50,-43,-29,-50,-51,-64,-67,-63,50,-65,-62,-66,]),'LE':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,92,94,114,117,126,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,105,-78,105,-30,-77,-71,-68,-70,-69,]),'RPAREN':([23,24,25,26,27,30,31,32,33,34,39,40,41,42,43,45,60,67,72,73,74,76,78,79,80,81,87,88,89,90,91,92,93,94,98,109,112,114,116,117,118,124,125,126,127,128,129,130,131,132,133,134,135,138,],[-24,-25,-23,-20,-13,-27,-28,-26,37,-15,-12,-16,-19,-17,-18,-15,-14,-32,-21,-76,-72,-75,-73,-74,96,-22,-35,-34,114,-36,115,-78,116,117,-60,117,-31,-30,-61,-77,-58,-59,-53,-71,-56,-52,-57,-55,-54,-68,-70,-69,-34,-33,]),'SEMICOLON':([12,13,16,18,23,24,25,26,29,30,31,32,36,47,72,73,74,76,78,79,81,85,86,92,96,114,115,117,126,132,133,134,139,],[20,-49,-48,-20,-24,-25,-23,-20,-46,-27,-28,-26,-47,62,-21,-76,-72,-75,-73,-74,-22,110,111,-78,119,-30,119,-77,-71,-68,-70,-69,119,]),'NE':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,92,94,114,117,126,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,103,-78,103,-30,-77,-71,-68,-70,-69,]),'LT':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,92,94,114,117,126,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,102,-78,102,-30,-77,-71,-68,-70,-69,]),'COMMA':([13,16,18,23,24,25,26,30,31,32,34,40,41,42,43,45,72,81,87,88,90,135,],[21,28,-20,-24,-25,-23,-20,-27,-28,-26,38,-16,-19,-17,-18,38,-21,-22,-35,113,-36,113,]),'PLUS':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,85,86,92,94,109,114,117,125,126,127,128,129,130,131,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,106,106,106,-78,106,106,-30,-77,106,-71,106,106,106,106,106,-68,-70,-69,]),'$end':([1,3,4,10,61,],[0,-3,-1,-2,-6,]),'GT':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,92,94,114,117,126,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,99,-78,99,-30,-77,-71,-68,-70,-69,]),'DIVIDE':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,85,86,92,94,109,114,117,125,126,127,128,129,130,131,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,100,100,100,-78,100,100,-30,-77,100,-71,100,100,100,100,100,100,-70,100,]),'EQUALS':([23,24,25,26,30,31,32,49,52,122,],[-24,-25,-23,-20,-27,-28,-26,64,66,66,]),'TIMES':([5,6,7,9,14,20,21,22,23,24,25,26,28,30,31,32,35,44,50,51,53,54,55,56,57,59,62,63,64,66,67,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,92,94,95,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,113,114,115,117,119,120,121,123,125,126,127,128,129,130,131,132,133,134,136,139,140,141,],[-7,-8,-9,14,14,-45,14,14,-24,-25,-23,-20,14,-27,-28,-26,14,14,14,-44,14,14,14,-42,14,-43,-29,14,14,14,14,14,-21,-76,-72,14,-75,14,-73,-74,-22,14,107,14,107,107,-78,107,14,14,14,14,14,14,14,14,14,14,14,14,14,107,-50,-51,14,-30,14,-77,-64,-67,-63,14,107,-71,107,107,107,107,107,107,-70,107,-65,14,-62,-66,]),'GE':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,92,94,114,117,126,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,104,-78,104,-30,-77,-71,-68,-70,-69,]),'AMPERSAND':([5,6,7,14,22,35,63,64,66,67,71,75,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,113,],[-7,-8,-9,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'LPAREN':([15,17,18,19,26,48,52,58,63,64,66,71,75,76,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,],[27,-11,-10,-10,-20,63,67,71,77,84,84,77,84,67,77,77,84,77,77,84,84,84,84,84,84,84,84,84,84,]),'ELSE':([51,56,59,110,111,119,120,121,136,140,141,],[-44,-42,-43,-50,-51,-64,-67,-63,139,-62,-66,]),'EQ':([23,24,25,26,30,31,32,72,73,74,76,78,79,81,83,92,94,114,117,126,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,-22,101,-78,101,-30,-77,-71,-68,-70,-69,]),'ID':([5,6,7,9,11,14,20,21,22,28,35,44,50,51,53,54,55,56,57,59,62,63,64,66,67,71,75,77,82,84,95,96,97,99,100,101,102,103,104,105,106,107,108,110,111,113,115,119,120,121,123,136,139,140,141,],[-7,-8,-9,18,19,26,-45,26,26,26,26,26,26,-44,26,26,26,-42,26,-43,-29,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-50,-51,26,26,-64,-67,-63,26,-65,26,-62,-66,]),'IF':([20,44,50,51,54,55,56,57,59,62,96,110,111,115,119,120,121,123,136,139,140,141,],[-45,58,58,-44,58,58,-42,58,-43,-29,58,-50,-51,58,-64,-67,-63,58,-65,58,-62,-66,]),'AND':([23,24,25,26,30,31,32,72,73,74,76,78,79,80,81,91,92,93,98,114,116,117,118,124,125,126,127,128,129,130,131,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,95,-22,95,-78,95,-60,-30,-61,-77,-58,95,-53,-71,-56,-52,-57,-55,-54,-68,-70,-69,]),'LBRACE':([37,96,115,139,],[44,123,123,123,]),'INT':([0,2,3,8,20,27,38,44,50,51,54,55,56,57,59,61,62,110,111,119,120,121,123,136,140,141,],[-5,5,5,-4,-45,5,5,5,5,-44,5,5,-42,5,-43,-6,-29,-50,-51,-64,-67,-63,5,-65,-62,-66,]),'FLOAT':([0,2,3,8,20,27,38,44,50,51,54,55,56,57,59,61,62,63,64,66,67,71,75,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,110,111,113,119,120,121,123,136,140,141,],[-5,7,7,-4,-45,7,7,7,7,-44,7,7,-42,7,-43,-6,-29,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,-50,-51,81,-64,-67,-63,7,-65,-62,-66,]),'NOT':([63,71,77,82,95,97,],[82,82,82,82,82,82,]),'MAIN':([5,6,7,9,11,],[-7,-8,-9,17,17,]),'OR':([23,24,25,26,30,31,32,72,73,74,76,78,79,80,81,91,92,93,98,114,116,117,118,124,125,126,127,128,129,130,131,132,133,134,],[-24,-25,-23,-20,-27,-28,-26,-21,-76,-72,-75,-73,-74,97,-22,97,-78,97,-60,-30,-61,-77,-58,-59,-53,-71,-56,-52,-57,-55,-54,-68,-70,-69,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([44,50,54,55,57,123,],[46,65,68,69,70,137,]),'address':([14,22,35,63,64,66,67,71,75,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,113,],[23,30,41,78,78,78,41,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,41,]),'funcall':([44,50,54,55,57,63,64,66,71,75,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,123,],[47,47,47,47,47,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,47,]),'arg':([27,38,],[34,45,]),'pointer':([9,14,21,22,28,35,44,50,53,54,55,57,63,64,66,67,71,75,77,82,84,95,96,97,99,100,101,102,103,104,105,106,107,108,113,115,123,139,],[13,25,13,32,13,43,49,49,13,49,49,49,74,74,74,43,74,74,74,74,74,74,49,74,74,74,74,74,74,74,74,74,74,74,43,49,49,49,]),'const':([63,64,66,67,71,75,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,113,],[79,79,79,90,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,90,]),'funcdefs':([2,3,],[4,10,]),'controlbody':([96,115,139,],[120,136,141,]),'whilestatement':([44,50,54,55,57,96,115,123,139,],[51,51,51,51,51,51,51,51,51,]),'param':([35,67,113,],[40,87,87,]),'callparam':([67,113,],[88,135,]),'program':([0,],[1,]),'params':([67,],[89,]),'statement':([44,50,54,55,57,96,115,123,139,],[55,55,55,55,55,121,121,55,121,]),'var':([9,14,21,22,28,35,44,50,53,54,55,57,63,64,66,67,71,75,77,82,84,95,96,97,99,100,101,102,103,104,105,106,107,108,113,115,123,139,],[16,24,16,31,16,42,52,52,16,52,52,52,76,76,76,42,76,76,76,76,76,76,122,76,76,76,76,76,76,76,76,76,76,76,42,122,52,122,]),'type':([2,3,27,38,44,50,54,55,57,123,],[9,11,35,35,53,53,53,53,53,53,]),'voidfuncall':([44,50,54,55,57,123,],[54,54,54,54,54,54,]),'function':([2,3,],[3,3,]),'fname':([9,11,],[15,15,]),'argcomp':([34,45,],[39,60,]),'assignment':([44,50,54,55,57,96,115,123,139,],[56,56,56,56,56,56,56,56,56,]),'args':([27,],[33,]),'declaration':([2,44,50,54,55,57,123,],[8,57,57,57,57,57,57,]),'paramcomp':([88,135,],[112,138,]),'condition':([63,71,77,82,95,97,],[80,91,93,98,118,124,]),'idlist':([9,21,28,53,],[12,29,36,12,]),'declarations':([0,],[2,]),'expression':([63,64,66,71,75,77,82,84,95,97,99,100,101,102,103,104,105,106,107,108,],[83,85,86,83,92,94,83,109,83,83,125,126,127,128,129,130,131,132,133,134,]),'ifstatement':([44,50,54,55,57,96,115,123,139,],[59,59,59,59,59,59,59,59,59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declarations funcdefs','program',2,'p_program','Parser.py',116),
  ('funcdefs -> function funcdefs','funcdefs',2,'p_funcdefs','Parser.py',127),
  ('funcdefs -> function','funcdefs',1,'p_funcdefs','Parser.py',128),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','Parser.py',138),
  ('declarations -> <empty>','declarations',0,'p_declarations','Parser.py',139),
  ('function -> type fname LPAREN args RPAREN LBRACE statements RBRACE','function',8,'p_function','Parser.py',149),
  ('type -> INT','type',1,'p_type','Parser.py',160),
  ('type -> VOID','type',1,'p_type','Parser.py',161),
  ('type -> FLOAT','type',1,'p_type','Parser.py',162),
  ('fname -> ID','fname',1,'p_fname','Parser.py',168),
  ('fname -> MAIN','fname',1,'p_fname','Parser.py',169),
  ('args -> arg argcomp','args',2,'p_args','Parser.py',178),
  ('args -> <empty>','args',0,'p_args','Parser.py',179),
  ('argcomp -> COMMA arg argcomp','argcomp',3,'p_args','Parser.py',180),
  ('argcomp -> <empty>','argcomp',0,'p_args','Parser.py',181),
  ('arg -> type param','arg',2,'p_arg','Parser.py',187),
  ('param -> var','param',1,'p_arg','Parser.py',188),
  ('param -> pointer','param',1,'p_arg','Parser.py',189),
  ('param -> address','param',1,'p_arg','Parser.py',190),
  ('var -> ID','var',1,'p_var','Parser.py',201),
  ('const -> NUMBER','const',1,'p_const','Parser.py',208),
  ('const -> FLOAT','const',1,'p_const','Parser.py',209),
  ('pointer -> TIMES pointer','pointer',2,'p_pointer','Parser.py',217),
  ('pointer -> TIMES address','pointer',2,'p_pointer','Parser.py',218),
  ('pointer -> TIMES var','pointer',2,'p_pointer','Parser.py',219),
  ('address -> AMPERSAND pointer','address',2,'p_address','Parser.py',226),
  ('address -> AMPERSAND address','address',2,'p_address','Parser.py',227),
  ('address -> AMPERSAND var','address',2,'p_address','Parser.py',228),
  ('voidfuncall -> funcall SEMICOLON','voidfuncall',2,'p_voidfuncall','Parser.py',234),
  ('funcall -> var LPAREN params RPAREN','funcall',4,'p_funcall','Parser.py',240),
  ('params -> callparam paramcomp','params',2,'p_funcall','Parser.py',241),
  ('params -> <empty>','params',0,'p_funcall','Parser.py',242),
  ('paramcomp -> COMMA callparam paramcomp','paramcomp',3,'p_funcall','Parser.py',243),
  ('paramcomp -> <empty>','paramcomp',0,'p_funcall','Parser.py',244),
  ('callparam -> param','callparam',1,'p_funcall','Parser.py',245),
  ('callparam -> const','callparam',1,'p_funcall','Parser.py',246),
  ('statements -> statement statements','statements',2,'p_statements','Parser.py',253),
  ('statements -> COMMENT statements','statements',2,'p_statements','Parser.py',254),
  ('statements -> declaration statements','statements',2,'p_statements','Parser.py',255),
  ('statements -> voidfuncall statements','statements',2,'p_statements','Parser.py',256),
  ('statements -> <empty>','statements',0,'p_statements','Parser.py',257),
  ('statement -> assignment','statement',1,'p_statements','Parser.py',258),
  ('statement -> ifstatement','statement',1,'p_statements','Parser.py',259),
  ('statement -> whilestatement','statement',1,'p_statements','Parser.py',260),
  ('declaration -> type idlist SEMICOLON','declaration',3,'p_declaration','Parser.py',278),
  ('idlist -> pointer COMMA idlist','idlist',3,'p_idlist','Parser.py',287),
  ('idlist -> var COMMA idlist','idlist',3,'p_idlist','Parser.py',288),
  ('idlist -> var','idlist',1,'p_idlist','Parser.py',289),
  ('idlist -> pointer','idlist',1,'p_idlist','Parser.py',290),
  ('assignment -> pointer EQUALS expression SEMICOLON','assignment',4,'p_assignment','Parser.py',300),
  ('assignment -> var EQUALS expression SEMICOLON','assignment',4,'p_assignment','Parser.py',301),
  ('condition -> expression LT expression','condition',3,'p_condition','Parser.py',307),
  ('condition -> expression GT expression','condition',3,'p_condition','Parser.py',308),
  ('condition -> expression LE expression','condition',3,'p_condition','Parser.py',309),
  ('condition -> expression GE expression','condition',3,'p_condition','Parser.py',310),
  ('condition -> expression EQ expression','condition',3,'p_condition','Parser.py',311),
  ('condition -> expression NE expression','condition',3,'p_condition','Parser.py',312),
  ('condition -> condition AND condition','condition',3,'p_condition','Parser.py',313),
  ('condition -> condition OR condition','condition',3,'p_condition','Parser.py',314),
  ('condition -> NOT condition','condition',2,'p_condition','Parser.py',315),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_condition','Parser.py',316),
  ('controlbody -> LBRACE statements RBRACE','controlbody',3,'p_controlbody','Parser.py',341),
  ('controlbody -> statement','controlbody',1,'p_controlbody','Parser.py',342),
  ('controlbody -> SEMICOLON','controlbody',1,'p_controlbody','Parser.py',343),
  ('ifstatement -> IF LPAREN condition RPAREN controlbody','ifstatement',5,'p_ifstatement','Parser.py',354),
  ('ifstatement -> IF LPAREN condition RPAREN controlbody ELSE controlbody','ifstatement',7,'p_ifstatement','Parser.py',355),
  ('whilestatement -> WHILE LPAREN condition RPAREN controlbody','whilestatement',5,'p_whilestatement','Parser.py',364),
  ('expression -> expression PLUS expression','expression',3,'p_expression','Parser.py',371),
  ('expression -> expression MINUS expression','expression',3,'p_expression','Parser.py',372),
  ('expression -> expression TIMES expression','expression',3,'p_expression','Parser.py',373),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','Parser.py',374),
  ('expression -> pointer','expression',1,'p_expression','Parser.py',375),
  ('expression -> address','expression',1,'p_expression','Parser.py',376),
  ('expression -> const','expression',1,'p_expression','Parser.py',377),
  ('expression -> var','expression',1,'p_expression','Parser.py',378),
  ('expression -> funcall','expression',1,'p_expression','Parser.py',379),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','Parser.py',380),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','Parser.py',397),
]
