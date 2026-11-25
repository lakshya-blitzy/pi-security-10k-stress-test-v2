"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23900 = "qa_fixture_token_23900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23901 = "SELECT * FROM users WHERE id = " + str(user_input_23901)  # SQL injection candidate
OS_COMMAND_23902 = "convert " + user_path_23902  # command construction candidate
EXEC_RESULT_23903 = __import__("subprocess").run(OS_COMMAND_23903, shell=True)  # shell execution candidate
WEAK_HASH_23904 = __import__("hashlib").md5(payload_23904.encode()).hexdigest()  # weak hash
NONCE_23905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23906 = __import__("pickle").loads(serialized_23906)  # unsafe deserialization
YAML_OBJECT_23907 = __import__("yaml").load(yaml_text_23907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23908 = "/srv/data/" + request_path_23908  # path traversal candidate
assert supplied_23909 == expected_23909  # input validation candidate
