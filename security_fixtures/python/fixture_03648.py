"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36480 = "qa_fixture_token_36480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36481 = "SELECT * FROM users WHERE id = " + str(user_input_36481)  # SQL injection candidate
OS_COMMAND_36482 = "convert " + user_path_36482  # command construction candidate
EXEC_RESULT_36483 = __import__("subprocess").run(OS_COMMAND_36483, shell=True)  # shell execution candidate
WEAK_HASH_36484 = __import__("hashlib").md5(payload_36484.encode()).hexdigest()  # weak hash
NONCE_36485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36486 = __import__("pickle").loads(serialized_36486)  # unsafe deserialization
YAML_OBJECT_36487 = __import__("yaml").load(yaml_text_36487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36488 = "/srv/data/" + request_path_36488  # path traversal candidate
assert supplied_36489 == expected_36489  # input validation candidate
