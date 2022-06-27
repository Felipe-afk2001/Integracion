# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from core.models import medicamento



class medicamentoTestCase(TestCase):


    def test_create_med(self):

        client = APIClient()
        
        test_creamed = {
            'nom_drug':'ibuprofeno',
            'descripcion':'ayuda al dolor',
            'max_cant':'20',
            'laboratorio':'laboratorio de chile',
        }

        response = client.post(
            '/medicamento/', 
            test_creamed,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('pk', result)
        self.assertIn('nom_drug', result)
        self.assertIn('descripcion', result)
        self.assertIn('max_cant', result)
        self.assertIn('laboratorio', result)

        if 'pk' in result:
            del result['pk']

        self.assertEqual(result, test_creamed)


    def test_update_med(self):

        client = APIClient()

        # Creamos un objeto en la base de datos para trabajar con datos
        med = medicamento.objects.create(
            nom_drug='ketoprofeno',
            descripcion='ayuda a el dolor muscular',
            max_cant='15',
            laboratorio='laboratorio de chile',
            user=self.user
        )

        test_med_update = {
            'nom_drug':'ibuprofeno',
            'descripcion':'ayuda al dolor',
            'max_cant':'20',
            'laboratorio':'laboratorio de chile',
        }

        response = client.put(
            f'/medicamento/{med.pk}/', 
            test_med_update,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if 'pk' in result:
            del result['pk']

        self.assertEqual(result, test_med_update)

    
    def test_delete_med(self):

        client = APIClient()

        # Creamos un objeto en la base de datos para trabajar con datos
        med = medicamento.objects.create(
            nom_drug='ketoprofeno',
            descripcion='ayuda a el dolor muscular',
            max_cant='15',
            laboratorio='laboratorio de chile',
            user=self.user
        )

        response = client.delete(
            f'/medicamento/{med.pk}/', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        edu_exists = medicamento.objects.filter(pk=med.pk)
        self.assertFalse(edu_exists)


    def test_get_med(self):

        client = APIClient()

        medicamento.objects.create(
            nom_drug='ketoprofeno',
            descripcion='ayuda a el dolor muscular',
            max_cant='15',
            laboratorio='laboratorio de chile',
            user=self.user
        )

        medicamento.objects.create(
            nom_drug='ibuprofeno',
            descripcion='ayuda a el dolor',
            max_cant='13',
            laboratorio='laboratorio de chile',
            user=self.user
        )

        response = client.get('/medicamento/')
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result['count'], 2)

        for edu in result['results']:
            self.assertIn('pk', edu)
            self.assertIn('nom_drug', result)
            self.assertIn('descripcion', result)
            self.assertIn('max_cant', result)
            self.assertIn('laboratorio', result)
            
            break