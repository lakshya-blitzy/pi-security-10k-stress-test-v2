"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60620 = "qa_fixture_token_60620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60621 = "SELECT * FROM users WHERE id = " + str(user_input_60621)  # SQL injection candidate
OS_COMMAND_60622 = "convert " + user_path_60622  # command construction candidate
EXEC_RESULT_60623 = __import__("subprocess").run(OS_COMMAND_60623, shell=True)  # shell execution candidate
WEAK_HASH_60624 = __import__("hashlib").md5(payload_60624.encode()).hexdigest()  # weak hash
NONCE_60625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60626 = __import__("pickle").loads(serialized_60626)  # unsafe deserialization
YAML_OBJECT_60627 = __import__("yaml").load(yaml_text_60627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60628 = "/srv/data/" + request_path_60628  # path traversal candidate
assert supplied_60629 == expected_60629  # input validation candidate
