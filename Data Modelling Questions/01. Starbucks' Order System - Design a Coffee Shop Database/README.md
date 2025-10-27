Starbucks is opening a new location and needs a simple order management system. As a data engineer, you need to create a database that tracks orders, products, and basic customer information.

## Your task is to design a data model that:
- Manages a menu of available drinks and food items
- Tracks customer orders and their status
- Handles basic customizations for drinks (size, milk type, add-ins)
- Supports a simple loyalty program (points per purchase)
- Enables daily, weekly, and monthly sales reporting

## Specific requirements:
- Each order can contain multiple items
- Drinks can have various customizations
- Customers can earn loyalty points for their purchases
- The system needs to track inventory for popular items
- Daily sales reports should be easy to generate

---
---

## 1. Translate business requirements into entities and relationships 

| Area | Entities |
|-----------|-----------|
| Menu | Product, Customisation |
| Orders | Order, OrderItems |
| Customers | Customer, LoyaltyTransaction |
| Inventory | InventoryItem |

## 2. Key relationships

- A Customer can place many Orders.
- Each Order can have multiple OrderItems.
- Each OrderItem is linked to a Product.
- A Product (Drink) can have multiple Customisations.
- Each OrderItem can have multiple Customisations applied.
- Loyalty points are earned per order.

## 3. ER diagram

![ER diagram](https://github.com/user-attachments/assets/d9f3a449-1318-4701-8fdf-f0a0b3d3a647)

## 4. SQL DDL statements

```sql
CREATE TABLE "Products" (
	"product_id" INTEGER NOT NULL UNIQUE,
	"name" VARCHAR(255) NOT NULL,
	"base_price" DECIMAL NOT NULL,
	"category" ENUM NOT NULL,
	PRIMARY KEY("product_id")
);

CREATE TABLE "Inventory" (
	"inventory_id" INTEGER NOT NULL UNIQUE,
	"product_id_fk" INTEGER NOT NULL,
	"quantity" INTEGER NOT NULL,
	"last_updated" TIMESTAMP NOT NULL,
	PRIMARY KEY("inventory_id")
);

CREATE TABLE "Orders" (
	"order_id" INTEGER NOT NULL UNIQUE,
	"customer_id_fk" INTEGER NOT NULL,
	"order_date" DATE NOT NULL,
	"status" ENUM NOT NULL,
	"total_amount" DECIMAL NOT NULL,
	PRIMARY KEY("order_id")
);

CREATE TABLE "OrderItems" (
	"order_item_id" INTEGER NOT NULL UNIQUE,
	"order_id_fk" INTEGER NOT NULL,
	"product_id_fk" INTEGER NOT NULL,
	"quantity" INTEGER NOT NULL,
	"price" DECIMAL NOT NULL,
	PRIMARY KEY("order_item_id")
);

CREATE TABLE "Customisation" (
	"customisation_id" INTEGER NOT NULL UNIQUE,
	"type" ENUM NOT NULL,
	"extra_cost" DECIMAL NOT NULL,
	PRIMARY KEY("customisation_id")
);

CREATE TABLE "OrderItemCustomisations" (
	"order_item_custom_id" INTEGER NOT NULL UNIQUE,
	"order_item_id_fk" INTEGER NOT NULL,
	"customisation_id_fk" INTEGER NOT NULL,
	PRIMARY KEY("order_item_custom_id")
);

CREATE TABLE "Customers" (
	"id" INTEGER NOT NULL UNIQUE,
	"name" VARCHAR(255) NOT NULL,
	"email" VARCHAR(255) NOT NULL,
	"phone" VARCHAR(255) NOT NULL,
	"loyalty_points" INTEGER NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE "LoyaltyTransactions" (
	"loyalty_trxn_id" INTEGER NOT NULL UNIQUE,
	"customer_id_fk" INTEGER NOT NULL,
	"order_id_fk" INTEGER NOT NULL,
	"points_earned" INTEGER,
	"points_redeemed" INTEGER,
	"txn_date" TIMESTAMP NOT NULL,
	PRIMARY KEY("loyalty_trxn_id")
);
ALTER TABLE "Products"
ADD FOREIGN KEY("product_id") REFERENCES "Customers"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Inventory"
ADD FOREIGN KEY("product_id_fk") REFERENCES "Products"("product_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Orders"
ADD FOREIGN KEY("customer_id_fk") REFERENCES "Customers"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "OrderItems"
ADD FOREIGN KEY("order_id_fk") REFERENCES "Orders"("order_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "OrderItems"
ADD FOREIGN KEY("product_id_fk") REFERENCES "Products"("product_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "OrderItemCustomisations"
ADD FOREIGN KEY("order_item_id_fk") REFERENCES "OrderItems"("order_item_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "OrderItemCustomisations"
ADD FOREIGN KEY("customisation_id_fk") REFERENCES "Customisation"("customisation_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "LoyaltyTransactions"
ADD FOREIGN KEY("customer_id_fk") REFERENCES "Customers"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "LoyaltyTransactions"
ADD FOREIGN KEY("order_id_fk") REFERENCES "Orders"("order_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
```