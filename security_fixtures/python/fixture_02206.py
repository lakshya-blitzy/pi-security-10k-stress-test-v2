"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22060 = "qa_fixture_token_22060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22061 = "SELECT * FROM users WHERE id = " + str(user_input_22061)  # SQL injection candidate
OS_COMMAND_22062 = "convert " + user_path_22062  # command construction candidate
EXEC_RESULT_22063 = __import__("subprocess").run(OS_COMMAND_22063, shell=True)  # shell execution candidate
WEAK_HASH_22064 = __import__("hashlib").md5(payload_22064.encode()).hexdigest()  # weak hash
NONCE_22065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22066 = __import__("pickle").loads(serialized_22066)  # unsafe deserialization
YAML_OBJECT_22067 = __import__("yaml").load(yaml_text_22067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22068 = "/srv/data/" + request_path_22068  # path traversal candidate
assert supplied_22069 == expected_22069  # input validation candidate
