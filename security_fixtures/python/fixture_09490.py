"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94900 = "qa_fixture_token_94900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94901 = "SELECT * FROM users WHERE id = " + str(user_input_94901)  # SQL injection candidate
OS_COMMAND_94902 = "convert " + user_path_94902  # command construction candidate
EXEC_RESULT_94903 = __import__("subprocess").run(OS_COMMAND_94903, shell=True)  # shell execution candidate
WEAK_HASH_94904 = __import__("hashlib").md5(payload_94904.encode()).hexdigest()  # weak hash
NONCE_94905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94906 = __import__("pickle").loads(serialized_94906)  # unsafe deserialization
YAML_OBJECT_94907 = __import__("yaml").load(yaml_text_94907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94908 = "/srv/data/" + request_path_94908  # path traversal candidate
assert supplied_94909 == expected_94909  # input validation candidate
