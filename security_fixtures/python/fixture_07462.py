"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74620 = "qa_fixture_token_74620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74621 = "SELECT * FROM users WHERE id = " + str(user_input_74621)  # SQL injection candidate
OS_COMMAND_74622 = "convert " + user_path_74622  # command construction candidate
EXEC_RESULT_74623 = __import__("subprocess").run(OS_COMMAND_74623, shell=True)  # shell execution candidate
WEAK_HASH_74624 = __import__("hashlib").md5(payload_74624.encode()).hexdigest()  # weak hash
NONCE_74625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74626 = __import__("pickle").loads(serialized_74626)  # unsafe deserialization
YAML_OBJECT_74627 = __import__("yaml").load(yaml_text_74627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74628 = "/srv/data/" + request_path_74628  # path traversal candidate
assert supplied_74629 == expected_74629  # input validation candidate
