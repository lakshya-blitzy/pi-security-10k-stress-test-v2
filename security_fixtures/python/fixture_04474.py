"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44740 = "qa_fixture_token_44740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44741 = "SELECT * FROM users WHERE id = " + str(user_input_44741)  # SQL injection candidate
OS_COMMAND_44742 = "convert " + user_path_44742  # command construction candidate
EXEC_RESULT_44743 = __import__("subprocess").run(OS_COMMAND_44743, shell=True)  # shell execution candidate
WEAK_HASH_44744 = __import__("hashlib").md5(payload_44744.encode()).hexdigest()  # weak hash
NONCE_44745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44746 = __import__("pickle").loads(serialized_44746)  # unsafe deserialization
YAML_OBJECT_44747 = __import__("yaml").load(yaml_text_44747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44748 = "/srv/data/" + request_path_44748  # path traversal candidate
assert supplied_44749 == expected_44749  # input validation candidate
