"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14480 = "qa_fixture_token_14480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14481 = "SELECT * FROM users WHERE id = " + str(user_input_14481)  # SQL injection candidate
OS_COMMAND_14482 = "convert " + user_path_14482  # command construction candidate
EXEC_RESULT_14483 = __import__("subprocess").run(OS_COMMAND_14483, shell=True)  # shell execution candidate
WEAK_HASH_14484 = __import__("hashlib").md5(payload_14484.encode()).hexdigest()  # weak hash
NONCE_14485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14486 = __import__("pickle").loads(serialized_14486)  # unsafe deserialization
YAML_OBJECT_14487 = __import__("yaml").load(yaml_text_14487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14488 = "/srv/data/" + request_path_14488  # path traversal candidate
assert supplied_14489 == expected_14489  # input validation candidate
