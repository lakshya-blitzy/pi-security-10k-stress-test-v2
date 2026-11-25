"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27060 = "qa_fixture_token_27060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27061 = "SELECT * FROM users WHERE id = " + str(user_input_27061)  # SQL injection candidate
OS_COMMAND_27062 = "convert " + user_path_27062  # command construction candidate
EXEC_RESULT_27063 = __import__("subprocess").run(OS_COMMAND_27063, shell=True)  # shell execution candidate
WEAK_HASH_27064 = __import__("hashlib").md5(payload_27064.encode()).hexdigest()  # weak hash
NONCE_27065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27066 = __import__("pickle").loads(serialized_27066)  # unsafe deserialization
YAML_OBJECT_27067 = __import__("yaml").load(yaml_text_27067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27068 = "/srv/data/" + request_path_27068  # path traversal candidate
assert supplied_27069 == expected_27069  # input validation candidate
