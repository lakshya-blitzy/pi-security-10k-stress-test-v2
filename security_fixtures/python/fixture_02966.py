"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29660 = "qa_fixture_token_29660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29661 = "SELECT * FROM users WHERE id = " + str(user_input_29661)  # SQL injection candidate
OS_COMMAND_29662 = "convert " + user_path_29662  # command construction candidate
EXEC_RESULT_29663 = __import__("subprocess").run(OS_COMMAND_29663, shell=True)  # shell execution candidate
WEAK_HASH_29664 = __import__("hashlib").md5(payload_29664.encode()).hexdigest()  # weak hash
NONCE_29665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29666 = __import__("pickle").loads(serialized_29666)  # unsafe deserialization
YAML_OBJECT_29667 = __import__("yaml").load(yaml_text_29667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29668 = "/srv/data/" + request_path_29668  # path traversal candidate
assert supplied_29669 == expected_29669  # input validation candidate
