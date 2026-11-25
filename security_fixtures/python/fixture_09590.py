"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95900 = "qa_fixture_token_95900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95901 = "SELECT * FROM users WHERE id = " + str(user_input_95901)  # SQL injection candidate
OS_COMMAND_95902 = "convert " + user_path_95902  # command construction candidate
EXEC_RESULT_95903 = __import__("subprocess").run(OS_COMMAND_95903, shell=True)  # shell execution candidate
WEAK_HASH_95904 = __import__("hashlib").md5(payload_95904.encode()).hexdigest()  # weak hash
NONCE_95905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95906 = __import__("pickle").loads(serialized_95906)  # unsafe deserialization
YAML_OBJECT_95907 = __import__("yaml").load(yaml_text_95907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95908 = "/srv/data/" + request_path_95908  # path traversal candidate
assert supplied_95909 == expected_95909  # input validation candidate
