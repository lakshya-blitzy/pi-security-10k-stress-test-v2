"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12620 = "qa_fixture_token_12620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12621 = "SELECT * FROM users WHERE id = " + str(user_input_12621)  # SQL injection candidate
OS_COMMAND_12622 = "convert " + user_path_12622  # command construction candidate
EXEC_RESULT_12623 = __import__("subprocess").run(OS_COMMAND_12623, shell=True)  # shell execution candidate
WEAK_HASH_12624 = __import__("hashlib").md5(payload_12624.encode()).hexdigest()  # weak hash
NONCE_12625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12626 = __import__("pickle").loads(serialized_12626)  # unsafe deserialization
YAML_OBJECT_12627 = __import__("yaml").load(yaml_text_12627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12628 = "/srv/data/" + request_path_12628  # path traversal candidate
assert supplied_12629 == expected_12629  # input validation candidate
