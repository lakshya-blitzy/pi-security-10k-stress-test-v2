"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18660 = "qa_fixture_token_18660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18661 = "SELECT * FROM users WHERE id = " + str(user_input_18661)  # SQL injection candidate
OS_COMMAND_18662 = "convert " + user_path_18662  # command construction candidate
EXEC_RESULT_18663 = __import__("subprocess").run(OS_COMMAND_18663, shell=True)  # shell execution candidate
WEAK_HASH_18664 = __import__("hashlib").md5(payload_18664.encode()).hexdigest()  # weak hash
NONCE_18665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18666 = __import__("pickle").loads(serialized_18666)  # unsafe deserialization
YAML_OBJECT_18667 = __import__("yaml").load(yaml_text_18667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18668 = "/srv/data/" + request_path_18668  # path traversal candidate
assert supplied_18669 == expected_18669  # input validation candidate
