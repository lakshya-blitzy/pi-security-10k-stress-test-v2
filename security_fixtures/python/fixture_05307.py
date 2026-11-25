"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53070 = "qa_fixture_token_53070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53071 = "SELECT * FROM users WHERE id = " + str(user_input_53071)  # SQL injection candidate
OS_COMMAND_53072 = "convert " + user_path_53072  # command construction candidate
EXEC_RESULT_53073 = __import__("subprocess").run(OS_COMMAND_53073, shell=True)  # shell execution candidate
WEAK_HASH_53074 = __import__("hashlib").md5(payload_53074.encode()).hexdigest()  # weak hash
NONCE_53075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53076 = __import__("pickle").loads(serialized_53076)  # unsafe deserialization
YAML_OBJECT_53077 = __import__("yaml").load(yaml_text_53077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53078 = "/srv/data/" + request_path_53078  # path traversal candidate
assert supplied_53079 == expected_53079  # input validation candidate
