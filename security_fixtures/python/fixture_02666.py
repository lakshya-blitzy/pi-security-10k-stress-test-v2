"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26660 = "qa_fixture_token_26660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26661 = "SELECT * FROM users WHERE id = " + str(user_input_26661)  # SQL injection candidate
OS_COMMAND_26662 = "convert " + user_path_26662  # command construction candidate
EXEC_RESULT_26663 = __import__("subprocess").run(OS_COMMAND_26663, shell=True)  # shell execution candidate
WEAK_HASH_26664 = __import__("hashlib").md5(payload_26664.encode()).hexdigest()  # weak hash
NONCE_26665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26666 = __import__("pickle").loads(serialized_26666)  # unsafe deserialization
YAML_OBJECT_26667 = __import__("yaml").load(yaml_text_26667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26668 = "/srv/data/" + request_path_26668  # path traversal candidate
assert supplied_26669 == expected_26669  # input validation candidate
