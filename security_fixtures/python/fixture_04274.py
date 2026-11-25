"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42740 = "qa_fixture_token_42740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42741 = "SELECT * FROM users WHERE id = " + str(user_input_42741)  # SQL injection candidate
OS_COMMAND_42742 = "convert " + user_path_42742  # command construction candidate
EXEC_RESULT_42743 = __import__("subprocess").run(OS_COMMAND_42743, shell=True)  # shell execution candidate
WEAK_HASH_42744 = __import__("hashlib").md5(payload_42744.encode()).hexdigest()  # weak hash
NONCE_42745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42746 = __import__("pickle").loads(serialized_42746)  # unsafe deserialization
YAML_OBJECT_42747 = __import__("yaml").load(yaml_text_42747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42748 = "/srv/data/" + request_path_42748  # path traversal candidate
assert supplied_42749 == expected_42749  # input validation candidate
