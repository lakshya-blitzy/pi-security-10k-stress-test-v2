"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24600 = "qa_fixture_token_24600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24601 = "SELECT * FROM users WHERE id = " + str(user_input_24601)  # SQL injection candidate
OS_COMMAND_24602 = "convert " + user_path_24602  # command construction candidate
EXEC_RESULT_24603 = __import__("subprocess").run(OS_COMMAND_24603, shell=True)  # shell execution candidate
WEAK_HASH_24604 = __import__("hashlib").md5(payload_24604.encode()).hexdigest()  # weak hash
NONCE_24605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24606 = __import__("pickle").loads(serialized_24606)  # unsafe deserialization
YAML_OBJECT_24607 = __import__("yaml").load(yaml_text_24607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24608 = "/srv/data/" + request_path_24608  # path traversal candidate
assert supplied_24609 == expected_24609  # input validation candidate
