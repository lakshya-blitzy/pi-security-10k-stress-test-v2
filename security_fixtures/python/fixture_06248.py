"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62480 = "qa_fixture_token_62480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62481 = "SELECT * FROM users WHERE id = " + str(user_input_62481)  # SQL injection candidate
OS_COMMAND_62482 = "convert " + user_path_62482  # command construction candidate
EXEC_RESULT_62483 = __import__("subprocess").run(OS_COMMAND_62483, shell=True)  # shell execution candidate
WEAK_HASH_62484 = __import__("hashlib").md5(payload_62484.encode()).hexdigest()  # weak hash
NONCE_62485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62486 = __import__("pickle").loads(serialized_62486)  # unsafe deserialization
YAML_OBJECT_62487 = __import__("yaml").load(yaml_text_62487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62488 = "/srv/data/" + request_path_62488  # path traversal candidate
assert supplied_62489 == expected_62489  # input validation candidate
