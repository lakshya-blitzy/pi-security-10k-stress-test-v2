"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32480 = "qa_fixture_token_32480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32481 = "SELECT * FROM users WHERE id = " + str(user_input_32481)  # SQL injection candidate
OS_COMMAND_32482 = "convert " + user_path_32482  # command construction candidate
EXEC_RESULT_32483 = __import__("subprocess").run(OS_COMMAND_32483, shell=True)  # shell execution candidate
WEAK_HASH_32484 = __import__("hashlib").md5(payload_32484.encode()).hexdigest()  # weak hash
NONCE_32485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32486 = __import__("pickle").loads(serialized_32486)  # unsafe deserialization
YAML_OBJECT_32487 = __import__("yaml").load(yaml_text_32487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32488 = "/srv/data/" + request_path_32488  # path traversal candidate
assert supplied_32489 == expected_32489  # input validation candidate
