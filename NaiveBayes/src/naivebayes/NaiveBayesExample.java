/* 
 * Copyright (C) 2014 Vasilis Vryniotis <bbriniotis at datumbox.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package naivebayes;

import naivebayes.NaiveBayes;
import naivebayes.NaiveBayesKnowledgeBase;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 *
 * @author Vasilis Vryniotis <bbriniotis at datumbox.com>
 * @see <a href="http://blog.datumbox.com/developing-a-naive-bayes-text-classifier-in-java/">http://blog.datumbox.com/developing-a-naive-bayes-text-classifier-in-java/</a>
 */
public class NaiveBayesExample {

    /**
     * Reads the all lines from a file and places it a String array. In each 
     * record in the String array we store a training example text.
     * 
     * @param url
     * @return
     * @throws IOException 
     */
    public static String[] readLines(String url) throws IOException {

        //Reader fileReader = new InputStreamReader(url.openStream(), Charset.forName("UTF-8"));
        List<String> lines;
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(url))) {
            lines = new ArrayList<>();
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                lines.add(line);
            }
        }
        return lines.toArray(new String[lines.size()]);
    }
    
    /**
     * Main method
     * 
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException {
        //map of dataset files
        Map<String, String> trainingFiles = new HashMap<>();
        trainingFiles.put("технологија","D://Sedmi_Semestar//PHP//Seminarska//smartportal//content.txt");
        trainingFiles.put("музика","D://Sedmi_Semestar//PHP//Seminarska//antenna5//content.txt");
        trainingFiles.put("фудбал","D://Sedmi_Semestar//PHP//Seminarska//24fudbal//content.txt");
        trainingFiles.put("астрономија","D://Sedmi_Semestar//PHP//Seminarska//astronomija//content.txt");
        trainingFiles.put("спорт","D://Sedmi_Semestar//PHP//Seminarska//ekipa//content.txt");
        trainingFiles.put("мода","D://Sedmi_Semestar//PHP//Seminarska//fashionel//content.txt");
        trainingFiles.put("стил на живеење","D://Sedmi_Semestar//PHP//Seminarska//kafepauza//content.txt");
        
        
        //loading examples in memory
        Map<String, String[]> trainingExamples = new HashMap<>();
        for(Map.Entry<String, String> entry : trainingFiles.entrySet()) {
            trainingExamples.put(entry.getKey(), readLines(entry.getValue()));
        }
        
        //train classifier
        NaiveBayes nb = new NaiveBayes();
        nb.setChisquareCriticalValue(6.63); //0.01 pvalue
        nb.train(trainingExamples);
        
        //get trained classifier knowledgeBase
        NaiveBayesKnowledgeBase knowledgeBase = nb.getKnowledgeBase();
        
        nb = null;
        trainingExamples = null;
        
        
        //Use classifier
        nb = new NaiveBayes(knowledgeBase);
        
        Scanner scanner = new Scanner(System.in);
        
        while(true){
        System.out.println("Внесете реченица: ");
        String exampleEn = scanner.nextLine();
        String outputEn = nb.predict(exampleEn);
        System.out.format("Реченицата \"%s\" беше класифицирана како \"%s\".%n", exampleEn, outputEn);
       
        }
      //  scanner.close();
       

    }
    
}
