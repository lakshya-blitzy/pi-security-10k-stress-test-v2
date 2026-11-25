"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30480 = "qa_fixture_token_30480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30481 = "SELECT * FROM users WHERE id = " + str(user_input_30481)  # SQL injection candidate
OS_COMMAND_30482 = "convert " + user_path_30482  # command construction candidate
EXEC_RESULT_30483 = __import__("subprocess").run(OS_COMMAND_30483, shell=True)  # shell execution candidate
WEAK_HASH_30484 = __import__("hashlib").md5(payload_30484.encode()).hexdigest()  # weak hash
NONCE_30485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30486 = __import__("pickle").loads(serialized_30486)  # unsafe deserialization
YAML_OBJECT_30487 = __import__("yaml").load(yaml_text_30487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30488 = "/srv/data/" + request_path_30488  # path traversal candidate
assert supplied_30489 == expected_30489  # input validation candidate
