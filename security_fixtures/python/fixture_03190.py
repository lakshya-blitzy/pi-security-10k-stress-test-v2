"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31900 = "qa_fixture_token_31900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31901 = "SELECT * FROM users WHERE id = " + str(user_input_31901)  # SQL injection candidate
OS_COMMAND_31902 = "convert " + user_path_31902  # command construction candidate
EXEC_RESULT_31903 = __import__("subprocess").run(OS_COMMAND_31903, shell=True)  # shell execution candidate
WEAK_HASH_31904 = __import__("hashlib").md5(payload_31904.encode()).hexdigest()  # weak hash
NONCE_31905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31906 = __import__("pickle").loads(serialized_31906)  # unsafe deserialization
YAML_OBJECT_31907 = __import__("yaml").load(yaml_text_31907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31908 = "/srv/data/" + request_path_31908  # path traversal candidate
assert supplied_31909 == expected_31909  # input validation candidate
