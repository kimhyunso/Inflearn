package chapter5;

import java.util.ArrayList;
import java.util.List;

enum Week {
    MONDAY, TUESDAY, WEDNESDAY,
    THURSDAY, FRIDAY, SATURDAY, SUNDAY;
    public boolean equalMonday() {
        return this.equals(Week.MONDAY);
    }
}


public class Main1 {
    public static void main(String[] args) {
        List<Week> weekList = new ArrayList<>();

        Week week = Week.SUNDAY;
        System.out.println(Week.valueOf("MONDAY").ordinal());
        System.out.println(week.name());
        System.out.println(week.ordinal());

        for (Week w : Week.values()) {
            weekList.add(w);
            System.out.println(w.name());
        }

        Week findWeek = weekList.stream().filter(Week::equalMonday)
                .findFirst()
                .get();

        System.out.println(findWeek.name());
    }
}
