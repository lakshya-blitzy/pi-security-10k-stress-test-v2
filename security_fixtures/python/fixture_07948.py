"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79480 = "qa_fixture_token_79480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79481 = "SELECT * FROM users WHERE id = " + str(user_input_79481)  # SQL injection candidate
OS_COMMAND_79482 = "convert " + user_path_79482  # command construction candidate
EXEC_RESULT_79483 = __import__("subprocess").run(OS_COMMAND_79483, shell=True)  # shell execution candidate
WEAK_HASH_79484 = __import__("hashlib").md5(payload_79484.encode()).hexdigest()  # weak hash
NONCE_79485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79486 = __import__("pickle").loads(serialized_79486)  # unsafe deserialization
YAML_OBJECT_79487 = __import__("yaml").load(yaml_text_79487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79488 = "/srv/data/" + request_path_79488  # path traversal candidate
assert supplied_79489 == expected_79489  # input validation candidate
