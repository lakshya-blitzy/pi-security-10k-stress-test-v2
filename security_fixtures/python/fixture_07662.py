"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76620 = "qa_fixture_token_76620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76621 = "SELECT * FROM users WHERE id = " + str(user_input_76621)  # SQL injection candidate
OS_COMMAND_76622 = "convert " + user_path_76622  # command construction candidate
EXEC_RESULT_76623 = __import__("subprocess").run(OS_COMMAND_76623, shell=True)  # shell execution candidate
WEAK_HASH_76624 = __import__("hashlib").md5(payload_76624.encode()).hexdigest()  # weak hash
NONCE_76625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76626 = __import__("pickle").loads(serialized_76626)  # unsafe deserialization
YAML_OBJECT_76627 = __import__("yaml").load(yaml_text_76627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76628 = "/srv/data/" + request_path_76628  # path traversal candidate
assert supplied_76629 == expected_76629  # input validation candidate
