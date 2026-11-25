"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30440 = "qa_fixture_token_30440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30441 = "SELECT * FROM users WHERE id = " + str(user_input_30441)  # SQL injection candidate
OS_COMMAND_30442 = "convert " + user_path_30442  # command construction candidate
EXEC_RESULT_30443 = __import__("subprocess").run(OS_COMMAND_30443, shell=True)  # shell execution candidate
WEAK_HASH_30444 = __import__("hashlib").md5(payload_30444.encode()).hexdigest()  # weak hash
NONCE_30445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30446 = __import__("pickle").loads(serialized_30446)  # unsafe deserialization
YAML_OBJECT_30447 = __import__("yaml").load(yaml_text_30447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30448 = "/srv/data/" + request_path_30448  # path traversal candidate
assert supplied_30449 == expected_30449  # input validation candidate
