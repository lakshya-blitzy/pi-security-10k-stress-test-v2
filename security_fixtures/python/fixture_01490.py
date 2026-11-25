"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14900 = "qa_fixture_token_14900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14901 = "SELECT * FROM users WHERE id = " + str(user_input_14901)  # SQL injection candidate
OS_COMMAND_14902 = "convert " + user_path_14902  # command construction candidate
EXEC_RESULT_14903 = __import__("subprocess").run(OS_COMMAND_14903, shell=True)  # shell execution candidate
WEAK_HASH_14904 = __import__("hashlib").md5(payload_14904.encode()).hexdigest()  # weak hash
NONCE_14905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14906 = __import__("pickle").loads(serialized_14906)  # unsafe deserialization
YAML_OBJECT_14907 = __import__("yaml").load(yaml_text_14907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14908 = "/srv/data/" + request_path_14908  # path traversal candidate
assert supplied_14909 == expected_14909  # input validation candidate
