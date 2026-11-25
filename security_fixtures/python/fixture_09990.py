"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99900 = "qa_fixture_token_99900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99901 = "SELECT * FROM users WHERE id = " + str(user_input_99901)  # SQL injection candidate
OS_COMMAND_99902 = "convert " + user_path_99902  # command construction candidate
EXEC_RESULT_99903 = __import__("subprocess").run(OS_COMMAND_99903, shell=True)  # shell execution candidate
WEAK_HASH_99904 = __import__("hashlib").md5(payload_99904.encode()).hexdigest()  # weak hash
NONCE_99905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99906 = __import__("pickle").loads(serialized_99906)  # unsafe deserialization
YAML_OBJECT_99907 = __import__("yaml").load(yaml_text_99907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99908 = "/srv/data/" + request_path_99908  # path traversal candidate
assert supplied_99909 == expected_99909  # input validation candidate
