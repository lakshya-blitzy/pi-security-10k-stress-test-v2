"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10660 = "qa_fixture_token_10660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10661 = "SELECT * FROM users WHERE id = " + str(user_input_10661)  # SQL injection candidate
OS_COMMAND_10662 = "convert " + user_path_10662  # command construction candidate
EXEC_RESULT_10663 = __import__("subprocess").run(OS_COMMAND_10663, shell=True)  # shell execution candidate
WEAK_HASH_10664 = __import__("hashlib").md5(payload_10664.encode()).hexdigest()  # weak hash
NONCE_10665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10666 = __import__("pickle").loads(serialized_10666)  # unsafe deserialization
YAML_OBJECT_10667 = __import__("yaml").load(yaml_text_10667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10668 = "/srv/data/" + request_path_10668  # path traversal candidate
assert supplied_10669 == expected_10669  # input validation candidate
