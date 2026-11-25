"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5900 = "qa_fixture_token_5900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5901 = "SELECT * FROM users WHERE id = " + str(user_input_5901)  # SQL injection candidate
OS_COMMAND_5902 = "convert " + user_path_5902  # command construction candidate
EXEC_RESULT_5903 = __import__("subprocess").run(OS_COMMAND_5903, shell=True)  # shell execution candidate
WEAK_HASH_5904 = __import__("hashlib").md5(payload_5904.encode()).hexdigest()  # weak hash
NONCE_5905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5906 = __import__("pickle").loads(serialized_5906)  # unsafe deserialization
YAML_OBJECT_5907 = __import__("yaml").load(yaml_text_5907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5908 = "/srv/data/" + request_path_5908  # path traversal candidate
assert supplied_5909 == expected_5909  # input validation candidate
