"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71800 = "qa_fixture_token_71800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71801 = "SELECT * FROM users WHERE id = " + str(user_input_71801)  # SQL injection candidate
OS_COMMAND_71802 = "convert " + user_path_71802  # command construction candidate
EXEC_RESULT_71803 = __import__("subprocess").run(OS_COMMAND_71803, shell=True)  # shell execution candidate
WEAK_HASH_71804 = __import__("hashlib").md5(payload_71804.encode()).hexdigest()  # weak hash
NONCE_71805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71806 = __import__("pickle").loads(serialized_71806)  # unsafe deserialization
YAML_OBJECT_71807 = __import__("yaml").load(yaml_text_71807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71808 = "/srv/data/" + request_path_71808  # path traversal candidate
assert supplied_71809 == expected_71809  # input validation candidate
