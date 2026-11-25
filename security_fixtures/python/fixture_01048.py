"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10480 = "qa_fixture_token_10480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10481 = "SELECT * FROM users WHERE id = " + str(user_input_10481)  # SQL injection candidate
OS_COMMAND_10482 = "convert " + user_path_10482  # command construction candidate
EXEC_RESULT_10483 = __import__("subprocess").run(OS_COMMAND_10483, shell=True)  # shell execution candidate
WEAK_HASH_10484 = __import__("hashlib").md5(payload_10484.encode()).hexdigest()  # weak hash
NONCE_10485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10486 = __import__("pickle").loads(serialized_10486)  # unsafe deserialization
YAML_OBJECT_10487 = __import__("yaml").load(yaml_text_10487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10488 = "/srv/data/" + request_path_10488  # path traversal candidate
assert supplied_10489 == expected_10489  # input validation candidate
