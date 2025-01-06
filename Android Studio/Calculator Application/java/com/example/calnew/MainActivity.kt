package com.example.calnew

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.calnew.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private var currentNumber: Long = 0
    private var calculatedResult: Long = 0
    private var selectedOperation: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setupNumberButtons()
        setupOperationButtons()
    }

    private fun setupNumberButtons() {
        val numberButtons = listOf(
            binding.shahinButton0 to 0,
            binding.shahinButton1 to 1,
            binding.shahinButton2 to 2,
            binding.shahinButton3 to 3,
            binding.shahinButton4 to 4,
            binding.shahinButton5 to 5,
            binding.shahinButton6 to 6,
            binding.shahinButton7 to 7,
            binding.shahinButton8 to 8,
            binding.shahinButton9 to 9
        )

        numberButtons.forEach { (button, number) ->
            button.setOnClickListener { appendNumber(number) }
        }

        binding.shahinButtonAc.setOnClickListener { clearAll() }
    }

    private fun setupOperationButtons() {
        binding.shahinButtonPlus.setOnClickListener { setOperation("+") }
        binding.shahinButtonMinus.setOnClickListener { setOperation("-") }
        binding.shahinButtonMultiply.setOnClickListener { setOperation("*") }
        binding.shahinButtonDivide.setOnClickListener { setOperation("/") }
        binding.shahinButtonReminder.setOnClickListener { setOperation("%") }
        binding.shahinButtonTavan.setOnClickListener { setOperation("**") }
        binding.shahinButtonEquals.setOnClickListener { calculateResult() }

        binding.shahinButtonMax.setOnClickListener {
            if (calculatedResult == 0L) {
                calculatedResult = currentNumber
            } else {
                calculatedResult = maxOf(calculatedResult, currentNumber)
            }
            binding.shahinText.text = calculatedResult.toString()
            currentNumber = 0
        }

        binding.shahinButtonFactor.setOnClickListener {
            if (currentNumber >= 0) {
                calculatedResult = factorial(currentNumber)
                binding.shahinText.text = calculatedResult.toString()
            } else {
                binding.shahinText.text = "Error"
            }
            currentNumber = 0
        }
    }

    private fun appendNumber(number: Int) {
        currentNumber = currentNumber * 10 + number
        binding.shahinText.text = currentNumber.toString()
    }

    private fun setOperation(operation: String) {
        if (selectedOperation == null) {
            calculatedResult = currentNumber
            currentNumber = 0
        } else {
            calculateResult()
        }
        selectedOperation = operation
    }

    private fun calculateResult() {
        when (selectedOperation) {
            "+" -> calculatedResult += currentNumber
            "-" -> calculatedResult -= currentNumber
            "*" -> calculatedResult *= currentNumber
            "**" -> calculatedResult = Math.pow(calculatedResult.toDouble(), currentNumber.toDouble()).toLong()
            "/" -> {
                if (currentNumber != 0L) {
                    calculatedResult /= currentNumber
                } else {
                    binding.shahinText.text = "Error"
                    clearAll()
                    return
                }
            }
            "%" -> calculatedResult %= currentNumber
        }
        binding.shahinText.text = calculatedResult.toString()
        currentNumber = 0
        selectedOperation = null
    }

    private fun clearAll() {
        currentNumber = 0
        calculatedResult = 0
        selectedOperation = null
        binding.shahinText.text = "0"
    }

    private fun factorial(number: Long): Long {
        return if (number <= 1) 1 else number * factorial(number - 1)
    }
}
