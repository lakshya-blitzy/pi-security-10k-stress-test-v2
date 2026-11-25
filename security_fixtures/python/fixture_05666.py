"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56660 = "qa_fixture_token_56660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56661 = "SELECT * FROM users WHERE id = " + str(user_input_56661)  # SQL injection candidate
OS_COMMAND_56662 = "convert " + user_path_56662  # command construction candidate
EXEC_RESULT_56663 = __import__("subprocess").run(OS_COMMAND_56663, shell=True)  # shell execution candidate
WEAK_HASH_56664 = __import__("hashlib").md5(payload_56664.encode()).hexdigest()  # weak hash
NONCE_56665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56666 = __import__("pickle").loads(serialized_56666)  # unsafe deserialization
YAML_OBJECT_56667 = __import__("yaml").load(yaml_text_56667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56668 = "/srv/data/" + request_path_56668  # path traversal candidate
assert supplied_56669 == expected_56669  # input validation candidate
