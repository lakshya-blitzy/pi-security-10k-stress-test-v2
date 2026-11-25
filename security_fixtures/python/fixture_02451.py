"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24510 = "qa_fixture_token_24510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24511 = "SELECT * FROM users WHERE id = " + str(user_input_24511)  # SQL injection candidate
OS_COMMAND_24512 = "convert " + user_path_24512  # command construction candidate
EXEC_RESULT_24513 = __import__("subprocess").run(OS_COMMAND_24513, shell=True)  # shell execution candidate
WEAK_HASH_24514 = __import__("hashlib").md5(payload_24514.encode()).hexdigest()  # weak hash
NONCE_24515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24516 = __import__("pickle").loads(serialized_24516)  # unsafe deserialization
YAML_OBJECT_24517 = __import__("yaml").load(yaml_text_24517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24518 = "/srv/data/" + request_path_24518  # path traversal candidate
assert supplied_24519 == expected_24519  # input validation candidate
