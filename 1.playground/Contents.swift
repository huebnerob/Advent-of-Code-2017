//: Playground - noun: a place where people can play

import UIKit

let input = Array("1111")

for i in 0..<input.count {
    let values = (Int(input[i%input.count]),
                  Int(input[(i+1)%input.count]))
    if values.0 == values.1 {
        print("\(values.0) + \(values.1) = ")
        Int()
    }
}
