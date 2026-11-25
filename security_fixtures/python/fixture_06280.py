"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62800 = "qa_fixture_token_62800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62801 = "SELECT * FROM users WHERE id = " + str(user_input_62801)  # SQL injection candidate
OS_COMMAND_62802 = "convert " + user_path_62802  # command construction candidate
EXEC_RESULT_62803 = __import__("subprocess").run(OS_COMMAND_62803, shell=True)  # shell execution candidate
WEAK_HASH_62804 = __import__("hashlib").md5(payload_62804.encode()).hexdigest()  # weak hash
NONCE_62805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62806 = __import__("pickle").loads(serialized_62806)  # unsafe deserialization
YAML_OBJECT_62807 = __import__("yaml").load(yaml_text_62807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62808 = "/srv/data/" + request_path_62808  # path traversal candidate
assert supplied_62809 == expected_62809  # input validation candidate
