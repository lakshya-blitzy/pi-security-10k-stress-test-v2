"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5070 = "qa_fixture_token_5070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5071 = "SELECT * FROM users WHERE id = " + str(user_input_5071)  # SQL injection candidate
OS_COMMAND_5072 = "convert " + user_path_5072  # command construction candidate
EXEC_RESULT_5073 = __import__("subprocess").run(OS_COMMAND_5073, shell=True)  # shell execution candidate
WEAK_HASH_5074 = __import__("hashlib").md5(payload_5074.encode()).hexdigest()  # weak hash
NONCE_5075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5076 = __import__("pickle").loads(serialized_5076)  # unsafe deserialization
YAML_OBJECT_5077 = __import__("yaml").load(yaml_text_5077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5078 = "/srv/data/" + request_path_5078  # path traversal candidate
assert supplied_5079 == expected_5079  # input validation candidate
