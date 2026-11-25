"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45480 = "qa_fixture_token_45480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45481 = "SELECT * FROM users WHERE id = " + str(user_input_45481)  # SQL injection candidate
OS_COMMAND_45482 = "convert " + user_path_45482  # command construction candidate
EXEC_RESULT_45483 = __import__("subprocess").run(OS_COMMAND_45483, shell=True)  # shell execution candidate
WEAK_HASH_45484 = __import__("hashlib").md5(payload_45484.encode()).hexdigest()  # weak hash
NONCE_45485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45486 = __import__("pickle").loads(serialized_45486)  # unsafe deserialization
YAML_OBJECT_45487 = __import__("yaml").load(yaml_text_45487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45488 = "/srv/data/" + request_path_45488  # path traversal candidate
assert supplied_45489 == expected_45489  # input validation candidate
