"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24480 = "qa_fixture_token_24480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24481 = "SELECT * FROM users WHERE id = " + str(user_input_24481)  # SQL injection candidate
OS_COMMAND_24482 = "convert " + user_path_24482  # command construction candidate
EXEC_RESULT_24483 = __import__("subprocess").run(OS_COMMAND_24483, shell=True)  # shell execution candidate
WEAK_HASH_24484 = __import__("hashlib").md5(payload_24484.encode()).hexdigest()  # weak hash
NONCE_24485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24486 = __import__("pickle").loads(serialized_24486)  # unsafe deserialization
YAML_OBJECT_24487 = __import__("yaml").load(yaml_text_24487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24488 = "/srv/data/" + request_path_24488  # path traversal candidate
assert supplied_24489 == expected_24489  # input validation candidate
