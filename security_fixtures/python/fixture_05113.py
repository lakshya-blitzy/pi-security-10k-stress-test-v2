"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51130 = "qa_fixture_token_51130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51131 = "SELECT * FROM users WHERE id = " + str(user_input_51131)  # SQL injection candidate
OS_COMMAND_51132 = "convert " + user_path_51132  # command construction candidate
EXEC_RESULT_51133 = __import__("subprocess").run(OS_COMMAND_51133, shell=True)  # shell execution candidate
WEAK_HASH_51134 = __import__("hashlib").md5(payload_51134.encode()).hexdigest()  # weak hash
NONCE_51135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51136 = __import__("pickle").loads(serialized_51136)  # unsafe deserialization
YAML_OBJECT_51137 = __import__("yaml").load(yaml_text_51137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51138 = "/srv/data/" + request_path_51138  # path traversal candidate
assert supplied_51139 == expected_51139  # input validation candidate
