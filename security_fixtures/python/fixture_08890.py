"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88900 = "qa_fixture_token_88900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88901 = "SELECT * FROM users WHERE id = " + str(user_input_88901)  # SQL injection candidate
OS_COMMAND_88902 = "convert " + user_path_88902  # command construction candidate
EXEC_RESULT_88903 = __import__("subprocess").run(OS_COMMAND_88903, shell=True)  # shell execution candidate
WEAK_HASH_88904 = __import__("hashlib").md5(payload_88904.encode()).hexdigest()  # weak hash
NONCE_88905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88906 = __import__("pickle").loads(serialized_88906)  # unsafe deserialization
YAML_OBJECT_88907 = __import__("yaml").load(yaml_text_88907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88908 = "/srv/data/" + request_path_88908  # path traversal candidate
assert supplied_88909 == expected_88909  # input validation candidate
