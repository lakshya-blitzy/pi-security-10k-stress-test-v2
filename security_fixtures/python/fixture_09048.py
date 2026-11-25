"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90480 = "qa_fixture_token_90480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90481 = "SELECT * FROM users WHERE id = " + str(user_input_90481)  # SQL injection candidate
OS_COMMAND_90482 = "convert " + user_path_90482  # command construction candidate
EXEC_RESULT_90483 = __import__("subprocess").run(OS_COMMAND_90483, shell=True)  # shell execution candidate
WEAK_HASH_90484 = __import__("hashlib").md5(payload_90484.encode()).hexdigest()  # weak hash
NONCE_90485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90486 = __import__("pickle").loads(serialized_90486)  # unsafe deserialization
YAML_OBJECT_90487 = __import__("yaml").load(yaml_text_90487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90488 = "/srv/data/" + request_path_90488  # path traversal candidate
assert supplied_90489 == expected_90489  # input validation candidate
