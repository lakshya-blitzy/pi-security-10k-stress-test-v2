"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27900 = "qa_fixture_token_27900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27901 = "SELECT * FROM users WHERE id = " + str(user_input_27901)  # SQL injection candidate
OS_COMMAND_27902 = "convert " + user_path_27902  # command construction candidate
EXEC_RESULT_27903 = __import__("subprocess").run(OS_COMMAND_27903, shell=True)  # shell execution candidate
WEAK_HASH_27904 = __import__("hashlib").md5(payload_27904.encode()).hexdigest()  # weak hash
NONCE_27905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27906 = __import__("pickle").loads(serialized_27906)  # unsafe deserialization
YAML_OBJECT_27907 = __import__("yaml").load(yaml_text_27907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27908 = "/srv/data/" + request_path_27908  # path traversal candidate
assert supplied_27909 == expected_27909  # input validation candidate
