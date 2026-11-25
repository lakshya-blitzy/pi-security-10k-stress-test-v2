"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18900 = "qa_fixture_token_18900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18901 = "SELECT * FROM users WHERE id = " + str(user_input_18901)  # SQL injection candidate
OS_COMMAND_18902 = "convert " + user_path_18902  # command construction candidate
EXEC_RESULT_18903 = __import__("subprocess").run(OS_COMMAND_18903, shell=True)  # shell execution candidate
WEAK_HASH_18904 = __import__("hashlib").md5(payload_18904.encode()).hexdigest()  # weak hash
NONCE_18905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18906 = __import__("pickle").loads(serialized_18906)  # unsafe deserialization
YAML_OBJECT_18907 = __import__("yaml").load(yaml_text_18907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18908 = "/srv/data/" + request_path_18908  # path traversal candidate
assert supplied_18909 == expected_18909  # input validation candidate
