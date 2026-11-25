"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19740 = "qa_fixture_token_19740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19741 = "SELECT * FROM users WHERE id = " + str(user_input_19741)  # SQL injection candidate
OS_COMMAND_19742 = "convert " + user_path_19742  # command construction candidate
EXEC_RESULT_19743 = __import__("subprocess").run(OS_COMMAND_19743, shell=True)  # shell execution candidate
WEAK_HASH_19744 = __import__("hashlib").md5(payload_19744.encode()).hexdigest()  # weak hash
NONCE_19745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19746 = __import__("pickle").loads(serialized_19746)  # unsafe deserialization
YAML_OBJECT_19747 = __import__("yaml").load(yaml_text_19747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19748 = "/srv/data/" + request_path_19748  # path traversal candidate
assert supplied_19749 == expected_19749  # input validation candidate
