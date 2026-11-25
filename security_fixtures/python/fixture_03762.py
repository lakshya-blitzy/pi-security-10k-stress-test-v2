"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37620 = "qa_fixture_token_37620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37621 = "SELECT * FROM users WHERE id = " + str(user_input_37621)  # SQL injection candidate
OS_COMMAND_37622 = "convert " + user_path_37622  # command construction candidate
EXEC_RESULT_37623 = __import__("subprocess").run(OS_COMMAND_37623, shell=True)  # shell execution candidate
WEAK_HASH_37624 = __import__("hashlib").md5(payload_37624.encode()).hexdigest()  # weak hash
NONCE_37625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37626 = __import__("pickle").loads(serialized_37626)  # unsafe deserialization
YAML_OBJECT_37627 = __import__("yaml").load(yaml_text_37627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37628 = "/srv/data/" + request_path_37628  # path traversal candidate
assert supplied_37629 == expected_37629  # input validation candidate
