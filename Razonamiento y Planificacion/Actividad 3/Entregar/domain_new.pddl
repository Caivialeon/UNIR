(define (domain pacientes)
	(:requirements :typing)
	(:types paciente ambulancia localizacion hospital)
	(:predicates
		(paciente-en-l ?l - localizacion ?p - paciente )
		(ambulancia-en-l ?l - localizacion ?a - ambulancia)
		(hospital-en ?l - localizacion)
		(llena-ambulancia ?p - paciente)
		(vacia-ambulancia)
		(ir ?l1 - localizacion ?l2 - localizacion)      
	)
	;///////////////////////////
	(:action mover
		:parameters (?a - ambulancia ?l1 - localizacion ?l2 - localizacion)
		:precondition 
			( and( ambulancia-en-l ?l1 ?a) (ir ?l1  ?l2 ))
		:effect 
			( and( not( ambulancia-en-l ?l1 ?a)) (ambulancia-en-l ?l2 ?a) (ir ?l2 ?l1))
	)
	;/////////////////////////////////////
	(:action subir
		:parameters (?p - paciente ?l1 - localizacion ?a - ambulancia)
		:precondition 
			(and (vacia-ambulancia) (ambulancia-en-l ?l1 ?a) (paciente-en-l ?l1 ?p) )
		:effect
			(and (not(vacia-ambulancia)) (llena-ambulancia ?p))
	)
	;////////////////////////
	(:action bajar
		:parameters (?p - paciente ?l1 - localizacion ?a - ambulancia)
		:precondition
			(and (llena-ambulancia ?p) (ambulancia-en-l ?l1 ?a))
		:effect
			(and (not(llena-ambulancia ?p)) (vacia-ambulancia) 
			(ambulancia-en-l ?l1 ?a) (paciente-en-l ?l1 ?p) )
	)
	;//////////////////////////
	
)