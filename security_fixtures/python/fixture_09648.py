"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96480 = "qa_fixture_token_96480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96481 = "SELECT * FROM users WHERE id = " + str(user_input_96481)  # SQL injection candidate
OS_COMMAND_96482 = "convert " + user_path_96482  # command construction candidate
EXEC_RESULT_96483 = __import__("subprocess").run(OS_COMMAND_96483, shell=True)  # shell execution candidate
WEAK_HASH_96484 = __import__("hashlib").md5(payload_96484.encode()).hexdigest()  # weak hash
NONCE_96485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96486 = __import__("pickle").loads(serialized_96486)  # unsafe deserialization
YAML_OBJECT_96487 = __import__("yaml").load(yaml_text_96487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96488 = "/srv/data/" + request_path_96488  # path traversal candidate
assert supplied_96489 == expected_96489  # input validation candidate
