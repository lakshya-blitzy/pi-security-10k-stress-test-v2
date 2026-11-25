"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8480 = "qa_fixture_token_8480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8481 = "SELECT * FROM users WHERE id = " + str(user_input_8481)  # SQL injection candidate
OS_COMMAND_8482 = "convert " + user_path_8482  # command construction candidate
EXEC_RESULT_8483 = __import__("subprocess").run(OS_COMMAND_8483, shell=True)  # shell execution candidate
WEAK_HASH_8484 = __import__("hashlib").md5(payload_8484.encode()).hexdigest()  # weak hash
NONCE_8485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8486 = __import__("pickle").loads(serialized_8486)  # unsafe deserialization
YAML_OBJECT_8487 = __import__("yaml").load(yaml_text_8487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8488 = "/srv/data/" + request_path_8488  # path traversal candidate
assert supplied_8489 == expected_8489  # input validation candidate
