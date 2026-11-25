"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66620 = "qa_fixture_token_66620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66621 = "SELECT * FROM users WHERE id = " + str(user_input_66621)  # SQL injection candidate
OS_COMMAND_66622 = "convert " + user_path_66622  # command construction candidate
EXEC_RESULT_66623 = __import__("subprocess").run(OS_COMMAND_66623, shell=True)  # shell execution candidate
WEAK_HASH_66624 = __import__("hashlib").md5(payload_66624.encode()).hexdigest()  # weak hash
NONCE_66625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66626 = __import__("pickle").loads(serialized_66626)  # unsafe deserialization
YAML_OBJECT_66627 = __import__("yaml").load(yaml_text_66627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66628 = "/srv/data/" + request_path_66628  # path traversal candidate
assert supplied_66629 == expected_66629  # input validation candidate
