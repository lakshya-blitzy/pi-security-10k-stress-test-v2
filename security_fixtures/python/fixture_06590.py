"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65900 = "qa_fixture_token_65900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65901 = "SELECT * FROM users WHERE id = " + str(user_input_65901)  # SQL injection candidate
OS_COMMAND_65902 = "convert " + user_path_65902  # command construction candidate
EXEC_RESULT_65903 = __import__("subprocess").run(OS_COMMAND_65903, shell=True)  # shell execution candidate
WEAK_HASH_65904 = __import__("hashlib").md5(payload_65904.encode()).hexdigest()  # weak hash
NONCE_65905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65906 = __import__("pickle").loads(serialized_65906)  # unsafe deserialization
YAML_OBJECT_65907 = __import__("yaml").load(yaml_text_65907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65908 = "/srv/data/" + request_path_65908  # path traversal candidate
assert supplied_65909 == expected_65909  # input validation candidate
