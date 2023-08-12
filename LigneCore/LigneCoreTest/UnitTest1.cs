using LigneCore;

namespace LigneCoreTest;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        Class1 class1 = new Class1();
        Assert.Equal("aab", class1.m());
    }
}
