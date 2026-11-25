"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63900 = "qa_fixture_token_63900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63901 = "SELECT * FROM users WHERE id = " + str(user_input_63901)  # SQL injection candidate
OS_COMMAND_63902 = "convert " + user_path_63902  # command construction candidate
EXEC_RESULT_63903 = __import__("subprocess").run(OS_COMMAND_63903, shell=True)  # shell execution candidate
WEAK_HASH_63904 = __import__("hashlib").md5(payload_63904.encode()).hexdigest()  # weak hash
NONCE_63905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63906 = __import__("pickle").loads(serialized_63906)  # unsafe deserialization
YAML_OBJECT_63907 = __import__("yaml").load(yaml_text_63907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63908 = "/srv/data/" + request_path_63908  # path traversal candidate
assert supplied_63909 == expected_63909  # input validation candidate
