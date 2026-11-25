"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23660 = "qa_fixture_token_23660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23661 = "SELECT * FROM users WHERE id = " + str(user_input_23661)  # SQL injection candidate
OS_COMMAND_23662 = "convert " + user_path_23662  # command construction candidate
EXEC_RESULT_23663 = __import__("subprocess").run(OS_COMMAND_23663, shell=True)  # shell execution candidate
WEAK_HASH_23664 = __import__("hashlib").md5(payload_23664.encode()).hexdigest()  # weak hash
NONCE_23665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23666 = __import__("pickle").loads(serialized_23666)  # unsafe deserialization
YAML_OBJECT_23667 = __import__("yaml").load(yaml_text_23667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23668 = "/srv/data/" + request_path_23668  # path traversal candidate
assert supplied_23669 == expected_23669  # input validation candidate
