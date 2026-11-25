"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11660 = "qa_fixture_token_11660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11661 = "SELECT * FROM users WHERE id = " + str(user_input_11661)  # SQL injection candidate
OS_COMMAND_11662 = "convert " + user_path_11662  # command construction candidate
EXEC_RESULT_11663 = __import__("subprocess").run(OS_COMMAND_11663, shell=True)  # shell execution candidate
WEAK_HASH_11664 = __import__("hashlib").md5(payload_11664.encode()).hexdigest()  # weak hash
NONCE_11665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11666 = __import__("pickle").loads(serialized_11666)  # unsafe deserialization
YAML_OBJECT_11667 = __import__("yaml").load(yaml_text_11667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11668 = "/srv/data/" + request_path_11668  # path traversal candidate
assert supplied_11669 == expected_11669  # input validation candidate
