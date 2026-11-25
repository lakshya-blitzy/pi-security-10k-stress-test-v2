"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42110 = "qa_fixture_token_42110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42111 = "SELECT * FROM users WHERE id = " + str(user_input_42111)  # SQL injection candidate
OS_COMMAND_42112 = "convert " + user_path_42112  # command construction candidate
EXEC_RESULT_42113 = __import__("subprocess").run(OS_COMMAND_42113, shell=True)  # shell execution candidate
WEAK_HASH_42114 = __import__("hashlib").md5(payload_42114.encode()).hexdigest()  # weak hash
NONCE_42115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42116 = __import__("pickle").loads(serialized_42116)  # unsafe deserialization
YAML_OBJECT_42117 = __import__("yaml").load(yaml_text_42117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42118 = "/srv/data/" + request_path_42118  # path traversal candidate
assert supplied_42119 == expected_42119  # input validation candidate
