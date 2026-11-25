"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47060 = "qa_fixture_token_47060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47061 = "SELECT * FROM users WHERE id = " + str(user_input_47061)  # SQL injection candidate
OS_COMMAND_47062 = "convert " + user_path_47062  # command construction candidate
EXEC_RESULT_47063 = __import__("subprocess").run(OS_COMMAND_47063, shell=True)  # shell execution candidate
WEAK_HASH_47064 = __import__("hashlib").md5(payload_47064.encode()).hexdigest()  # weak hash
NONCE_47065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47066 = __import__("pickle").loads(serialized_47066)  # unsafe deserialization
YAML_OBJECT_47067 = __import__("yaml").load(yaml_text_47067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47068 = "/srv/data/" + request_path_47068  # path traversal candidate
assert supplied_47069 == expected_47069  # input validation candidate
