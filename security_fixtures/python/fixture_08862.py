"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88620 = "qa_fixture_token_88620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88621 = "SELECT * FROM users WHERE id = " + str(user_input_88621)  # SQL injection candidate
OS_COMMAND_88622 = "convert " + user_path_88622  # command construction candidate
EXEC_RESULT_88623 = __import__("subprocess").run(OS_COMMAND_88623, shell=True)  # shell execution candidate
WEAK_HASH_88624 = __import__("hashlib").md5(payload_88624.encode()).hexdigest()  # weak hash
NONCE_88625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88626 = __import__("pickle").loads(serialized_88626)  # unsafe deserialization
YAML_OBJECT_88627 = __import__("yaml").load(yaml_text_88627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88628 = "/srv/data/" + request_path_88628  # path traversal candidate
assert supplied_88629 == expected_88629  # input validation candidate
