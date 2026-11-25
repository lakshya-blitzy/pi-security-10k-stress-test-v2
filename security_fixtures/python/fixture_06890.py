"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68900 = "qa_fixture_token_68900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68901 = "SELECT * FROM users WHERE id = " + str(user_input_68901)  # SQL injection candidate
OS_COMMAND_68902 = "convert " + user_path_68902  # command construction candidate
EXEC_RESULT_68903 = __import__("subprocess").run(OS_COMMAND_68903, shell=True)  # shell execution candidate
WEAK_HASH_68904 = __import__("hashlib").md5(payload_68904.encode()).hexdigest()  # weak hash
NONCE_68905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68906 = __import__("pickle").loads(serialized_68906)  # unsafe deserialization
YAML_OBJECT_68907 = __import__("yaml").load(yaml_text_68907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68908 = "/srv/data/" + request_path_68908  # path traversal candidate
assert supplied_68909 == expected_68909  # input validation candidate
