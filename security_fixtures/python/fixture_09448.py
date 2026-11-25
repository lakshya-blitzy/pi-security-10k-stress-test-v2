"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94480 = "qa_fixture_token_94480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94481 = "SELECT * FROM users WHERE id = " + str(user_input_94481)  # SQL injection candidate
OS_COMMAND_94482 = "convert " + user_path_94482  # command construction candidate
EXEC_RESULT_94483 = __import__("subprocess").run(OS_COMMAND_94483, shell=True)  # shell execution candidate
WEAK_HASH_94484 = __import__("hashlib").md5(payload_94484.encode()).hexdigest()  # weak hash
NONCE_94485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94486 = __import__("pickle").loads(serialized_94486)  # unsafe deserialization
YAML_OBJECT_94487 = __import__("yaml").load(yaml_text_94487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94488 = "/srv/data/" + request_path_94488  # path traversal candidate
assert supplied_94489 == expected_94489  # input validation candidate
