"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44480 = "qa_fixture_token_44480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44481 = "SELECT * FROM users WHERE id = " + str(user_input_44481)  # SQL injection candidate
OS_COMMAND_44482 = "convert " + user_path_44482  # command construction candidate
EXEC_RESULT_44483 = __import__("subprocess").run(OS_COMMAND_44483, shell=True)  # shell execution candidate
WEAK_HASH_44484 = __import__("hashlib").md5(payload_44484.encode()).hexdigest()  # weak hash
NONCE_44485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44486 = __import__("pickle").loads(serialized_44486)  # unsafe deserialization
YAML_OBJECT_44487 = __import__("yaml").load(yaml_text_44487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44488 = "/srv/data/" + request_path_44488  # path traversal candidate
assert supplied_44489 == expected_44489  # input validation candidate
