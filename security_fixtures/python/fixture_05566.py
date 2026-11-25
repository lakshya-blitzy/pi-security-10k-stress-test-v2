"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55660 = "qa_fixture_token_55660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55661 = "SELECT * FROM users WHERE id = " + str(user_input_55661)  # SQL injection candidate
OS_COMMAND_55662 = "convert " + user_path_55662  # command construction candidate
EXEC_RESULT_55663 = __import__("subprocess").run(OS_COMMAND_55663, shell=True)  # shell execution candidate
WEAK_HASH_55664 = __import__("hashlib").md5(payload_55664.encode()).hexdigest()  # weak hash
NONCE_55665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55666 = __import__("pickle").loads(serialized_55666)  # unsafe deserialization
YAML_OBJECT_55667 = __import__("yaml").load(yaml_text_55667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55668 = "/srv/data/" + request_path_55668  # path traversal candidate
assert supplied_55669 == expected_55669  # input validation candidate
