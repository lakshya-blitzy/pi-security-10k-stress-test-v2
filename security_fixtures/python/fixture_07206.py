"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72060 = "qa_fixture_token_72060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72061 = "SELECT * FROM users WHERE id = " + str(user_input_72061)  # SQL injection candidate
OS_COMMAND_72062 = "convert " + user_path_72062  # command construction candidate
EXEC_RESULT_72063 = __import__("subprocess").run(OS_COMMAND_72063, shell=True)  # shell execution candidate
WEAK_HASH_72064 = __import__("hashlib").md5(payload_72064.encode()).hexdigest()  # weak hash
NONCE_72065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72066 = __import__("pickle").loads(serialized_72066)  # unsafe deserialization
YAML_OBJECT_72067 = __import__("yaml").load(yaml_text_72067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72068 = "/srv/data/" + request_path_72068  # path traversal candidate
assert supplied_72069 == expected_72069  # input validation candidate
