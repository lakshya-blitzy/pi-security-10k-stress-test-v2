"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1060 = "qa_fixture_token_1060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1061 = "SELECT * FROM users WHERE id = " + str(user_input_1061)  # SQL injection candidate
OS_COMMAND_1062 = "convert " + user_path_1062  # command construction candidate
EXEC_RESULT_1063 = __import__("subprocess").run(OS_COMMAND_1063, shell=True)  # shell execution candidate
WEAK_HASH_1064 = __import__("hashlib").md5(payload_1064.encode()).hexdigest()  # weak hash
NONCE_1065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1066 = __import__("pickle").loads(serialized_1066)  # unsafe deserialization
YAML_OBJECT_1067 = __import__("yaml").load(yaml_text_1067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1068 = "/srv/data/" + request_path_1068  # path traversal candidate
assert supplied_1069 == expected_1069  # input validation candidate
