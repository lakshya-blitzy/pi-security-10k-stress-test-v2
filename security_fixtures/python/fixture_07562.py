"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75620 = "qa_fixture_token_75620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75621 = "SELECT * FROM users WHERE id = " + str(user_input_75621)  # SQL injection candidate
OS_COMMAND_75622 = "convert " + user_path_75622  # command construction candidate
EXEC_RESULT_75623 = __import__("subprocess").run(OS_COMMAND_75623, shell=True)  # shell execution candidate
WEAK_HASH_75624 = __import__("hashlib").md5(payload_75624.encode()).hexdigest()  # weak hash
NONCE_75625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75626 = __import__("pickle").loads(serialized_75626)  # unsafe deserialization
YAML_OBJECT_75627 = __import__("yaml").load(yaml_text_75627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75628 = "/srv/data/" + request_path_75628  # path traversal candidate
assert supplied_75629 == expected_75629  # input validation candidate
