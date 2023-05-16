"""Add values

Revision ID: 003
Revises: 
Create Date: 2023-05-05 18:24:59.501485

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '003'
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("INSERT INTO category (id,name) "
               "VALUES "
               "(1,'for_body'),"
               "(2,'for_hair'),"
               "(3,'for_face')")
    op.execute("INSERT INTO subcategory (id,name,category_id)"
               "VALUES "
               "(1,'shower_gel',1),"
               "(2,'body_scrub',1),"
               "(3,'body_cream',1),"
               "(4,'shampoo',2),"
               "(5,'balm',2),"
               "(6,'conditioner',2),"
               "(7,'mask',2),"
               "(8,'cream',3),"
               "(9,'mask_for_face',3),"
               "(10,'serum',3),"
               "(11,'gel',3),"
               "(12,'micellar_water',3)")
    op.execute("INSERT INTO product (id,vendor_code,name,price,quantity,status,subcategory_id)"
               "VALUES "
               "(1,1123,'shower_gel_coconut',2,1540,'ACTIVE',1),"
               "(2,1235,'shower_gel_apple',1.98,1850,'ACTIVE',1),"
               "(3,1023,'shower_gel_mango',2.3,1485,'ACTIVE',1),"
               "(4,1021,'body_scrub_vanilla',3.3,1489,'ACTIVE',2),"
               "(5,1022,'body_scrub_cherry',3.3,1021,'ACTIVE',2),"
               "(6,1024,'body_scrub_chocolate',3.3,980,'ACTIVE',2),"
               "(7,1026,'body_cream_nuts',3.3,1100,'ACTIVE',3),"
               "(8,1027,'body_cream_tiramisu',3.3,1650,'ACTIVE',3),"
               "(9,1028,'body_cream_coffe',3.3,1542,'ACTIVE',3),"
               "(10,1029,'shampoo_fresh',2.7,976,'ACTIVE',4),"
               "(11,1030,'anti_dandruff_shampoo_',2.8,198,'ACTIVE',4),"
               "(12,1031,'shampoo_for_color_hair',2.8,785,'ACTIVE',4),"
               "(13,1032,'balm_for_split_ends',2,1335,'ACTIVE',5),"
               "(14,1033,'balm_for_weak_hair',2.3,1254,'ACTIVE',5),"
               "(15,1034,'balm_for_color_hair',2.2,1125,'ACTIVE',5),"
               "(16,1036,'conditioner_for_split_ends',3.3,1320,'ACTIVE',6),"
               "(17,1037,'conditioner_for_weak_hair',3.3,1501,'ACTIVE',6),"
               "(18,1038,'conditioner_for_color_hair',3.3,1120,'ACTIVE',6),"
               "(19,1039,'mask_for_weak_hair',2.3,1320,'ACTIVE',7),"
               "(20,1040,'mask_for_slit_ends',2.2,1320,'ACTIVE',7),"
               "(21,1014,'mask_for_falling_hair',2.2,1345,'ACTIVE',7),"
               "(22,1042,'night_cream',3.6,1540,'ACTIVE',8),"
               "(23,1043,'morning_cream',3.6,1140,'ACTIVE',8),"
               "(24,1044,'intensive_cream',3.8,1360,'ACTIVE',8),"
               "(25,1045,'mask_for_face_hyaluron',1.3,1045,'ACTIVE',9),"
               "(26,1046,'mask_for_face_snail_mucin',1.5,1023,'ACTIVE',9),"
               "(27,1047,'mask_for_face_collagen',1.5,1036,'ACTIVE',9),"
               "(28,1048,'serum_collagen',4.1,1068,'ACTIVE',10),"
               "(29,1049,'serum_hyaluron',4.2,1155,'ACTIVE',10),"
               "(30,1050,'serum_c_vit',4.2,1365,'ACTIVE',10),"
               "(31,1051,'gel_for_dry_skin',2.3,0,'ACTIVE',11),"
               "(32,1052,'gel_for_oily_skin',2.6,1550,'ACTIVE',11),"
               "(33,1053,'gel_for_combi_skin',2.5,1574,'ACTIVE',11),"
               "(34,1054,'micellar_water_for_combi_skin',4.2,1145,'ACTIVE',12),"
               "(35,1055,'micellar_water_for_oily_skin',4.1,1440,'ACTIVE',12),"
               "(36,1056,'micellar_water_for_dry_skin',4.2,1870,'ACTIVE',12)")
    op.execute("INSERT INTO characteristic (id,name)"
                "VALUES" 
                "(1,'yellow'),"
                "(2,'red'),"
                "(3,'green'),"
                "(4,'white')")
    op.execute("INSERT INTO product_character_link (product_id,characteristic_id)"
                "VALUES (1,2),"
                "(1,1),"
                "(2,4),"
                "(3,2),"
                "(4,3),"
                "(5,1),"
                "(6,2),"
                "(7,1),"
                "(8,4),"
                "(9,2),"
                "(10,4),"
                "(11,1),"
                "(12,3),"
                "(13,2),"
                "(14,3),"
                "(15,2),"
                "(16,4),"
                "(17,3),"
                "(18,2),"
                "(19,4),"
                "(20,3),"
                "(21,2),"
                "(22,4),"
                "(23,2),"
                "(24,3),"
                "(25,1),"
                "(26,1),"
                "(27,2),"
                "(28,3),"
                "(29,4),"
                "(30,1),"
                "(31,2),"
                "(32,4),"
                "(33,3),"
                "(34,1),"
                "(35,2),"
                "(36,1);")


def downgrade() -> None:
    op.execute("DELETE FROM product_character_link")
    op.execute("DELETE FROM characteristic")
    op.execute("DELETE FROM product")
    op.execute("DELETE FROM subcategory")
    op.execute("DELETE FROM category")
