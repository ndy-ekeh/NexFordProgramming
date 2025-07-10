set.seed(123)

#Generating worker number
workerGeneration <- function(number_workers = 400) {
  firstname <- c('Kunmi', 'Deji', 'Eyiwunmi', 'Oke', 'Somto', 'Stephen', 'Emeka', 'Joy')
  lastname <- c('Ode', 'John', 'Olawore', 'Kenneth', 'Peter', 'Enua', 'Orji', 'Azu')
  gender <- c('Male', 'Female')

  workersarrary <- data.frame(
    id = sample(1000:9999, number_workers, replace = TRUE),
    fullname = paste(sample(firstname, number_workers, replace = TRUE),
                 sample(lastname, number_workers, replace = TRUE)),
    gender = sample(gender, number_workers, replace = TRUE),
    salary = round(runif(number_workers, 5000, 30000), 2),
    stringsAsFactors = FALSE
  )
  
  return(workersarrary)
}

#Generate Payment Slips
generatePaymentSlips <- function(workers) {
  for (i in 1:nrow(workers)) {
    worker <- workers[i, ]
    
    level <- "Unassigned"
    tryCatch({
      if (worker$salary > 10000 && worker$salary < 20000) {
        level <- "A1"
      }
      if (worker$salary > 7500 && worker$salary < 30000 && worker$gender == "Female") {
        level <- "A5-F"
      }
      
      cat(sprintf("Payment Slip for %s (ID: %d)\n", worker$fullname, worker$id))
      cat(sprintf("Gender: %s\n", worker$gender))
      cat(sprintf("Salary: $%.2f\n", worker$salary))
      cat(sprintf("Employee Level: %s\n", level))
      cat(rep("=", 40), "\n", sep = "")
    }, error = function(e) {
      cat("Error processing worker:", conditionMessage(e), "\n")
    })
  }
}




workers <- workerGeneration()
generatePaymentSlips(workers)