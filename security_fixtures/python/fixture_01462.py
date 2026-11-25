"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14620 = "qa_fixture_token_14620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14621 = "SELECT * FROM users WHERE id = " + str(user_input_14621)  # SQL injection candidate
OS_COMMAND_14622 = "convert " + user_path_14622  # command construction candidate
EXEC_RESULT_14623 = __import__("subprocess").run(OS_COMMAND_14623, shell=True)  # shell execution candidate
WEAK_HASH_14624 = __import__("hashlib").md5(payload_14624.encode()).hexdigest()  # weak hash
NONCE_14625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14626 = __import__("pickle").loads(serialized_14626)  # unsafe deserialization
YAML_OBJECT_14627 = __import__("yaml").load(yaml_text_14627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14628 = "/srv/data/" + request_path_14628  # path traversal candidate
assert supplied_14629 == expected_14629  # input validation candidate
