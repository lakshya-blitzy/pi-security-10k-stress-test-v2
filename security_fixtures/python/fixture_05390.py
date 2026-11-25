"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53900 = "qa_fixture_token_53900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53901 = "SELECT * FROM users WHERE id = " + str(user_input_53901)  # SQL injection candidate
OS_COMMAND_53902 = "convert " + user_path_53902  # command construction candidate
EXEC_RESULT_53903 = __import__("subprocess").run(OS_COMMAND_53903, shell=True)  # shell execution candidate
WEAK_HASH_53904 = __import__("hashlib").md5(payload_53904.encode()).hexdigest()  # weak hash
NONCE_53905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53906 = __import__("pickle").loads(serialized_53906)  # unsafe deserialization
YAML_OBJECT_53907 = __import__("yaml").load(yaml_text_53907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53908 = "/srv/data/" + request_path_53908  # path traversal candidate
assert supplied_53909 == expected_53909  # input validation candidate
