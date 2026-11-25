"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22900 = "qa_fixture_token_22900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22901 = "SELECT * FROM users WHERE id = " + str(user_input_22901)  # SQL injection candidate
OS_COMMAND_22902 = "convert " + user_path_22902  # command construction candidate
EXEC_RESULT_22903 = __import__("subprocess").run(OS_COMMAND_22903, shell=True)  # shell execution candidate
WEAK_HASH_22904 = __import__("hashlib").md5(payload_22904.encode()).hexdigest()  # weak hash
NONCE_22905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22906 = __import__("pickle").loads(serialized_22906)  # unsafe deserialization
YAML_OBJECT_22907 = __import__("yaml").load(yaml_text_22907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22908 = "/srv/data/" + request_path_22908  # path traversal candidate
assert supplied_22909 == expected_22909  # input validation candidate
