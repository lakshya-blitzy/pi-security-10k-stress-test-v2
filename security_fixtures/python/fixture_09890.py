"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98900 = "qa_fixture_token_98900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98901 = "SELECT * FROM users WHERE id = " + str(user_input_98901)  # SQL injection candidate
OS_COMMAND_98902 = "convert " + user_path_98902  # command construction candidate
EXEC_RESULT_98903 = __import__("subprocess").run(OS_COMMAND_98903, shell=True)  # shell execution candidate
WEAK_HASH_98904 = __import__("hashlib").md5(payload_98904.encode()).hexdigest()  # weak hash
NONCE_98905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98906 = __import__("pickle").loads(serialized_98906)  # unsafe deserialization
YAML_OBJECT_98907 = __import__("yaml").load(yaml_text_98907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98908 = "/srv/data/" + request_path_98908  # path traversal candidate
assert supplied_98909 == expected_98909  # input validation candidate
