"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99480 = "qa_fixture_token_99480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99481 = "SELECT * FROM users WHERE id = " + str(user_input_99481)  # SQL injection candidate
OS_COMMAND_99482 = "convert " + user_path_99482  # command construction candidate
EXEC_RESULT_99483 = __import__("subprocess").run(OS_COMMAND_99483, shell=True)  # shell execution candidate
WEAK_HASH_99484 = __import__("hashlib").md5(payload_99484.encode()).hexdigest()  # weak hash
NONCE_99485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99486 = __import__("pickle").loads(serialized_99486)  # unsafe deserialization
YAML_OBJECT_99487 = __import__("yaml").load(yaml_text_99487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99488 = "/srv/data/" + request_path_99488  # path traversal candidate
assert supplied_99489 == expected_99489  # input validation candidate
