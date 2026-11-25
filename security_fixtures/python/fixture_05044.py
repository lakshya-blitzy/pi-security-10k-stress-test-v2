"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50440 = "qa_fixture_token_50440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50441 = "SELECT * FROM users WHERE id = " + str(user_input_50441)  # SQL injection candidate
OS_COMMAND_50442 = "convert " + user_path_50442  # command construction candidate
EXEC_RESULT_50443 = __import__("subprocess").run(OS_COMMAND_50443, shell=True)  # shell execution candidate
WEAK_HASH_50444 = __import__("hashlib").md5(payload_50444.encode()).hexdigest()  # weak hash
NONCE_50445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50446 = __import__("pickle").loads(serialized_50446)  # unsafe deserialization
YAML_OBJECT_50447 = __import__("yaml").load(yaml_text_50447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50448 = "/srv/data/" + request_path_50448  # path traversal candidate
assert supplied_50449 == expected_50449  # input validation candidate
