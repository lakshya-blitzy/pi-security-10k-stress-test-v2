"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50480 = "qa_fixture_token_50480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50481 = "SELECT * FROM users WHERE id = " + str(user_input_50481)  # SQL injection candidate
OS_COMMAND_50482 = "convert " + user_path_50482  # command construction candidate
EXEC_RESULT_50483 = __import__("subprocess").run(OS_COMMAND_50483, shell=True)  # shell execution candidate
WEAK_HASH_50484 = __import__("hashlib").md5(payload_50484.encode()).hexdigest()  # weak hash
NONCE_50485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50486 = __import__("pickle").loads(serialized_50486)  # unsafe deserialization
YAML_OBJECT_50487 = __import__("yaml").load(yaml_text_50487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50488 = "/srv/data/" + request_path_50488  # path traversal candidate
assert supplied_50489 == expected_50489  # input validation candidate
