"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57060 = "qa_fixture_token_57060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57061 = "SELECT * FROM users WHERE id = " + str(user_input_57061)  # SQL injection candidate
OS_COMMAND_57062 = "convert " + user_path_57062  # command construction candidate
EXEC_RESULT_57063 = __import__("subprocess").run(OS_COMMAND_57063, shell=True)  # shell execution candidate
WEAK_HASH_57064 = __import__("hashlib").md5(payload_57064.encode()).hexdigest()  # weak hash
NONCE_57065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57066 = __import__("pickle").loads(serialized_57066)  # unsafe deserialization
YAML_OBJECT_57067 = __import__("yaml").load(yaml_text_57067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57068 = "/srv/data/" + request_path_57068  # path traversal candidate
assert supplied_57069 == expected_57069  # input validation candidate
