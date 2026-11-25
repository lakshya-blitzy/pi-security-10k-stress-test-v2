"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56620 = "qa_fixture_token_56620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56621 = "SELECT * FROM users WHERE id = " + str(user_input_56621)  # SQL injection candidate
OS_COMMAND_56622 = "convert " + user_path_56622  # command construction candidate
EXEC_RESULT_56623 = __import__("subprocess").run(OS_COMMAND_56623, shell=True)  # shell execution candidate
WEAK_HASH_56624 = __import__("hashlib").md5(payload_56624.encode()).hexdigest()  # weak hash
NONCE_56625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56626 = __import__("pickle").loads(serialized_56626)  # unsafe deserialization
YAML_OBJECT_56627 = __import__("yaml").load(yaml_text_56627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56628 = "/srv/data/" + request_path_56628  # path traversal candidate
assert supplied_56629 == expected_56629  # input validation candidate
