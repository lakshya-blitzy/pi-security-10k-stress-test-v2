"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84900 = "qa_fixture_token_84900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84901 = "SELECT * FROM users WHERE id = " + str(user_input_84901)  # SQL injection candidate
OS_COMMAND_84902 = "convert " + user_path_84902  # command construction candidate
EXEC_RESULT_84903 = __import__("subprocess").run(OS_COMMAND_84903, shell=True)  # shell execution candidate
WEAK_HASH_84904 = __import__("hashlib").md5(payload_84904.encode()).hexdigest()  # weak hash
NONCE_84905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84906 = __import__("pickle").loads(serialized_84906)  # unsafe deserialization
YAML_OBJECT_84907 = __import__("yaml").load(yaml_text_84907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84908 = "/srv/data/" + request_path_84908  # path traversal candidate
assert supplied_84909 == expected_84909  # input validation candidate
