from apps.shop.models import Card


class Cart:
    """
    A base Cart class, providing some default behaviors that
    can be inherited or overrided as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")
        if cart == None:
            cart = self.session["session_key"] = {}
        self.cart = cart

    def __iter__(self):
        """
        Collect the cards_ids in the session data to query the database
        and return cards
        """
        # cards_ids = self.cart.keys()
        # cards = Card.objects.filter(id__in=cards_ids)

        cart = self.cart.copy()
        for i in self.cart:
            cart[i]["card"] = Card.objects.get(id=i)

        for item in cart.values():
            item["total_price"] = item["price"] * item["qty"]
        yield item

    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(int(item["qty"]) for item in self.cart.values())

    def save(self):
        self.session.modified = True

    def get_cart_total(self):
        return sum(int(item["price"]) * int(item["qty"]) for item in self.cart.values())

    def add(self, card: Card, qty, card_game):
        """
        Adding and updating the users cart session data
        """
        card_id = card.id

        if str(card_id) in self.cart:
            self.cart[str(card_id)]["qty"] = qty
        else:
            self.cart[str(card_id)] = {
                "price": int(card.price),
                "qty": qty,
                "card_game_id": card_game,
            }
        self.save()

    def update(self, card_id, qty_value):
        if card_id in self.cart:
            card = self.cart[str(card_id)]

            card["qty"] = qty_value
            self.save()

    def delete(self, card_id):
        if card_id in self.cart:
            del self.cart[card_id]
            self.save()

    def clear(self):
        del self.session["session_key"]
        self.save()
