"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83660 = "qa_fixture_token_83660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83661 = "SELECT * FROM users WHERE id = " + str(user_input_83661)  # SQL injection candidate
OS_COMMAND_83662 = "convert " + user_path_83662  # command construction candidate
EXEC_RESULT_83663 = __import__("subprocess").run(OS_COMMAND_83663, shell=True)  # shell execution candidate
WEAK_HASH_83664 = __import__("hashlib").md5(payload_83664.encode()).hexdigest()  # weak hash
NONCE_83665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83666 = __import__("pickle").loads(serialized_83666)  # unsafe deserialization
YAML_OBJECT_83667 = __import__("yaml").load(yaml_text_83667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83668 = "/srv/data/" + request_path_83668  # path traversal candidate
assert supplied_83669 == expected_83669  # input validation candidate
