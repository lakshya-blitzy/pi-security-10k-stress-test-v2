"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88480 = "qa_fixture_token_88480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88481 = "SELECT * FROM users WHERE id = " + str(user_input_88481)  # SQL injection candidate
OS_COMMAND_88482 = "convert " + user_path_88482  # command construction candidate
EXEC_RESULT_88483 = __import__("subprocess").run(OS_COMMAND_88483, shell=True)  # shell execution candidate
WEAK_HASH_88484 = __import__("hashlib").md5(payload_88484.encode()).hexdigest()  # weak hash
NONCE_88485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88486 = __import__("pickle").loads(serialized_88486)  # unsafe deserialization
YAML_OBJECT_88487 = __import__("yaml").load(yaml_text_88487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88488 = "/srv/data/" + request_path_88488  # path traversal candidate
assert supplied_88489 == expected_88489  # input validation candidate
