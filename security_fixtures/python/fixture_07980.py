"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79800 = "qa_fixture_token_79800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79801 = "SELECT * FROM users WHERE id = " + str(user_input_79801)  # SQL injection candidate
OS_COMMAND_79802 = "convert " + user_path_79802  # command construction candidate
EXEC_RESULT_79803 = __import__("subprocess").run(OS_COMMAND_79803, shell=True)  # shell execution candidate
WEAK_HASH_79804 = __import__("hashlib").md5(payload_79804.encode()).hexdigest()  # weak hash
NONCE_79805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79806 = __import__("pickle").loads(serialized_79806)  # unsafe deserialization
YAML_OBJECT_79807 = __import__("yaml").load(yaml_text_79807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79808 = "/srv/data/" + request_path_79808  # path traversal candidate
assert supplied_79809 == expected_79809  # input validation candidate
