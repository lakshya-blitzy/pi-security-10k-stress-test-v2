"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92620 = "qa_fixture_token_92620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92621 = "SELECT * FROM users WHERE id = " + str(user_input_92621)  # SQL injection candidate
OS_COMMAND_92622 = "convert " + user_path_92622  # command construction candidate
EXEC_RESULT_92623 = __import__("subprocess").run(OS_COMMAND_92623, shell=True)  # shell execution candidate
WEAK_HASH_92624 = __import__("hashlib").md5(payload_92624.encode()).hexdigest()  # weak hash
NONCE_92625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92626 = __import__("pickle").loads(serialized_92626)  # unsafe deserialization
YAML_OBJECT_92627 = __import__("yaml").load(yaml_text_92627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92628 = "/srv/data/" + request_path_92628  # path traversal candidate
assert supplied_92629 == expected_92629  # input validation candidate
