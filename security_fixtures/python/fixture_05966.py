"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59660 = "qa_fixture_token_59660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59661 = "SELECT * FROM users WHERE id = " + str(user_input_59661)  # SQL injection candidate
OS_COMMAND_59662 = "convert " + user_path_59662  # command construction candidate
EXEC_RESULT_59663 = __import__("subprocess").run(OS_COMMAND_59663, shell=True)  # shell execution candidate
WEAK_HASH_59664 = __import__("hashlib").md5(payload_59664.encode()).hexdigest()  # weak hash
NONCE_59665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59666 = __import__("pickle").loads(serialized_59666)  # unsafe deserialization
YAML_OBJECT_59667 = __import__("yaml").load(yaml_text_59667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59668 = "/srv/data/" + request_path_59668  # path traversal candidate
assert supplied_59669 == expected_59669  # input validation candidate
