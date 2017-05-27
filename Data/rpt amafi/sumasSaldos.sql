EXEC sumasSaldos 4, '02/01/2012', '02/02/2012', '01/01/2012', 1, 1

ALTER PROCEDURE sumasSaldos(@Inivel integer, @IFechaIni SMALLDATETIME, @IFechaFin SMALLDATETIME, @IfechaAper SMALLDATETIME, @IMoneda INTEGER, @IGestion INTEGER)
	AS
BEGIN

	-- Creamos Una Tabla
	CREATE TABLE #SQL(
		cnNombre		VARCHAR(50),
		cnLugar			VARCHAR(50),
		cnNit			VARCHAR(25),
		cnTelefono		VARCHAR(25),
		cnTeleFax		VARCHAR(25),
		cnDireccion		VARCHAR(50),
		cnSimboloMon		VARCHAR(10),
		cnDescripcionMon	VARCHAR(25),
		debe			DECIMAL(10,2),
		haber			DECIMAL(10,2),
		debeS			DECIMAL(10,2),
		haberS			DECIMAL(10,2),
		cnCuentaContable	VARCHAR(20),
		cnDescripcionC		VARCHAR(50),
		IFechaIni 		SMALLDATETIME, 
		IFechaFin 		SMALLDATETIME
	)

	-- Declaracion de variables
	DECLARE 
		@cnNombre		VARCHAR(50),
		@cnLugar		VARCHAR(50),
		@cnNit			VARCHAR(25),
		@cnTelefono		VARCHAR(25),
		@cnTeleFax		VARCHAR(25),
		@cnDireccion		VARCHAR(50),
		@cnSimboloMon		VARCHAR(10),
		@cnDescripcionMon	VARCHAR(25),
		@debe			DECIMAL(10,2),
		@haber			DECIMAL(10,2),
		@debeS			DECIMAL(10,2),
		@haberS			DECIMAL(10,2),
		@cnCuentaContable	VARCHAR(20),
		@cnDescripcionC		VARCHAR(50);
							
	-- sacamos los primero parametros
	SELECT 	
		@cnNombre 	= w.cnNombre,
		@cnLugar  	= w.cnLugar,
		@cnNit	  	= w.cnNit,
		@cnTelefono 	= w.cnTelefono,
		@cnTeleFax  	= w.cnTeleFax,
		@cnDireccion	= w.cnDireccion,
		@cnSimboloMon 	  = CASE  WHEN @IMoneda = 1 THEN n.cnSimbolo WHEN @IMoneda = 2 THEN e.cnSimbolo END,
		@cnDescripcionMon = CASE  WHEN @IMoneda = 1 THEN n.cnDescripcion WHEN @IMoneda = 2 THEN e.cnDescripcion END
	FROM cnConfEmpresa w,
		cnParamContable s 
		INNER JOIN cnMoneda 	n	ON n.pk_Moneda	= s.fkMonNac
		INNER JOIN cnMoneda 	e	ON e.pk_Moneda 	= s.fkMonExt
	WHERE 	(s.pk_ParamContable = @IGestion)

		IF(@Inivel = 1)
		BEGIN
			DECLARE mayor CURSOR FOR
			SELECT
				n.cnNivel1 as codeA, n.cnDescripcion as descA
			FROM 	
				cnComprobante c
				INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
				INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
				INNER JOIN cnPlanContable n 	ON p.cnNivel1 		= n.cnNivel1 	AND n.cnNivel = 1
			WHERE 	(c.cnEstado = 'T' )
				AND (c.cnFechaComp BETWEEN @IfechaAper AND @IFechaFin)
			GROUP BY n.cnNivel1, n.cnDescripcion
		END
		ELSE
		BEGIN
			IF(@Inivel = 2)
			BEGIN
				DECLARE mayor CURSOR FOR
				SELECT
					n.cnNivel2 as codeA, n.cnDescripcion as descA
				FROM 	
					cnComprobante c
					INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
					INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
					INNER JOIN cnPlanContable n 	ON p.cnNivel2 		= n.cnNivel2 	AND n.cnNivel = 2
				WHERE 	(c.cnEstado = 'T' )					
					AND (c.cnFechaComp BETWEEN @IfechaAper AND @IFechaFin)
				GROUP BY n.cnNivel2, n.cnDescripcion
			END
			ELSE
			BEGIN
				IF(@Inivel = 3)
				BEGIN
					DECLARE mayor CURSOR FOR
					SELECT
						n.cnNivel3 as codeA, n.cnDescripcion as descA
					FROM 	
						-- comprobantes contables de 01/01/2012 ---> 01/31/2012
						cnComprobante c
						INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
						INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
						INNER JOIN cnPlanContable n 	ON p.cnNivel3 		= n.cnNivel3 	AND n.cnNivel = 3
					WHERE 	(c.cnEstado = 'T')						
						AND (c.cnFechaComp BETWEEN @IfechaAper AND @IFechaFin)
					GROUP BY n.cnNivel3, n.cnDescripcion
				END
				ELSE
				BEGIN
					IF(@Inivel = 4)
					BEGIN
						DECLARE mayor CURSOR FOR
						SELECT
							n.cnNivel4 as codeA, n.cnDescripcion as descA
						FROM 	
							-- comprobantes contables de 01/01/2012 ---> 01/31/2012
							cnComprobante c
							INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
							INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
							INNER JOIN cnPlanContable n 	ON p.cnNivel4 		= n.cnNivel4 	AND n.cnNivel = 4
						WHERE 	(c.cnEstado = 'T' )
							AND (c.cnFechaComp BETWEEN @IfechaAper AND @IFechaFin)
						GROUP BY n.cnNivel4, n.cnDescripcion
					END
					ELSE
					BEGIN
						IF(@Inivel = 5)-- A NIVEL DE CUENTA
						BEGIN
							DECLARE mayor CURSOR FOR
							SELECT
								p.cnCuentaContable as codeA, p.cnDescripcion as descA
							FROM 	
								cnComprobante c
								INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
								INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable								
							WHERE 	(c.cnEstado = 'T' )								
								AND (c.cnFechaComp BETWEEN @IfechaAper AND @IFechaFin)
							GROUP BY p.cnCuentaContable, p.cnDescripcion
						END
					END
				END
			END
		END
		
	OPEN mayor;
	FETCH NEXT FROM mayor
	INTO
		@cnCuentaContable, @cnDescripcionC
	WHILE @@FETCH_STATUS = 0
	BEGIN 
		SET @debeS  = 0;
		SET @haberS = 0;
		
		IF(@Inivel = 1) -- nivel 1
		BEGIN
			IF(@IfechaAper < (@IFechaIni-1))
			BEGIN
				-- saldo inicial
				SELECT
					@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
					@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
				FROM 	
					cnComprobante c
					INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
					INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
				WHERE 	(c.cnEstado = 'T' )
					AND (c.cnFechaComp BETWEEN @IfechaAper AND (@IFechaIni-1))
					AND (p.cnNivel1 = @cnCuentaContable)			
				-- saldo mensual 
				SELECT
					@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
					@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
				FROM 	
					cnComprobante c
					INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
					INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
				WHERE 	(c.cnEstado = 'T' )					
					AND (c.cnFechaComp BETWEEN @IFechaIni AND (@IFechaFin))
					AND (p.cnNivel1 = @cnCuentaContable)					
			END 
			ELSE 
			BEGIN
				-- balance inicial 
				SELECT
					@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
					@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
				FROM 	
					cnComprobante c
					INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
					INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
				WHERE 	(c.cnEstado = 'T' )
					AND (c.cnTcomp = 0)
					AND (c.fkGestion = @IGestion)
					AND (p.cnNivel1 = @cnCuentaContable)
				-- saldo mensual 
				SELECT
					@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
					@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
				FROM 	
					cnComprobante c
					INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
					INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
				WHERE 	(c.cnEstado = 'T' )
					AND (c.cnTcomp > 0)
					AND (c.cnFechaComp BETWEEN @IFechaIni AND (@IFechaFin))
					AND (p.cnNivel1 = @cnCuentaContable)					
			END 
		END
		ELSE
		BEGIN
			IF(@Inivel = 2)
			BEGIN
				IF(@IfechaAper < (@IFechaIni-1))
				BEGIN 
					-- saldo inicial
					SELECT
						@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
						@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
					FROM 	
						cnComprobante c
						INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
						INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
					WHERE 	(c.cnEstado = 'T' )
						AND (c.cnFechaComp BETWEEN @IfechaAper AND (@IFechaIni-1))
						AND (p.cnNivel2 = @cnCuentaContable)
					-- saldo mensual 
					SELECT
						@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
						@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
					FROM 	
						cnComprobante c
						INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
						INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
					WHERE 	(c.cnEstado = 'T' )						
						AND (c.cnFechaComp BETWEEN @IFechaIni AND @IFechaFin)
						AND (p.cnNivel2 = @cnCuentaContable)
				END 
				ELSE
				BEGIN 
					-- balance inicial
					SELECT
						@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
						@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
					FROM 	
						cnComprobante c
						INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
						INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
					WHERE 	(c.cnEstado = 'T' )
						AND (c.cnTcomp = 0)
						AND (c.fkGestion = @IGestion)
						AND (p.cnNivel2 = @cnCuentaContable)
					-- saldo mensual 
					SELECT
						@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
						@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
					FROM 	
						cnComprobante c
						INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
						INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
					WHERE 	(c.cnEstado = 'T' )
						AND (c.cnTcomp > 0)
						AND (c.cnFechaComp BETWEEN @IFechaIni AND @IFechaFin)
						AND (p.cnNivel2 = @cnCuentaContable)
				END 
			END
			ELSE
			BEGIN
				IF(@Inivel = 3)
				BEGIN
					IF(@IfechaAper < (@IFechaIni-1))
					BEGIN
						-- saldo inicial 
						SELECT
							@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
							@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
						FROM 	
							cnComprobante c
							INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
							INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
						WHERE 	(c.cnEstado = 'T' )
							AND (c.cnFechaComp BETWEEN @IfechaAper AND (@IFechaIni-1))
							AND (p.cnNivel3 = @cnCuentaContable)
						-- saldo mensual 
						SELECT
							@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
							@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
						FROM 	
							cnComprobante c
							INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
							INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
						WHERE 	(c.cnEstado = 'T')
							AND (c.cnFechaComp BETWEEN @IFechaIni AND @IFechaFin)
							AND (p.cnNivel3 = @cnCuentaContable)
					END 
					ELSE
					BEGIN 
						-- Balance inicial
						SELECT
							@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
							@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
						FROM 	
							cnComprobante c
							INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
							INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
						WHERE 	(c.cnEstado = 'T' )
							AND (c.cnTcomp = 0)
							AND (c.fkGestion = @IGestion)
							AND (p.cnNivel3 = @cnCuentaContable)
						-- saldo mensual 
						SELECT
							@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
							@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
						FROM 	
							cnComprobante c
							INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
							INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
						WHERE 	(c.cnEstado = 'T' )
							AND (c.cnTcomp > 0)
							AND (c.cnFechaComp BETWEEN @IFechaIni AND @IFechaFin)
							AND (p.cnNivel3 = @cnCuentaContable)
					END 
				END
				ELSE
				BEGIN
					IF(@Inivel = 4)
					BEGIN
						IF(@IfechaAper < (@IFechaIni-1))
						BEGIN 
							-- saldo inicial							
							SELECT
								@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
								@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
							FROM 	
								cnComprobante c
								INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
								INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
							WHERE 	(c.cnEstado = 'T' )
								AND (c.cnFechaComp BETWEEN @IfechaAper AND (@IFechaIni-1))
								AND (p.cnNivel4 = @cnCuentaContable)
							print 'saldo inicial 4' 
							print '@cnCuentaContable : ' + @cnCuentaContable
							-- saldo mensual
							SELECT
								@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
								@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
							FROM 	
								cnComprobante c
								INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
								INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
							WHERE 	(c.cnEstado = 'T' )								
								AND (c.cnFechaComp BETWEEN @IFechaIni AND @IFechaFin)
								AND (p.cnNivel4 = @cnCuentaContable)
						END 
						ELSE
						BEGIN 
							-- balance inicial
							SELECT
								@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
								@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
							FROM 	
								cnComprobante c
								INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
								INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
							WHERE 	(c.cnEstado = 'T' )
								AND (c.cnTcomp = 0)
								AND (c.fkGestion = @IGestion)
								AND (p.cnNivel4 = @cnCuentaContable)
							print 'balance inicial 4' 
							-- saldo mensual
							SELECT
								@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
								@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
							FROM 	
								cnComprobante c
								INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
								INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
							WHERE 	(c.cnEstado = 'T' )
								AND (c.cnTcomp > 0)
								AND (c.cnFechaComp BETWEEN @IFechaIni AND @IFechaFin)
								AND (p.cnNivel4 = @cnCuentaContable)
						END 
					END
					ELSE
					BEGIN
						IF(@Inivel = 5)
						BEGIN
							print 'nivel 5' 
							IF(@IfechaAper < (@IFechaIni-1))
							BEGIN 
								-- Saldo inicial
								print 'saldo anterior' 
								SELECT
									@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
									@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
								FROM 	
									cnComprobante c
									INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
									INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
								WHERE 	(c.cnEstado = 'T' )
									AND (c.cnFechaComp BETWEEN @IfechaAper AND (@IFechaIni-1))
									AND (p.cnCuentaContable = @cnCuentaContable)

								-- saldo mensual
								SELECT
									@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
									@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
								FROM 	
									cnComprobante c
									INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
									INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
								WHERE 	(c.cnEstado = 'T')									
									AND (c.cnFechaComp BETWEEN @IfechaIni AND @IFechaFin)
									AND (p.cnCuentaContable = @cnCuentaContable)
								if(@cnCuentaContable = '5-8-01-01-001')
								BEGIN
									print 'Diferencia  Normal'
									print '@debeS : ' + convert(char(10), @debeS)
									print '@haberS : ' + convert(char(10), @haberS)
									print '@debe : ' + convert(char(10), @debe)
									print '@haber : ' + convert(char(10), @haber)
								END 
							END 
							ELSE
							BEGIN
								-- balance inicial
								print 'balance inicial'
								SELECT
									@debeS  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
									@haberS = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
								FROM 	
									cnComprobante c
									INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
									INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
								WHERE 	(c.cnEstado = 'T' )
									AND (c.cnTcomp = 0)
									AND (c.fkGestion = @IGestion)
									AND (p.cnCuentaContable = @cnCuentaContable)
												
								-- saldo mensual
								SELECT
									@debe  = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnDebeN WHEN @IMoneda = 2 THEN dc.cnDebeE END),0),
									@haber = ISNULL(SUM(CASE  WHEN @IMoneda = 1 THEN dc.cnHaberN WHEN @IMoneda = 2 THEN dc.cnHaberE END),0)
								FROM 	
									cnComprobante c
									INNER JOIN cnDetComprobante dc 	ON c.pk_Comprobante 	= dc.fkComprobante
									INNER JOIN cnPlanContable p 	ON p.pk_PlanContable 	= dc.fkCuentaContable
								WHERE 	(c.cnEstado = 'T')
									AND (c.cnTcomp > 0)
									AND (c.cnFechaComp BETWEEN @IfechaIni AND @IFechaFin)
									AND (p.cnCuentaContable = @cnCuentaContable)
								if(@cnCuentaContable = '5-8-01-01-001')
								BEGIN
									print 'Diferencia  balance inicial'
									print '@debeS : ' + convert(char(10), @debeS)
									print '@haberS : ' + convert(char(10), @haberS)
									print '@debe : ' + convert(char(10), @debe)
									print '@haber : ' + convert(char(10), @haber)
								END 
							END
						END
					END
				END
			END
		END
		-- insertamos en la tabla temporal
		INSERT INTO #SQL VALUES(@cnNombre, @cnLugar, @cnNit, @cnTelefono, @cnTeleFax, @cnDireccion, @cnSimboloMon, @cnDescripcionMon, @debe, @haber, @debeS, @haberS, @cnCuentaContable, @cnDescripcionC, @IFechaIni, @IFechaFin)
		
	FETCH NEXT FROM mayor
        INTO
		@cnCuentaContable, @cnDescripcionC
	END
	CLOSE mayor;
	DEALLOCATE mayor;	


	SELECT 
		cnNombre, cnLugar, cnNit, cnTelefono, cnTeleFax, cnDireccion, 
		cnSimboloMon, cnDescripcionMon, debe, haber, debeS, 
		haberS, cnCuentaContable, cnDescripcionC,
		IFechaIni, IFechaFin 
	FROM #SQL
	ORDER BY cnCuentaContable ASC
END


/*


SELECT * FROM cnDetcomprobante
select * from cnComprobante
SELECT * FROM cnPlanContable
SELECT * FROM cnParamContable
SELECT * FROM cnConfEmpresa
SELECT * FROM cnMoneda


SELECT * FROM cnmoneda m, cnmoneda e

*/