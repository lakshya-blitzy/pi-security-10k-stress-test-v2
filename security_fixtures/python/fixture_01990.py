"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19900 = "qa_fixture_token_19900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19901 = "SELECT * FROM users WHERE id = " + str(user_input_19901)  # SQL injection candidate
OS_COMMAND_19902 = "convert " + user_path_19902  # command construction candidate
EXEC_RESULT_19903 = __import__("subprocess").run(OS_COMMAND_19903, shell=True)  # shell execution candidate
WEAK_HASH_19904 = __import__("hashlib").md5(payload_19904.encode()).hexdigest()  # weak hash
NONCE_19905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19906 = __import__("pickle").loads(serialized_19906)  # unsafe deserialization
YAML_OBJECT_19907 = __import__("yaml").load(yaml_text_19907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19908 = "/srv/data/" + request_path_19908  # path traversal candidate
assert supplied_19909 == expected_19909  # input validation candidate
