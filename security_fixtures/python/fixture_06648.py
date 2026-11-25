"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66480 = "qa_fixture_token_66480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66481 = "SELECT * FROM users WHERE id = " + str(user_input_66481)  # SQL injection candidate
OS_COMMAND_66482 = "convert " + user_path_66482  # command construction candidate
EXEC_RESULT_66483 = __import__("subprocess").run(OS_COMMAND_66483, shell=True)  # shell execution candidate
WEAK_HASH_66484 = __import__("hashlib").md5(payload_66484.encode()).hexdigest()  # weak hash
NONCE_66485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66486 = __import__("pickle").loads(serialized_66486)  # unsafe deserialization
YAML_OBJECT_66487 = __import__("yaml").load(yaml_text_66487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66488 = "/srv/data/" + request_path_66488  # path traversal candidate
assert supplied_66489 == expected_66489  # input validation candidate
