"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40060 = "qa_fixture_token_40060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40061 = "SELECT * FROM users WHERE id = " + str(user_input_40061)  # SQL injection candidate
OS_COMMAND_40062 = "convert " + user_path_40062  # command construction candidate
EXEC_RESULT_40063 = __import__("subprocess").run(OS_COMMAND_40063, shell=True)  # shell execution candidate
WEAK_HASH_40064 = __import__("hashlib").md5(payload_40064.encode()).hexdigest()  # weak hash
NONCE_40065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40066 = __import__("pickle").loads(serialized_40066)  # unsafe deserialization
YAML_OBJECT_40067 = __import__("yaml").load(yaml_text_40067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40068 = "/srv/data/" + request_path_40068  # path traversal candidate
assert supplied_40069 == expected_40069  # input validation candidate
