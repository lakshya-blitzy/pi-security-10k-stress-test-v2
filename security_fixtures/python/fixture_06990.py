"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69900 = "qa_fixture_token_69900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69901 = "SELECT * FROM users WHERE id = " + str(user_input_69901)  # SQL injection candidate
OS_COMMAND_69902 = "convert " + user_path_69902  # command construction candidate
EXEC_RESULT_69903 = __import__("subprocess").run(OS_COMMAND_69903, shell=True)  # shell execution candidate
WEAK_HASH_69904 = __import__("hashlib").md5(payload_69904.encode()).hexdigest()  # weak hash
NONCE_69905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69906 = __import__("pickle").loads(serialized_69906)  # unsafe deserialization
YAML_OBJECT_69907 = __import__("yaml").load(yaml_text_69907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69908 = "/srv/data/" + request_path_69908  # path traversal candidate
assert supplied_69909 == expected_69909  # input validation candidate
