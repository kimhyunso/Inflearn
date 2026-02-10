package chapter2;

class Address {
    private String address;
    private String phoneNum;
    public Address(String address, String phoneNum) {
        this.address = address;
        this.phoneNum = phoneNum;
    }

    @Override
    public String toString() {
        return "Address{" +
                "address='" + address + '\'' +
                ", phoneNum='" + phoneNum + '\'' +
                '}';
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setPhoneNum(String phoneNum) {
        this.phoneNum = phoneNum;
    }

    public String getAddress() {
        return address;
    }

    public String getPhoneNum() {
        return phoneNum;
    }
}

class User {
    private String name;
    private Address address;
    public User(String name, String address, String phoneNum) {
        this.name = name;
        this.address = new Address(address, phoneNum);
    }

    public void shallowCopy(User target) {
        this.name = target.name;
        this.address = target.address;
    }

    public void deepCopy(User target) {
        this.name = target.name;
        this.address.setAddress(target.address.getAddress());
        this.address.setPhoneNum(target.address.getPhoneNum());
    }

    public String getName() {
        return name;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    public void setName(String name) {
        this.name = name;
    }
}


public class Copy {
    public static void main(String[] args) {
        User user1 = new User("hong", "seoul", "010-1111-1111");
        User user2 = new User("kim", "gyeonggi", "010-2222-2222");

        System.out.println(user1.getName());
        System.out.println(user1.getAddress());

        user1.shallowCopy(user2);

        user2.getAddress().setAddress("aaa");
        user2.getAddress().setPhoneNum("010-3333-3333");

        System.out.println(user1.getName());
        System.out.println(user1.getAddress());

        User user3 = new User("hong", "seoul", "010-1111-1111");
        User user4 = new User("kim", "gyeonggi", "010-2222-2222");

        System.out.println(user3.getName());
        System.out.println(user3.getAddress());

        user3.deepCopy(user4);

        user4.getAddress().setAddress("bbbb");
        user4.getAddress().setPhoneNum("010-4444-4444");

        System.out.println(user3.getName());
        System.out.println(user3.getAddress());
    }
}
