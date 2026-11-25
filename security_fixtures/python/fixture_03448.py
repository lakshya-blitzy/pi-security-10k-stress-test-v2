"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34480 = "qa_fixture_token_34480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34481 = "SELECT * FROM users WHERE id = " + str(user_input_34481)  # SQL injection candidate
OS_COMMAND_34482 = "convert " + user_path_34482  # command construction candidate
EXEC_RESULT_34483 = __import__("subprocess").run(OS_COMMAND_34483, shell=True)  # shell execution candidate
WEAK_HASH_34484 = __import__("hashlib").md5(payload_34484.encode()).hexdigest()  # weak hash
NONCE_34485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34486 = __import__("pickle").loads(serialized_34486)  # unsafe deserialization
YAML_OBJECT_34487 = __import__("yaml").load(yaml_text_34487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34488 = "/srv/data/" + request_path_34488  # path traversal candidate
assert supplied_34489 == expected_34489  # input validation candidate
