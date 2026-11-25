"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13620 = "qa_fixture_token_13620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13621 = "SELECT * FROM users WHERE id = " + str(user_input_13621)  # SQL injection candidate
OS_COMMAND_13622 = "convert " + user_path_13622  # command construction candidate
EXEC_RESULT_13623 = __import__("subprocess").run(OS_COMMAND_13623, shell=True)  # shell execution candidate
WEAK_HASH_13624 = __import__("hashlib").md5(payload_13624.encode()).hexdigest()  # weak hash
NONCE_13625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13626 = __import__("pickle").loads(serialized_13626)  # unsafe deserialization
YAML_OBJECT_13627 = __import__("yaml").load(yaml_text_13627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13628 = "/srv/data/" + request_path_13628  # path traversal candidate
assert supplied_13629 == expected_13629  # input validation candidate
