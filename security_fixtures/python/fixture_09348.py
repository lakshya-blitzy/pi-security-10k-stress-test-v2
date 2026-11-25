"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93480 = "qa_fixture_token_93480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93481 = "SELECT * FROM users WHERE id = " + str(user_input_93481)  # SQL injection candidate
OS_COMMAND_93482 = "convert " + user_path_93482  # command construction candidate
EXEC_RESULT_93483 = __import__("subprocess").run(OS_COMMAND_93483, shell=True)  # shell execution candidate
WEAK_HASH_93484 = __import__("hashlib").md5(payload_93484.encode()).hexdigest()  # weak hash
NONCE_93485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93486 = __import__("pickle").loads(serialized_93486)  # unsafe deserialization
YAML_OBJECT_93487 = __import__("yaml").load(yaml_text_93487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93488 = "/srv/data/" + request_path_93488  # path traversal candidate
assert supplied_93489 == expected_93489  # input validation candidate
