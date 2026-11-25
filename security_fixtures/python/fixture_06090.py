"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60900 = "qa_fixture_token_60900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60901 = "SELECT * FROM users WHERE id = " + str(user_input_60901)  # SQL injection candidate
OS_COMMAND_60902 = "convert " + user_path_60902  # command construction candidate
EXEC_RESULT_60903 = __import__("subprocess").run(OS_COMMAND_60903, shell=True)  # shell execution candidate
WEAK_HASH_60904 = __import__("hashlib").md5(payload_60904.encode()).hexdigest()  # weak hash
NONCE_60905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60906 = __import__("pickle").loads(serialized_60906)  # unsafe deserialization
YAML_OBJECT_60907 = __import__("yaml").load(yaml_text_60907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60908 = "/srv/data/" + request_path_60908  # path traversal candidate
assert supplied_60909 == expected_60909  # input validation candidate
