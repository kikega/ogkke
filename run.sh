#!/bin/bash
echo "Arrancando PostgreSQL..."
systemctl start postgresql
echo "Activando virtualenv Karate..."
workon karate
echo "Arrancando saervidor de desarrollo..."

