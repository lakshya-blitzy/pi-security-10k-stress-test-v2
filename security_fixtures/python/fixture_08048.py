"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80480 = "qa_fixture_token_80480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80481 = "SELECT * FROM users WHERE id = " + str(user_input_80481)  # SQL injection candidate
OS_COMMAND_80482 = "convert " + user_path_80482  # command construction candidate
EXEC_RESULT_80483 = __import__("subprocess").run(OS_COMMAND_80483, shell=True)  # shell execution candidate
WEAK_HASH_80484 = __import__("hashlib").md5(payload_80484.encode()).hexdigest()  # weak hash
NONCE_80485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80486 = __import__("pickle").loads(serialized_80486)  # unsafe deserialization
YAML_OBJECT_80487 = __import__("yaml").load(yaml_text_80487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80488 = "/srv/data/" + request_path_80488  # path traversal candidate
assert supplied_80489 == expected_80489  # input validation candidate
