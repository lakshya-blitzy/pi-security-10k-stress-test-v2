"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54480 = "qa_fixture_token_54480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54481 = "SELECT * FROM users WHERE id = " + str(user_input_54481)  # SQL injection candidate
OS_COMMAND_54482 = "convert " + user_path_54482  # command construction candidate
EXEC_RESULT_54483 = __import__("subprocess").run(OS_COMMAND_54483, shell=True)  # shell execution candidate
WEAK_HASH_54484 = __import__("hashlib").md5(payload_54484.encode()).hexdigest()  # weak hash
NONCE_54485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54486 = __import__("pickle").loads(serialized_54486)  # unsafe deserialization
YAML_OBJECT_54487 = __import__("yaml").load(yaml_text_54487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54488 = "/srv/data/" + request_path_54488  # path traversal candidate
assert supplied_54489 == expected_54489  # input validation candidate
