(define (problem trasladoPacientes)
	(:domain pacientes)
	(:objects 
	p1 p2 - paciente 
	l1 l2 l3 l4 - localizacion 
	a - ambulancia 
	h - hospital)
	
	(:init 
	(hospital-en l1) 
	(paciente-en-l l3 p1) 
	(paciente-en-l l4 p2) 
	(ambulancia-en-l l1 a) 
	(vacia-ambulancia)
	(ir l1 l2) 
	(ir l2 l4)
	(ir l4 l3)
		   
	
	)
	(:goal (and 
	(paciente-en-l l1 p1) 
	(paciente-en-l l1 p2))
	)
)
