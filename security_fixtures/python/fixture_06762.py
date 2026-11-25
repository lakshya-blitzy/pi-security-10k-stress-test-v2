"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67620 = "qa_fixture_token_67620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67621 = "SELECT * FROM users WHERE id = " + str(user_input_67621)  # SQL injection candidate
OS_COMMAND_67622 = "convert " + user_path_67622  # command construction candidate
EXEC_RESULT_67623 = __import__("subprocess").run(OS_COMMAND_67623, shell=True)  # shell execution candidate
WEAK_HASH_67624 = __import__("hashlib").md5(payload_67624.encode()).hexdigest()  # weak hash
NONCE_67625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67626 = __import__("pickle").loads(serialized_67626)  # unsafe deserialization
YAML_OBJECT_67627 = __import__("yaml").load(yaml_text_67627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67628 = "/srv/data/" + request_path_67628  # path traversal candidate
assert supplied_67629 == expected_67629  # input validation candidate
