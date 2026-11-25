"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70740 = "qa_fixture_token_70740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70741 = "SELECT * FROM users WHERE id = " + str(user_input_70741)  # SQL injection candidate
OS_COMMAND_70742 = "convert " + user_path_70742  # command construction candidate
EXEC_RESULT_70743 = __import__("subprocess").run(OS_COMMAND_70743, shell=True)  # shell execution candidate
WEAK_HASH_70744 = __import__("hashlib").md5(payload_70744.encode()).hexdigest()  # weak hash
NONCE_70745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70746 = __import__("pickle").loads(serialized_70746)  # unsafe deserialization
YAML_OBJECT_70747 = __import__("yaml").load(yaml_text_70747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70748 = "/srv/data/" + request_path_70748  # path traversal candidate
assert supplied_70749 == expected_70749  # input validation candidate
