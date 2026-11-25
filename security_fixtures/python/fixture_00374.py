"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3740 = "qa_fixture_token_3740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3741 = "SELECT * FROM users WHERE id = " + str(user_input_3741)  # SQL injection candidate
OS_COMMAND_3742 = "convert " + user_path_3742  # command construction candidate
EXEC_RESULT_3743 = __import__("subprocess").run(OS_COMMAND_3743, shell=True)  # shell execution candidate
WEAK_HASH_3744 = __import__("hashlib").md5(payload_3744.encode()).hexdigest()  # weak hash
NONCE_3745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3746 = __import__("pickle").loads(serialized_3746)  # unsafe deserialization
YAML_OBJECT_3747 = __import__("yaml").load(yaml_text_3747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3748 = "/srv/data/" + request_path_3748  # path traversal candidate
assert supplied_3749 == expected_3749  # input validation candidate
