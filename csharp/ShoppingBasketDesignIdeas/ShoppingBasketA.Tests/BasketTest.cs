using NUnit.Framework;
using Assert = NUnit.Framework.Assert;

namespace ShoppingBasketA;

/*
 * Implement tests in this order:
 * 
 * Empty basket - basket contains no items
 * one item "A" - basket contains 1 item "A"
 * two items "A" - basket contains 2 items "A"
 * two items, "A" and "B" - basket contains 1 item "A"
 * Empty basket - total price 0
 * "A" costs $10, basket contains one "A" - total $10
 * "D" costs $160, basket contains one "D" - total $152 (5% discount)
 * "E" costs $250, basket contains one "E" - total $225 (10% discount)
 * Then remove the "Ignore" marking on the test that's here and hopefully it will pass!
 */
[TestFixture]
public class BasketTest
{
    [Test]
    [Ignore("WIP")]
    public void Total_Over_100_Gives_Five_Percent_Discount()
    {
        var basket = new ShoppingBasket();
        var itemA = new BasketItem("A", new decimal(10));
        var itemB = new BasketItem("B", new decimal(25));
        var itemC = new BasketItem("C", new decimal(9.99));
        basket.Add(itemA, 5);
        basket.Add(itemB, 2);
        basket.Add(itemC, 6);

        Assert.That(basket.GetQuantity("C"), Is.EqualTo(6));
        Assert.That(basket.CalculateTotal(), Is.EqualTo(new decimal(151.94)).Within(0.01));
    }
}