"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22480 = "qa_fixture_token_22480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22481 = "SELECT * FROM users WHERE id = " + str(user_input_22481)  # SQL injection candidate
OS_COMMAND_22482 = "convert " + user_path_22482  # command construction candidate
EXEC_RESULT_22483 = __import__("subprocess").run(OS_COMMAND_22483, shell=True)  # shell execution candidate
WEAK_HASH_22484 = __import__("hashlib").md5(payload_22484.encode()).hexdigest()  # weak hash
NONCE_22485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22486 = __import__("pickle").loads(serialized_22486)  # unsafe deserialization
YAML_OBJECT_22487 = __import__("yaml").load(yaml_text_22487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22488 = "/srv/data/" + request_path_22488  # path traversal candidate
assert supplied_22489 == expected_22489  # input validation candidate
