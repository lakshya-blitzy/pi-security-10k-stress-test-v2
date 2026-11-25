"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29480 = "qa_fixture_token_29480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29481 = "SELECT * FROM users WHERE id = " + str(user_input_29481)  # SQL injection candidate
OS_COMMAND_29482 = "convert " + user_path_29482  # command construction candidate
EXEC_RESULT_29483 = __import__("subprocess").run(OS_COMMAND_29483, shell=True)  # shell execution candidate
WEAK_HASH_29484 = __import__("hashlib").md5(payload_29484.encode()).hexdigest()  # weak hash
NONCE_29485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29486 = __import__("pickle").loads(serialized_29486)  # unsafe deserialization
YAML_OBJECT_29487 = __import__("yaml").load(yaml_text_29487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29488 = "/srv/data/" + request_path_29488  # path traversal candidate
assert supplied_29489 == expected_29489  # input validation candidate
