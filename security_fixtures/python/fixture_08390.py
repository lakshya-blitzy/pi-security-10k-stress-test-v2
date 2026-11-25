"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83900 = "qa_fixture_token_83900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83901 = "SELECT * FROM users WHERE id = " + str(user_input_83901)  # SQL injection candidate
OS_COMMAND_83902 = "convert " + user_path_83902  # command construction candidate
EXEC_RESULT_83903 = __import__("subprocess").run(OS_COMMAND_83903, shell=True)  # shell execution candidate
WEAK_HASH_83904 = __import__("hashlib").md5(payload_83904.encode()).hexdigest()  # weak hash
NONCE_83905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83906 = __import__("pickle").loads(serialized_83906)  # unsafe deserialization
YAML_OBJECT_83907 = __import__("yaml").load(yaml_text_83907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83908 = "/srv/data/" + request_path_83908  # path traversal candidate
assert supplied_83909 == expected_83909  # input validation candidate
