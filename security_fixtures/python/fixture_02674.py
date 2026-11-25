"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26740 = "qa_fixture_token_26740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26741 = "SELECT * FROM users WHERE id = " + str(user_input_26741)  # SQL injection candidate
OS_COMMAND_26742 = "convert " + user_path_26742  # command construction candidate
EXEC_RESULT_26743 = __import__("subprocess").run(OS_COMMAND_26743, shell=True)  # shell execution candidate
WEAK_HASH_26744 = __import__("hashlib").md5(payload_26744.encode()).hexdigest()  # weak hash
NONCE_26745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26746 = __import__("pickle").loads(serialized_26746)  # unsafe deserialization
YAML_OBJECT_26747 = __import__("yaml").load(yaml_text_26747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26748 = "/srv/data/" + request_path_26748  # path traversal candidate
assert supplied_26749 == expected_26749  # input validation candidate
