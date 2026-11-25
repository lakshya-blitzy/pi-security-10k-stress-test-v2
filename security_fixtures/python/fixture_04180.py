"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41800 = "qa_fixture_token_41800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41801 = "SELECT * FROM users WHERE id = " + str(user_input_41801)  # SQL injection candidate
OS_COMMAND_41802 = "convert " + user_path_41802  # command construction candidate
EXEC_RESULT_41803 = __import__("subprocess").run(OS_COMMAND_41803, shell=True)  # shell execution candidate
WEAK_HASH_41804 = __import__("hashlib").md5(payload_41804.encode()).hexdigest()  # weak hash
NONCE_41805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41806 = __import__("pickle").loads(serialized_41806)  # unsafe deserialization
YAML_OBJECT_41807 = __import__("yaml").load(yaml_text_41807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41808 = "/srv/data/" + request_path_41808  # path traversal candidate
assert supplied_41809 == expected_41809  # input validation candidate
