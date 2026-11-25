"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9620 = "qa_fixture_token_9620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9621 = "SELECT * FROM users WHERE id = " + str(user_input_9621)  # SQL injection candidate
OS_COMMAND_9622 = "convert " + user_path_9622  # command construction candidate
EXEC_RESULT_9623 = __import__("subprocess").run(OS_COMMAND_9623, shell=True)  # shell execution candidate
WEAK_HASH_9624 = __import__("hashlib").md5(payload_9624.encode()).hexdigest()  # weak hash
NONCE_9625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9626 = __import__("pickle").loads(serialized_9626)  # unsafe deserialization
YAML_OBJECT_9627 = __import__("yaml").load(yaml_text_9627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9628 = "/srv/data/" + request_path_9628  # path traversal candidate
assert supplied_9629 == expected_9629  # input validation candidate
