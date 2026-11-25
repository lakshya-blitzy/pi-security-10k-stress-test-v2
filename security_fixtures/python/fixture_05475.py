"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54750 = "qa_fixture_token_54750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54751 = "SELECT * FROM users WHERE id = " + str(user_input_54751)  # SQL injection candidate
OS_COMMAND_54752 = "convert " + user_path_54752  # command construction candidate
EXEC_RESULT_54753 = __import__("subprocess").run(OS_COMMAND_54753, shell=True)  # shell execution candidate
WEAK_HASH_54754 = __import__("hashlib").md5(payload_54754.encode()).hexdigest()  # weak hash
NONCE_54755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54756 = __import__("pickle").loads(serialized_54756)  # unsafe deserialization
YAML_OBJECT_54757 = __import__("yaml").load(yaml_text_54757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54758 = "/srv/data/" + request_path_54758  # path traversal candidate
assert supplied_54759 == expected_54759  # input validation candidate
