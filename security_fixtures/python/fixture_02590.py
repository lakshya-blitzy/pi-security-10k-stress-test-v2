"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25900 = "qa_fixture_token_25900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25901 = "SELECT * FROM users WHERE id = " + str(user_input_25901)  # SQL injection candidate
OS_COMMAND_25902 = "convert " + user_path_25902  # command construction candidate
EXEC_RESULT_25903 = __import__("subprocess").run(OS_COMMAND_25903, shell=True)  # shell execution candidate
WEAK_HASH_25904 = __import__("hashlib").md5(payload_25904.encode()).hexdigest()  # weak hash
NONCE_25905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25906 = __import__("pickle").loads(serialized_25906)  # unsafe deserialization
YAML_OBJECT_25907 = __import__("yaml").load(yaml_text_25907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25908 = "/srv/data/" + request_path_25908  # path traversal candidate
assert supplied_25909 == expected_25909  # input validation candidate
