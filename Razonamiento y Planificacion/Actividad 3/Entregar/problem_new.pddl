(define (problem trasladoPacientes)
	(:domain pacientes)
	(:objects 
	p1 p2 - paciente 
	l1 l2 l3 l4 l5 l6 l7 - localizacion 
	a - ambulancia 
	h - hospital)
	
	(:init 
	(hospital-en l1) 
	(paciente-en-l l5 p1) 
	(paciente-en-l l6 p2) 
	(ambulancia-en-l l1 a) 
	(vacia-ambulancia)
	(ir l1 l2)
	(ir l2 l3)
	(ir l3 l4)
	(ir l4 l5)
	(ir l4 l6)
	(ir l5 l6)
		   
	
	)
	(:goal (and 
	(paciente-en-l l1 p1) 
	(paciente-en-l l1 p2))
	)
)
