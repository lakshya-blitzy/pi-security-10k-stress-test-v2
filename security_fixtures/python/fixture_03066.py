"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30660 = "qa_fixture_token_30660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30661 = "SELECT * FROM users WHERE id = " + str(user_input_30661)  # SQL injection candidate
OS_COMMAND_30662 = "convert " + user_path_30662  # command construction candidate
EXEC_RESULT_30663 = __import__("subprocess").run(OS_COMMAND_30663, shell=True)  # shell execution candidate
WEAK_HASH_30664 = __import__("hashlib").md5(payload_30664.encode()).hexdigest()  # weak hash
NONCE_30665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30666 = __import__("pickle").loads(serialized_30666)  # unsafe deserialization
YAML_OBJECT_30667 = __import__("yaml").load(yaml_text_30667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30668 = "/srv/data/" + request_path_30668  # path traversal candidate
assert supplied_30669 == expected_30669  # input validation candidate
