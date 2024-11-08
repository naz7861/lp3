#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Job
{
public:
    char id;
    int deadline;
    int profit;

    Job(char id, int deadline, int profit)
    {
        this->id = id;
        this->deadline = deadline;
        this->profit = profit;
    }
};

bool compare(Job j1, Job j2)
{
    return j1.profit > j2.profit;
}

void printJobSequence(vector<Job> jobs)
{
    // Sort jobs in descending order of profit
    sort(jobs.begin(), jobs.end(), compare);

    // Find the maximum deadline
    int maxDeadline = 0;
    for (Job job : jobs)
    {
        maxDeadline = max(maxDeadline, job.deadline);
    }

    // Initialize result and slot arrays
    vector<char> result(maxDeadline, 'X');
    vector<bool> slot(maxDeadline, false);

    // Assign jobs to slots
    for (int i = 0; i < jobs.size(); i++)
    {
        for (int j = min(maxDeadline - 1, jobs[i].deadline - 1); j >= 0; j--)
        {
            if (!slot[j])
            {
                result[j] = jobs[i].id;
                slot[j] = true;
                break;
            }
        }
    }

    // Print the job sequence
    cout << "Job Sequence: ";
    for (char jobId : result)
    {
        if (jobId != 'X')
        {
            cout << jobId << " ";
        }
    }
    cout << endl;

    // Calculate total profit
    int totalProfit = 0;
    for (int i = 0; i < maxDeadline; i++)
    {
        if (slot[i])
        {
            for (Job job : jobs)
            {
                if (job.id == result[i])
                {
                    totalProfit += job.profit;
                    break;
                }
            }
        }
    }
    cout << "Total Profit: " << totalProfit << endl;
}

int main()
{
    int n;
    cout << "Enter number of jobs: ";
    cin >> n;

    vector<Job> jobs;
    cout << "Enter jobs in the format (id deadline profit):" << endl;
    for (int i = 0; i < n; i++)
    {
        char id;
        int deadline, profit;
        cin >> id >> deadline >> profit;
        jobs.push_back(Job(id, deadline, profit));
    }

    printJobSequence(jobs);
    return 0;
}
