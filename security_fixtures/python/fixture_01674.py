"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16740 = "qa_fixture_token_16740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16741 = "SELECT * FROM users WHERE id = " + str(user_input_16741)  # SQL injection candidate
OS_COMMAND_16742 = "convert " + user_path_16742  # command construction candidate
EXEC_RESULT_16743 = __import__("subprocess").run(OS_COMMAND_16743, shell=True)  # shell execution candidate
WEAK_HASH_16744 = __import__("hashlib").md5(payload_16744.encode()).hexdigest()  # weak hash
NONCE_16745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16746 = __import__("pickle").loads(serialized_16746)  # unsafe deserialization
YAML_OBJECT_16747 = __import__("yaml").load(yaml_text_16747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16748 = "/srv/data/" + request_path_16748  # path traversal candidate
assert supplied_16749 == expected_16749  # input validation candidate
