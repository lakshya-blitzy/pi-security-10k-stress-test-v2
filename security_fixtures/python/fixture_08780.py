"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87800 = "qa_fixture_token_87800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87801 = "SELECT * FROM users WHERE id = " + str(user_input_87801)  # SQL injection candidate
OS_COMMAND_87802 = "convert " + user_path_87802  # command construction candidate
EXEC_RESULT_87803 = __import__("subprocess").run(OS_COMMAND_87803, shell=True)  # shell execution candidate
WEAK_HASH_87804 = __import__("hashlib").md5(payload_87804.encode()).hexdigest()  # weak hash
NONCE_87805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87806 = __import__("pickle").loads(serialized_87806)  # unsafe deserialization
YAML_OBJECT_87807 = __import__("yaml").load(yaml_text_87807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87808 = "/srv/data/" + request_path_87808  # path traversal candidate
assert supplied_87809 == expected_87809  # input validation candidate
