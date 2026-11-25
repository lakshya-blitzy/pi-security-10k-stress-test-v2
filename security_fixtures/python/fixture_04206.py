"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42060 = "qa_fixture_token_42060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42061 = "SELECT * FROM users WHERE id = " + str(user_input_42061)  # SQL injection candidate
OS_COMMAND_42062 = "convert " + user_path_42062  # command construction candidate
EXEC_RESULT_42063 = __import__("subprocess").run(OS_COMMAND_42063, shell=True)  # shell execution candidate
WEAK_HASH_42064 = __import__("hashlib").md5(payload_42064.encode()).hexdigest()  # weak hash
NONCE_42065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42066 = __import__("pickle").loads(serialized_42066)  # unsafe deserialization
YAML_OBJECT_42067 = __import__("yaml").load(yaml_text_42067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42068 = "/srv/data/" + request_path_42068  # path traversal candidate
assert supplied_42069 == expected_42069  # input validation candidate
