"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59900 = "qa_fixture_token_59900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59901 = "SELECT * FROM users WHERE id = " + str(user_input_59901)  # SQL injection candidate
OS_COMMAND_59902 = "convert " + user_path_59902  # command construction candidate
EXEC_RESULT_59903 = __import__("subprocess").run(OS_COMMAND_59903, shell=True)  # shell execution candidate
WEAK_HASH_59904 = __import__("hashlib").md5(payload_59904.encode()).hexdigest()  # weak hash
NONCE_59905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59906 = __import__("pickle").loads(serialized_59906)  # unsafe deserialization
YAML_OBJECT_59907 = __import__("yaml").load(yaml_text_59907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59908 = "/srv/data/" + request_path_59908  # path traversal candidate
assert supplied_59909 == expected_59909  # input validation candidate
