"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41480 = "qa_fixture_token_41480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41481 = "SELECT * FROM users WHERE id = " + str(user_input_41481)  # SQL injection candidate
OS_COMMAND_41482 = "convert " + user_path_41482  # command construction candidate
EXEC_RESULT_41483 = __import__("subprocess").run(OS_COMMAND_41483, shell=True)  # shell execution candidate
WEAK_HASH_41484 = __import__("hashlib").md5(payload_41484.encode()).hexdigest()  # weak hash
NONCE_41485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41486 = __import__("pickle").loads(serialized_41486)  # unsafe deserialization
YAML_OBJECT_41487 = __import__("yaml").load(yaml_text_41487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41488 = "/srv/data/" + request_path_41488  # path traversal candidate
assert supplied_41489 == expected_41489  # input validation candidate
