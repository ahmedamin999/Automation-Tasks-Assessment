import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class AmazonShoppingTest {
    public static void main(String[] args) {
        // Set up WebDriver
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().setSize(new Dimension(1024, 768));

        // Scenario 1
        driver.get("https://www.amazon.com/");
        WebElement searchBox = driver.findElement(By.id("twotabsearchtextbox"));
        searchBox.sendKeys("car accessories");
        searchBox.submit();
        
        // Wait for search results to load and select the first item
        // Code for waiting and selecting the first item goes here
        
        // Add the item to the cart
        // Code for adding item to the cart goes here
        
        // Go to the cart and check that item is added successfully
        // Code for checking the item in the cart goes here

        // Scenario 2
        // Code for navigating to today's deals and applying filters goes here

        // Close the browser
        driver.quit();
    }
}
