from src.JavaScriptParserVisitor import JavaScriptParserVisitor
if __name__ is not None and "." in __name__:
    from src.JavaScriptParser import JavaScriptParser
else:
    from JavaScriptParser import JavaScriptParser



class AstVisitor(JavaScriptParserVisitor):

    def __init__(self):
        self.nest_level = 0
        self.tree = ""

    def addNode(self, node: str):
        self.tree += node

    def printNewLine(self):
        string = '\n' + '-' * int(self.nest_level) * 4
        self.addNode(string)

    def visitChild(self, child, child_name=None):
        if child_name is None:
            child.accept(self)
            return

        self.printNewLine()
        self.addNode(child_name)
        self.nest_level += 1
        child.accept(self)
        self.nest_level -= 1


    # Visit a parse tree produced by JavaScriptParser#program.
    def visitProgram(self, ctx:JavaScriptParser.ProgramContext):
        self.addNode('Program')
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#sourceElement.
    def visitSourceElement(self, ctx:JavaScriptParser.SourceElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#statement.
    def visitStatement(self, ctx:JavaScriptParser.StatementContext):
        result = self.visitChildren(ctx)
        return result


    # Visit a parse tree produced by JavaScriptParser#block.
    def visitBlock(self, ctx:JavaScriptParser.BlockContext):
        self.printNewLine()
        self.addNode('Block')
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result

    # Visit a parse tree produced by JavaScriptParser#statementList.
    def visitStatementList(self, ctx:JavaScriptParser.StatementListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaScriptParser#importStatement.
    def visitImportStatement(self, ctx:JavaScriptParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importFromBlock.
    def visitImportFromBlock(self, ctx:JavaScriptParser.ImportFromBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#moduleItems.
    def visitModuleItems(self, ctx:JavaScriptParser.ModuleItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importDefault.
    def visitImportDefault(self, ctx:JavaScriptParser.ImportDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importNamespace.
    def visitImportNamespace(self, ctx:JavaScriptParser.ImportNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importFrom.
    def visitImportFrom(self, ctx:JavaScriptParser.ImportFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#aliasName.
    def visitAliasName(self, ctx:JavaScriptParser.AliasNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ExportDeclaration.
    def visitExportDeclaration(self, ctx:JavaScriptParser.ExportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ExportDefaultDeclaration.
    def visitExportDefaultDeclaration(self, ctx:JavaScriptParser.ExportDefaultDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#exportFromBlock.
    def visitExportFromBlock(self, ctx:JavaScriptParser.ExportFromBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#declaration.
    def visitDeclaration(self, ctx:JavaScriptParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableStatement.
    def visitVariableStatement(self, ctx:JavaScriptParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:JavaScriptParser.VariableDeclarationListContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('VariableDeclarationList')
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('VariableDeclaration')
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx:JavaScriptParser.EmptyStatementContext):
        self.printNewLine()
        self.addNode('EmptyStatement')
        return None

    # Visit a parse tree produced by JavaScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ifStatement.
    def visitIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        self.printNewLine()
        self.addNode('IfStatement')
        self.nest_level += 1

        test = ctx.expressionSequence()
        self.visitChild(test, 'Test')

        consequent = ctx.statement(0)
        self.visitChild(consequent, 'Consequent')

        if ctx.Else():
            alternate = ctx.statement(1)
            self.visitChild(alternate, "Alternate")

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#DoStatement.
    def visitDoStatement(self, ctx:JavaScriptParser.DoStatementContext):
        self.printNewLine()
        self.addNode('DoStatement')
        self.nest_level += 1

        body = ctx.statement()
        self.visitChild(body, 'Body')

        test = ctx.expressionSequence()
        self.visitChild(test, 'Test')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx:JavaScriptParser.WhileStatementContext):
        self.printNewLine()
        self.addNode('WhileStatement')
        self.nest_level += 1

        test = ctx.expressionSequence()
        self.visitChild(test, 'Test')

        body = ctx.statement()
        self.visitChild(body, 'Body')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ForStatement.
    def visitForStatement(self, ctx:JavaScriptParser.ForStatementContext):
        self.printNewLine()
        self.addNode('ForStatement')
        self.nest_level += 1

        i = 0
        if not (init := ctx.variableDeclarationList()):
            init = ctx.expressionSequence(i)
            i += 1
        if init:
            self.visitChild(init, 'Init')

        if test := ctx.expressionSequence(i):
            self.visitChild(test, 'Test')

        if update := ctx.expressionSequence(++i):
            self.visitChild(update, 'Update')

        if body := ctx.statement():
            self.visitChild(body, 'Body')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ForInStatement.
    def visitForInStatement(self, ctx:JavaScriptParser.ForInStatementContext):
        self.printNewLine()
        self.addNode('ForInStatement:')
        self.nest_level += 1

        if not (left := ctx.variableDeclarationList()):
            left = ctx.singleExpression()
        if left:
            self.visitChild(left, 'Left')

        if right := ctx.expressionSequence():
            self.visitChild(right, 'Right')

        if body := ctx.statement():
            self.visitChild(body, 'Body')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#ForOfStatement.
    def visitForOfStatement(self, ctx:JavaScriptParser.ForOfStatementContext):
        self.printNewLine()
        self.addNode('ForOfStatement')
        self.nest_level += 1

        if not (left := ctx.variableDeclarationList()):
            left = ctx.singleExpression()
        self.visitChild(left, 'Left')

        if (right := ctx.expressionSequence()):
            self.visitChild(right, 'Right')

        if (body := ctx.statement()):
            self.visitChild(body, 'Body')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#varModifier.
    def visitVarModifier(self, ctx:JavaScriptParser.VarModifierContext):
        self.printNewLine()
        self.addNode('VarModifier: ')
        var_modifier = None
        if ctx.Var():
            var_modifier = 'var'
        elif ctx.Const():
            var_modifier = 'const'
        elif ctx.let():
            var_modifier = 'let'
        self.addNode(var_modifier)
        return None


    # Visit a parse tree produced by JavaScriptParser#continueStatement.
    def visitContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        self.printNewLine()
        self.addNode('ContinueStatement')
        if ctx.identifier():
            self.nest_level += 1
            ctx.identifier().accept(self)
            self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        self.printNewLine()
        self.addNode('BreakStatement')
        if ctx.identifier():
            self.nest_level += 1
            ctx.identifier().accept(self)
            self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        self.printNewLine()
        self.addNode('ReturnStatement')
        self.nest_level += 1
        if ctx.expressionSequence():
            self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#yieldStatement.
    def visitYieldStatement(self, ctx:JavaScriptParser.YieldStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#withStatement.
    def visitWithStatement(self, ctx:JavaScriptParser.WithStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx:JavaScriptParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseBlock.
    def visitCaseBlock(self, ctx:JavaScriptParser.CaseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseClauses.
    def visitCaseClauses(self, ctx:JavaScriptParser.CaseClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseClause.
    def visitCaseClause(self, ctx:JavaScriptParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#defaultClause.
    def visitDefaultClause(self, ctx:JavaScriptParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx:JavaScriptParser.LabelledStatementContext):
        return None


    # Visit a parse tree produced by JavaScriptParser#throwStatement.
    def visitThrowStatement(self, ctx:JavaScriptParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#tryStatement.
    def visitTryStatement(self, ctx:JavaScriptParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#catchProduction.
    def visitCatchProduction(self, ctx:JavaScriptParser.CatchProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx:JavaScriptParser.FinallyProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx:JavaScriptParser.DebuggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        self.printNewLine()
        self.addNode('FunctionDeclaration')
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result



    # Visit a parse tree produced by JavaScriptParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        self.printNewLine()
        self.addNode("ClassDeclaration: not implemented")
        return None


    # Visit a parse tree produced by JavaScriptParser#classTail.
    def visitClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        self.printNewLine()
        self.addNode("ClassTail: not implemented")
        return None


    # Visit a parse tree produced by JavaScriptParser#classElement.
    def visitClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        self.printNewLine()
        self.addNode("ClassElement: not implemented")
        return None


    # Visit a parse tree produced by JavaScriptParser#methodDefinition.
    def visitMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        self.printNewLine()
        self.addNode("ClassDeclaration: not implemented")
        return None


    # Visit a parse tree produced by JavaScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        self.printNewLine()
        self.addNode('ParameterList')
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#formalParameterArg.
    def visitFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        self.printNewLine()
        self.addNode('FormalParameterArg')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1

    # Visit a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def visitLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        self.printNewLine()
        self.addNode("LastFormalParameterArg: not implemented")
        return None

    # Visit a parse tree produced by JavaScriptParser#functionBody.
    def visitFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        self.printNewLine()
        self.addNode('FunctionBody')
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#sourceElements.
    def visitSourceElements(self, ctx:JavaScriptParser.SourceElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:JavaScriptParser.ArrayLiteralContext):
        self.printNewLine()
        self.addNode('ArrayLiteral')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1


    # Visit a parse tree produced by JavaScriptParser#elementList.
    def visitElementList(self, ctx:JavaScriptParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrayElement.
    def visitArrayElement(self, ctx:JavaScriptParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:JavaScriptParser.PropertyExpressionAssignmentContext):
        # isn't it PropertyAssignmentExpression ?
        self.printNewLine()
        self.addNode('PropertyAssignment')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def visitComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        self.printNewLine()
        self.addNode("ComputedPropertyExpressionAssignment: not implemented")
        return None


    # Visit a parse tree produced by JavaScriptParser#FunctionProperty.
    def visitFunctionProperty(self, ctx:JavaScriptParser.FunctionPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        self.printNewLine()
        self.addNode('PropertyGetter')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        self.printNewLine()
        self.addNode('PropertySetter')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#PropertyShorthand.
    def visitPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        self.printNewLine()
        self.addNode('PropertyShorthand: not implemented')
        return None

    # Visit a parse tree produced by JavaScriptParser#propertyName.
    def visitPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        self.printNewLine()
        self.addNode('PropertyName')
        self.nest_level += 1

        if ctx.singleExpression() or ctx.identifierName():
            self.visitChildren(ctx)
        else:
            self.printNewLine()
            if ctx.StringLiteral():
                self.addNode(ctx.StringLiteral().getText())
            elif ctx.numericLiteral():
                self.addNode(ctx.numericLiteral().getText())

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#arguments.
    def visitArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        self.printNewLine()
        self.addNode('Arguments')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#argument.
    def visitArgument(self, ctx:JavaScriptParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx:JavaScriptParser.ExpressionSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TemplateStringExpression.
    def visitTemplateStringExpression(self, ctx:JavaScriptParser.TemplateStringExpressionContext):
        self.printNewLine()
        self.addNode('TemplateStringExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        self.printNewLine()
        self.addNode('TernaryExpression')
        self.nest_level += 1

        test = ctx.singleExpression(0)
        self.visitChild(test, 'Test')

        consequent = ctx.singleExpression(1)
        self.visitChild(consequent, 'Consequent')

        alternate = ctx.singleExpression(2)
        self.visitChild(alternate, "Alternate")

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:JavaScriptParser.LogicalAndExpressionContext):
        self.printNewLine()
        self.addNode('LogicalAndExpression')
        self.nest_level += 1

        self.printNewLine()
        self.addNode('Operator: &&')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#PowerExpression.
    def visitPowerExpression(self, ctx:JavaScriptParser.PowerExpressionContext):
        self.printNewLine()
        self.addNode('PowerExpression')
        self.nest_level += 1

        self.printNewLine()
        self.addNode('Operator: **')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        self.printNewLine()
        self.addNode('PreIncrementExpression')
        self.nest_level += 1

        self.printNewLine()
        self.addNode('Operator: ++')
        self.visitChild(ctx.singleExpression())

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        self.printNewLine()
        self.addNode('ObjectLiteral')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#MetaExpression.
    def visitMetaExpression(self, ctx:JavaScriptParser.MetaExpressionContext):
        self.printNewLine()
        self.addNode('MetaExpression: not implemented')
        return None

    # Visit a parse tree produced by JavaScriptParser#InExpression.
    def visitInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        self.printNewLine()
        self.addNode('InExpression')
        self.nest_level += 1

        self.printNewLine()
        self.addNode('Operator: in')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:JavaScriptParser.LogicalOrExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('LogicalOrExpression')

        self.printNewLine()
        self.addNode('Operator: ||')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#NotExpression.
    def visitNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        self.printNewLine()
        self.addNode('NotExpression')

        self.nest_level += 1
        self.printNewLine()
        self.addNode('Operator: !')
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        self.printNewLine()
        self.addNode('PreDecreaseExpression')

        self.nest_level += 1
        self.printNewLine()
        self.addNode('Operator: --')
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AwaitExpression.
    def visitAwaitExpression(self, ctx:JavaScriptParser.AwaitExpressionContext):
        self.printNewLine()
        self.addNode('AwaitExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#ThisExpression.
    def visitThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        self.printNewLine()
        self.addNode('ThisExpression')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx:JavaScriptParser.FunctionExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaScriptParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:JavaScriptParser.UnaryMinusExpressionContext):
        self.printNewLine()
        self.addNode('UnaryMinusExpression')
        self.nest_level += 1
        self.printNewLine()
        self.addNode('Operator: -')
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        self.printNewLine()
        self.addNode('AssignmentExpression')
        self.nest_level += 1

        self.printNewLine()
        self.addNode('Operator: =')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        self.printNewLine()
        self.addNode('PostDecreaseExpression')
        self.nest_level += 1
        self.printNewLine()
        self.addNode('Operator: --')
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        self.printNewLine()
        self.addNode('InstanceOf: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        self.printNewLine()
        self.addNode('UnaryPlusExpression')
        self.nest_level += 1
        self.printNewLine()
        self.addNode('Operator: +')
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        self.printNewLine()
        self.addNode('DeleteExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#ImportExpression.
    def visitImportExpression(self, ctx:JavaScriptParser.ImportExpressionContext):
        self.printNewLine()
        self.addNode('ImportExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('EqualityExpression')

        self.printNewLine()
        self.addNode('Operator: ')

        if ctx.Equals_():
            self.addNode('==')
        elif ctx.IdentityEquals():
            self.addNode('===')
        elif ctx.NotEquals():
            self.addNode('!=')
        elif ctx.IdentityNotEquals():
            self.addNode('!==')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:JavaScriptParser.BitXOrExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('BitXorExpression')

        self.printNewLine()
        self.addNode('Operator: ^')
        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#SuperExpression.
    def visitSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        self.printNewLine()
        self.addNode('SuperExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('MultiplicativeExpression')

        self.printNewLine()
        self.addNode('Operator: ')

        if ctx.Divide():
            self.addNode('/')
        elif ctx.Multiply():
            self.addNode('*')
        elif ctx.Modulus():
            self.addNode('%')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:JavaScriptParser.BitShiftExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('BitShiftExpression')

        self.printNewLine()
        self.addNode('Operator: ')

        if ctx.LeftShiftArithmetic():
            self.addNode('<<')
        elif ctx.RightShiftArithmetic():
            self.addNode('>>')
        elif ctx.RightShiftLogical():
            self.addNode('>>>')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:JavaScriptParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:JavaScriptParser.AdditiveExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('AdditiveExpression')

        self.printNewLine()
        self.addNode('Operator: ')
        if ctx.Minus():
            self.addNode('-')
        elif ctx.Plus():
            self.addNode('+')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        self.printNewLine()
        self.addNode('RelationalExpression')
        self.nest_level += 1

        self.printNewLine()
        self.addNode('Operator: ')

        if ctx.GreaterThanEquals():
            self.addNode('>=')
        elif ctx.LessThan():
            self.addNode('<')
        elif ctx.LessThanEquals():
            self.addNode('<=')
        elif ctx.MoreThan():
            self.addNode('>')
        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        self.printNewLine()
        self.addNode('PostIncrementExpression')
        self.nest_level += 1
        self.printNewLine()
        self.addNode('Operator: ++')
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#YieldExpression.
    def visitYieldExpression(self, ctx:JavaScriptParser.YieldExpressionContext):
        self.printNewLine()
        self.addNode('YieldExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        self.printNewLine()
        self.addNode('BitNotExpression')
        self.nest_level += 1
        self.printNewLine()
        self.addNode('Operator: ~')
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#NewExpression.
    def visitNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):
        self.printNewLine()
        self.addNode('NewExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        self.printNewLine()
        self.addNode('LiteralExpression')
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        self.printNewLine()
        self.addNode('MemberDotExpression')

        self.nest_level += 1
        self.visitChild(ctx.singleExpression(), 'Object')
        self.visitChild(ctx.identifierName(), 'Property')
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ClassExpression.
    def visitClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        self.printNewLine()
        self.addNode('ClassExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        self.printNewLine()
        self.addNode('MemberIndexExpression')

        self.nest_level += 1
        self.visitChild(ctx.singleExpression(), 'Object')
        self.visitChild(ctx.expressionSequence(), 'Property')
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('BitAndExpression')

        self.printNewLine()
        self.addNode('Operator: &')
        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:JavaScriptParser.BitOrExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('BitOrExpression')

        self.printNewLine()
        self.addNode('Operator: |')
        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:JavaScriptParser.AssignmentOperatorExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode('AssignmentOperatorExpression')

        operator = ctx.assignmentOperator()
        self.visitChild(operator, 'AssignmentOperator')

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#VoidExpression.
    def visitVoidExpression(self, ctx:JavaScriptParser.VoidExpressionContext):
        self.printNewLine()
        self.addNode('VoidExpression: not implemented')
        return None


    # Visit a parse tree produced by JavaScriptParser#CoalesceExpression.
    def visitCoalesceExpression(self, ctx:JavaScriptParser.CoalesceExpressionContext):
        self.printNewLine()
        self.addNode('CoalesceExpression: not implemented')
        return None

    # Visit a parse tree produced by JavaScriptParser#assignable.
    def visitAssignable(self, ctx:JavaScriptParser.AssignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx:JavaScriptParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#FunctionDecl.
    def visitFunctionDecl(self, ctx:JavaScriptParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AnoymousFunctionDecl.
    def visitAnoymousFunctionDecl(self, ctx:JavaScriptParser.AnoymousFunctionDeclContext):
        self.printNewLine()
        self.addNode('AnoymousFunctionDecl')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#ArrowFunction.
    def visitArrowFunction(self, ctx:JavaScriptParser.ArrowFunctionContext):
        self.printNewLine()
        self.addNode('ArrowFunction')
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#arrowFunctionParameters.
    def visitArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrowFunctionBody.
    def visitArrowFunctionBody(self, ctx:JavaScriptParser.ArrowFunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:JavaScriptParser.AssignmentOperatorContext):
        self.printNewLine()
        self.nest_level += 1
        string = None
        if ctx.BitAndAssign():
            string = f'BitAndAssign: {ctx.BitAndAssign()}'
        if ctx.BitOrAssign():
            string = f'BitOrAssign: {ctx.BitOrAssign()}'
        if ctx.BitXorAssign():
            string = f'BitXorAssign: {ctx.BitXorAssign()}'
        if ctx.MultiplyAssign():
            string = f'MultiplyAssign: {ctx.MultiplyAssign()}'
        if ctx.DivideAssign():
            string = f'DivideAssign: {ctx.DivideAssign()}'
        if ctx.ModulusAssign():
            string = f'ModulusAssign: {ctx.ModulusAssign()}'
        if ctx.PlusAssign():
            string = f'PlusAssign: {ctx.PlusAssign()}'
        if ctx.MinusAssign():
            string = f'MinusAssign: {ctx.MinusAssign()}'
        if ctx.LeftShiftArithmeticAssign():
            string = f'LeftShiftArithmeticAssign: {ctx.LeftShiftArithmeticAssign()}'
        if ctx.RightShiftArithmeticAssign():
            string = f'RightShiftArithmeticAssign: {ctx.RightShiftArithmeticAssign()}'

        if ctx.RightShiftLogicalAssign():
            string = f'RightShiftLogicalAssign: {ctx.RightShiftLogicalAssign()}'
        if ctx.PowerAssign():
            string = f'PowerAssign: {ctx.PowerAssign()}'

        self.addNode(string)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#literal.
    def visitLiteral(self, ctx:JavaScriptParser.LiteralContext):
        if ctx.numericLiteral():
            return self.visitChildren(ctx)

        self.printNewLine()
        self.nest_level += 1

        string = ctx.getChild(0).getText()
        self.addNode(string)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        self.printNewLine()
        self.addNode(ctx.getChild(0).getText())
        return None


    # Visit a parse tree produced by JavaScriptParser#bigintLiteral.
    def visitBigintLiteral(self, ctx:JavaScriptParser.BigintLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaScriptParser#getter.
    def visitGetter(self, ctx:JavaScriptParser.GetterContext):
        self.printNewLine()
        self.addNode('Getter')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#setter.
    def visitSetter(self, ctx:JavaScriptParser.SetterContext):
        self.printNewLine()
        self.addNode('Setter')
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#identifierName.
    def visitIdentifierName(self, ctx:JavaScriptParser.IdentifierNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#identifier.
    def visitIdentifier(self, ctx:JavaScriptParser.IdentifierContext):
        self.printNewLine()
        self.nest_level += 1
        self.addNode(f'Identifier: {ctx.Identifier()}')
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#reservedWord.
    def visitReservedWord(self, ctx:JavaScriptParser.ReservedWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#keyword.
    def visitKeyword(self, ctx:JavaScriptParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#let.
    def visitLet(self, ctx:JavaScriptParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#eos.
    def visitEos(self, ctx:JavaScriptParser.EosContext):
        return self.visitChildren(ctx)
