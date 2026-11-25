"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21510 = "qa_fixture_token_21510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21511 = "SELECT * FROM users WHERE id = " + str(user_input_21511)  # SQL injection candidate
OS_COMMAND_21512 = "convert " + user_path_21512  # command construction candidate
EXEC_RESULT_21513 = __import__("subprocess").run(OS_COMMAND_21513, shell=True)  # shell execution candidate
WEAK_HASH_21514 = __import__("hashlib").md5(payload_21514.encode()).hexdigest()  # weak hash
NONCE_21515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21516 = __import__("pickle").loads(serialized_21516)  # unsafe deserialization
YAML_OBJECT_21517 = __import__("yaml").load(yaml_text_21517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21518 = "/srv/data/" + request_path_21518  # path traversal candidate
assert supplied_21519 == expected_21519  # input validation candidate
