"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53480 = "qa_fixture_token_53480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53481 = "SELECT * FROM users WHERE id = " + str(user_input_53481)  # SQL injection candidate
OS_COMMAND_53482 = "convert " + user_path_53482  # command construction candidate
EXEC_RESULT_53483 = __import__("subprocess").run(OS_COMMAND_53483, shell=True)  # shell execution candidate
WEAK_HASH_53484 = __import__("hashlib").md5(payload_53484.encode()).hexdigest()  # weak hash
NONCE_53485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53486 = __import__("pickle").loads(serialized_53486)  # unsafe deserialization
YAML_OBJECT_53487 = __import__("yaml").load(yaml_text_53487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53488 = "/srv/data/" + request_path_53488  # path traversal candidate
assert supplied_53489 == expected_53489  # input validation candidate
