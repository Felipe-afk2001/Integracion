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
        self.assertIn('id_stock', result)
        self.assertIn('nom_drug', result)
        self.assertIn('descripcion', result)
        self.assertIn('max_cant', result)
        self.assertIn('laboratorio', result)

        # if 'id_stock' in result:
        #     del result['id_stock']

        # self.assertEqual(result, test_creamed)


    def test_update_med(self):

        client = APIClient()

        # Creamos un objeto en la base de datos para trabajar con datos
        med = medicamento.objects.create(
            nom_drug='ketoprofeno',
            descripcion='ayuda a el dolor muscular',
            max_cant='15',
            laboratorio='laboratorio de chile',
        )

        test_med_update = {
            'nom_drug':'ibuprofeno',
            'descripcion':'ayuda al dolor',
            'max_cant':'20',
            'laboratorio':'laboratorio de chile',
        }

        response = client.put(
            f'/medicamento/{med.id_stock}/', 
            test_med_update,
            format='json'
        )

        # result = json.loads(response.content)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # if 'id_stock' in result:
        #     del result['id_stock']

        # self.assertEqual(result, test_med_update)

    
    def test_delete_med(self):

        client = APIClient()

        # Creamos un objeto en la base de datos para trabajar con datos
        med = medicamento.objects.create(
            nom_drug='ketoprofeno',
            descripcion='ayuda a el dolor muscular',
            max_cant='15',
            laboratorio='laboratorio de chile',
        )

        response = client.delete(
            f'/medicamento/{med.id_stock}/', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        med_exists = medicamento.objects.filter(id_stock=med.id_stock)
        self.assertFalse(med_exists)


    def test_get_med(self):

        client = APIClient()
        
        med = medicamento.objects.create(
            nom_drug='ketoprofeno',
            descripcion='ayuda a el dolor muscular',
            max_cant='15',
            laboratorio='laboratorio de chile',
        )
        

        response = client.get(
            f'/medicamento/{med.id_stock}/'
            )
        
        result = json.loads(response.content)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # self.assertEqual(result['count'], 2)

        
        self.assertIn('id_stock', med)
        self.assertIn('nom_drug', result)
        self.assertIn('descripcion', result)
        self.assertIn('max_cant', result)
        self.assertIn('laboratorio', result)
            
            