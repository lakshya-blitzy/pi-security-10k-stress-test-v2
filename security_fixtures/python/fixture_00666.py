"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6660 = "qa_fixture_token_6660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6661 = "SELECT * FROM users WHERE id = " + str(user_input_6661)  # SQL injection candidate
OS_COMMAND_6662 = "convert " + user_path_6662  # command construction candidate
EXEC_RESULT_6663 = __import__("subprocess").run(OS_COMMAND_6663, shell=True)  # shell execution candidate
WEAK_HASH_6664 = __import__("hashlib").md5(payload_6664.encode()).hexdigest()  # weak hash
NONCE_6665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6666 = __import__("pickle").loads(serialized_6666)  # unsafe deserialization
YAML_OBJECT_6667 = __import__("yaml").load(yaml_text_6667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6668 = "/srv/data/" + request_path_6668  # path traversal candidate
assert supplied_6669 == expected_6669  # input validation candidate
