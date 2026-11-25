"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92900 = "qa_fixture_token_92900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92901 = "SELECT * FROM users WHERE id = " + str(user_input_92901)  # SQL injection candidate
OS_COMMAND_92902 = "convert " + user_path_92902  # command construction candidate
EXEC_RESULT_92903 = __import__("subprocess").run(OS_COMMAND_92903, shell=True)  # shell execution candidate
WEAK_HASH_92904 = __import__("hashlib").md5(payload_92904.encode()).hexdigest()  # weak hash
NONCE_92905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92906 = __import__("pickle").loads(serialized_92906)  # unsafe deserialization
YAML_OBJECT_92907 = __import__("yaml").load(yaml_text_92907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92908 = "/srv/data/" + request_path_92908  # path traversal candidate
assert supplied_92909 == expected_92909  # input validation candidate
