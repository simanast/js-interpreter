from src.JavaScriptParserVisitor import JavaScriptParserVisitor
if __name__ is not None and "." in __name__:
    from src.JavaScriptParser import JavaScriptParser
else:
    from JavaScriptParser import JavaScriptParser



class AstVisitor(JavaScriptParserVisitor):

    def __init__(self):
        self.nest_level = 0
        self.tree = ""

    def printNewLine(self):
        string = '\n' + '-' * int(self.nest_level) * 4
        self.tree += string

    def visitChild(self, child, child_name=None):
        if child_name is None:
            child.accept(self)
            return

        self.printNewLine()
        self.tree += child_name
        self.nest_level += 1
        child.accept(self)
        self.nest_level -= 1


    # Visit a parse tree produced by JavaScriptParser#program.
    def visitProgram(self, ctx:JavaScriptParser.ProgramContext):
        self.tree += 'Program'
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
        self.tree += 'Block'
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
        self.tree += 'VariableDeclarationList'
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        self.printNewLine()
        self.nest_level += 1
        self.tree += 'VariableDeclaration'
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx:JavaScriptParser.EmptyStatementContext):
        self.printNewLine()
        self.tree += 'EmptyStatement'
        return None

    # Visit a parse tree produced by JavaScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ifStatement.
    def visitIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        self.printNewLine()
        self.tree += 'IfStatement'
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
        self.tree += 'DoStatement'
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
        self.tree += 'WhileStatement'
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
        self.tree += 'ForStatement'
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
        self.tree += 'ForInStatement:'
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
        self.tree += 'ForOfStatement'
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
        self.tree += 'VarModifier: '
        var_modifier = None
        if ctx.Var():
            var_modifier = 'var'
        elif ctx.Const():
            var_modifier = 'const'
        elif ctx.let():
            var_modifier = 'let'
        self.tree += var_modifier
        return None


    # Visit a parse tree produced by JavaScriptParser#continueStatement.
    def visitContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        self.printNewLine()
        self.tree += 'ContinueStatement'
        if ctx.identifier():
            self.nest_level += 1
            ctx.identifier().accept(self)
            self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        self.printNewLine()
        self.tree += 'BreakStatement'
        if ctx.identifier():
            self.nest_level += 1
            ctx.identifier().accept(self)
            self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        self.printNewLine()
        self.tree += 'ReturnStatement'
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
        self.tree += 'FunctionDeclaration'
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result



    # Visit a parse tree produced by JavaScriptParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classTail.
    def visitClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classElement.
    def visitClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#methodDefinition.
    def visitMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        self.printNewLine()
        self.tree += 'ParameterList'
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#formalParameterArg.
    def visitFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        self.printNewLine()
        self.tree += 'FormalParameterArg'
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1

    # Visit a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def visitLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        return None

    # Visit a parse tree produced by JavaScriptParser#functionBody.
    def visitFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        self.printNewLine()
        self.tree += 'FunctionBody'
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
        self.tree += 'ArrayLiteral'
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
        self.tree += 'PropertyAssignment'
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def visitComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#FunctionProperty.
    def visitFunctionProperty(self, ctx:JavaScriptParser.FunctionPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        self.printNewLine()
        self.tree += 'PropertyGetter'
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        self.printNewLine()
        self.tree += 'PropertySetter'
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#PropertyShorthand.
    def visitPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#propertyName.
    def visitPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        self.printNewLine()
        self.tree += 'PropertyName'
        self.nest_level += 1

        if ctx.singleExpression() or ctx.identifierName():
            self.visitChildren(ctx)
        else:
            self.printNewLine()
            if ctx.StringLiteral():
                self.tree += ctx.StringLiteral().getText()
            elif ctx.numericLiteral():
                self.tree += ctx.numericLiteral().getText()

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#arguments.
    def visitArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        self.printNewLine()
        self.tree += 'Arguments'
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        self.printNewLine()
        self.tree += 'TernaryExpression'
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
        self.tree += 'LogicalAndExpression'
        self.nest_level += 1

        self.printNewLine()
        self.tree += 'Operator: &&'

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#PowerExpression.
    def visitPowerExpression(self, ctx:JavaScriptParser.PowerExpressionContext):
        self.printNewLine()
        self.tree += 'PowerExpression'
        self.nest_level += 1

        self.printNewLine()
        self.tree += 'Operator: **'

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        self.printNewLine()
        self.tree += 'PreIncrementExpression'
        self.nest_level += 1

        self.printNewLine()
        self.tree += 'Operator: ++'
        self.visitChild(ctx.singleExpression())

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        self.printNewLine()
        self.tree += 'ObjectLiteral'
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#MetaExpression.
    def visitMetaExpression(self, ctx:JavaScriptParser.MetaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#InExpression.
    def visitInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        self.printNewLine()
        self.tree += 'InExpression'
        self.nest_level += 1

        self.printNewLine()
        self.tree += 'Operator: in'

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
        self.tree += 'LogicalOrExpression'

        self.printNewLine()
        self.tree += 'Operator: ||'

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#NotExpression.
    def visitNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        self.printNewLine()
        self.tree += 'NotExpression'

        self.nest_level += 1
        self.printNewLine()
        self.tree += 'Operator: !'
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        self.printNewLine()
        self.tree += 'PreDecreaseExpression'

        self.nest_level += 1
        self.printNewLine()
        self.tree += 'Operator: --'
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AwaitExpression.
    def visitAwaitExpression(self, ctx:JavaScriptParser.AwaitExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ThisExpression.
    def visitThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        self.printNewLine()
        self.tree += 'ThisExpression'
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
        self.tree += 'UnaryMinusExpression'
        self.nest_level += 1
        self.printNewLine()
        self.tree += 'Operator: -'
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        self.printNewLine()
        self.tree += 'AssignmentExpression'
        self.nest_level += 1

        self.printNewLine()
        self.tree += 'Operator: ='

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None



    # Visit a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        self.printNewLine()
        self.tree += 'PostDecreaseExpression'
        self.nest_level += 1
        self.printNewLine()
        self.tree += 'Operator: --'
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        self.printNewLine()
        self.tree += 'UnaryPlusExpression'
        self.nest_level += 1
        self.printNewLine()
        self.tree += 'Operator: +'
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ImportExpression.
    def visitImportExpression(self, ctx:JavaScriptParser.ImportExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.tree += 'EqualityExpression'

        self.printNewLine()
        self.tree += 'Operator: '

        if ctx.Equals_():
            self.tree += '=='
        elif ctx.IdentityEquals():
            self.tree += '==='
        elif ctx.NotEquals():
            self.tree += '!='
        elif ctx.IdentityNotEquals():
            self.tree += '!=='

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
        self.tree += 'BitXorExpression'

        self.printNewLine()
        self.tree += 'Operator: ^'
        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#SuperExpression.
    def visitSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.tree += 'MultiplicativeExpression'

        self.printNewLine()
        self.tree += 'Operator: '

        if ctx.Divide():
            self.tree += '/'
        elif ctx.Multiply():
            self.tree += '*'
        elif ctx.Modulus():
            self.tree += '%'

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
        self.tree += 'BitShiftExpression'

        self.printNewLine()
        self.tree += 'Operator: '

        if ctx.LeftShiftArithmetic():
            self.tree += '<<'
        elif ctx.RightShiftArithmetic():
            self.tree += '>>'
        elif ctx.RightShiftLogical():
            self.tree += '>>>'

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
        self.tree += 'AdditiveExpression'

        self.printNewLine()
        self.tree += 'Operator: '
        if ctx.Minus():
            self.tree += '-'
        elif ctx.Plus():
            self.tree += '+'

        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        self.printNewLine()
        self.tree += 'RelationalExpression'
        self.nest_level += 1

        self.printNewLine()
        self.tree += 'Operator: '

        if ctx.GreaterThanEquals():
            self.tree += '>='
        elif ctx.LessThan():
            self.tree += '<'
        elif ctx.LessThanEquals():
            self.tree += '<='
        elif ctx.MoreThan():
            self.tree += '>'
        lhs = ctx.singleExpression(0)
        self.visitChild(lhs, 'Lhs')

        rhs = ctx.singleExpression(1)
        self.visitChild(rhs, 'Rhs')

        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        self.printNewLine()
        self.tree += 'PostIncrementExpression'
        self.nest_level += 1
        self.printNewLine()
        self.tree += 'Operator: ++'
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#YieldExpression.
    def visitYieldExpression(self, ctx:JavaScriptParser.YieldExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        self.printNewLine()
        self.tree += 'BitNotExpression'
        self.nest_level += 1
        self.printNewLine()
        self.tree += 'Operator: ~'
        self.visitChild(ctx.singleExpression())
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#NewExpression.
    def visitNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):

        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        self.printNewLine()
        self.tree += 'LiteralExpression'
        self.nest_level += 1
        result = self.visitChildren(ctx)
        self.nest_level -= 1
        return result


    # Visit a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ClassExpression.
    def visitClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        self.printNewLine()
        self.nest_level += 1
        self.tree += 'BitAndExpression'

        self.printNewLine()
        self.tree += 'Operator: &'
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
        self.tree += 'BitOrExpression'

        self.printNewLine()
        self.tree += 'Operator: |'
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
        self.tree += 'AssignmentOperatorExpression'

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#CoalesceExpression.
    def visitCoalesceExpression(self, ctx:JavaScriptParser.CoalesceExpressionContext):
        return self.visitChildren(ctx)


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
        self.tree += 'AnoymousFunctionDecl'
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None

    # Visit a parse tree produced by JavaScriptParser#ArrowFunction.
    def visitArrowFunction(self, ctx:JavaScriptParser.ArrowFunctionContext):
        self.printNewLine()
        self.tree += 'ArrowFunction'
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

        self.tree += string
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#literal.
    def visitLiteral(self, ctx:JavaScriptParser.LiteralContext):
        if ctx.numericLiteral():
            return self.visitChildren(ctx)

        self.printNewLine()
        self.nest_level += 1

        string = ctx.getChild(0).getText()
        self.tree += string
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        self.printNewLine()
        self.tree += ctx.getChild(0).getText()
        return None


    # Visit a parse tree produced by JavaScriptParser#bigintLiteral.
    def visitBigintLiteral(self, ctx:JavaScriptParser.BigintLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#getter.
    def visitGetter(self, ctx:JavaScriptParser.GetterContext):
        self.printNewLine()
        self.tree += 'Getter'
        self.nest_level += 1
        self.visitChildren(ctx)
        self.nest_level -= 1
        return None


    # Visit a parse tree produced by JavaScriptParser#setter.
    def visitSetter(self, ctx:JavaScriptParser.SetterContext):
        self.printNewLine()
        self.tree += 'Setter'
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
        self.tree += f'Identifier: {ctx.Identifier()}'
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
