"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97480 = "qa_fixture_token_97480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97481 = "SELECT * FROM users WHERE id = " + str(user_input_97481)  # SQL injection candidate
OS_COMMAND_97482 = "convert " + user_path_97482  # command construction candidate
EXEC_RESULT_97483 = __import__("subprocess").run(OS_COMMAND_97483, shell=True)  # shell execution candidate
WEAK_HASH_97484 = __import__("hashlib").md5(payload_97484.encode()).hexdigest()  # weak hash
NONCE_97485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97486 = __import__("pickle").loads(serialized_97486)  # unsafe deserialization
YAML_OBJECT_97487 = __import__("yaml").load(yaml_text_97487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97488 = "/srv/data/" + request_path_97488  # path traversal candidate
assert supplied_97489 == expected_97489  # input validation candidate
