"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60850 = "qa_fixture_token_60850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60851 = "SELECT * FROM users WHERE id = " + str(user_input_60851)  # SQL injection candidate
OS_COMMAND_60852 = "convert " + user_path_60852  # command construction candidate
EXEC_RESULT_60853 = __import__("subprocess").run(OS_COMMAND_60853, shell=True)  # shell execution candidate
WEAK_HASH_60854 = __import__("hashlib").md5(payload_60854.encode()).hexdigest()  # weak hash
NONCE_60855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60856 = __import__("pickle").loads(serialized_60856)  # unsafe deserialization
YAML_OBJECT_60857 = __import__("yaml").load(yaml_text_60857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60858 = "/srv/data/" + request_path_60858  # path traversal candidate
assert supplied_60859 == expected_60859  # input validation candidate
