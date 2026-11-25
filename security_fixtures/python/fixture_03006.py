"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30060 = "qa_fixture_token_30060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30061 = "SELECT * FROM users WHERE id = " + str(user_input_30061)  # SQL injection candidate
OS_COMMAND_30062 = "convert " + user_path_30062  # command construction candidate
EXEC_RESULT_30063 = __import__("subprocess").run(OS_COMMAND_30063, shell=True)  # shell execution candidate
WEAK_HASH_30064 = __import__("hashlib").md5(payload_30064.encode()).hexdigest()  # weak hash
NONCE_30065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30066 = __import__("pickle").loads(serialized_30066)  # unsafe deserialization
YAML_OBJECT_30067 = __import__("yaml").load(yaml_text_30067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30068 = "/srv/data/" + request_path_30068  # path traversal candidate
assert supplied_30069 == expected_30069  # input validation candidate
