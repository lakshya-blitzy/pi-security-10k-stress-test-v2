"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61900 = "qa_fixture_token_61900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61901 = "SELECT * FROM users WHERE id = " + str(user_input_61901)  # SQL injection candidate
OS_COMMAND_61902 = "convert " + user_path_61902  # command construction candidate
EXEC_RESULT_61903 = __import__("subprocess").run(OS_COMMAND_61903, shell=True)  # shell execution candidate
WEAK_HASH_61904 = __import__("hashlib").md5(payload_61904.encode()).hexdigest()  # weak hash
NONCE_61905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61906 = __import__("pickle").loads(serialized_61906)  # unsafe deserialization
YAML_OBJECT_61907 = __import__("yaml").load(yaml_text_61907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61908 = "/srv/data/" + request_path_61908  # path traversal candidate
assert supplied_61909 == expected_61909  # input validation candidate
