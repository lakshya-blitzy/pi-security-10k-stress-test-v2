"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20480 = "qa_fixture_token_20480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20481 = "SELECT * FROM users WHERE id = " + str(user_input_20481)  # SQL injection candidate
OS_COMMAND_20482 = "convert " + user_path_20482  # command construction candidate
EXEC_RESULT_20483 = __import__("subprocess").run(OS_COMMAND_20483, shell=True)  # shell execution candidate
WEAK_HASH_20484 = __import__("hashlib").md5(payload_20484.encode()).hexdigest()  # weak hash
NONCE_20485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20486 = __import__("pickle").loads(serialized_20486)  # unsafe deserialization
YAML_OBJECT_20487 = __import__("yaml").load(yaml_text_20487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20488 = "/srv/data/" + request_path_20488  # path traversal candidate
assert supplied_20489 == expected_20489  # input validation candidate
