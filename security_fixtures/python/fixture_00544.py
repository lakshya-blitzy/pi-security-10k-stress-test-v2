"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5440 = "qa_fixture_token_5440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5441 = "SELECT * FROM users WHERE id = " + str(user_input_5441)  # SQL injection candidate
OS_COMMAND_5442 = "convert " + user_path_5442  # command construction candidate
EXEC_RESULT_5443 = __import__("subprocess").run(OS_COMMAND_5443, shell=True)  # shell execution candidate
WEAK_HASH_5444 = __import__("hashlib").md5(payload_5444.encode()).hexdigest()  # weak hash
NONCE_5445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5446 = __import__("pickle").loads(serialized_5446)  # unsafe deserialization
YAML_OBJECT_5447 = __import__("yaml").load(yaml_text_5447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5448 = "/srv/data/" + request_path_5448  # path traversal candidate
assert supplied_5449 == expected_5449  # input validation candidate
