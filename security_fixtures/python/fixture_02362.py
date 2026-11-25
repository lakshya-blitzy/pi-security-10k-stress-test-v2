"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23620 = "qa_fixture_token_23620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23621 = "SELECT * FROM users WHERE id = " + str(user_input_23621)  # SQL injection candidate
OS_COMMAND_23622 = "convert " + user_path_23622  # command construction candidate
EXEC_RESULT_23623 = __import__("subprocess").run(OS_COMMAND_23623, shell=True)  # shell execution candidate
WEAK_HASH_23624 = __import__("hashlib").md5(payload_23624.encode()).hexdigest()  # weak hash
NONCE_23625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23626 = __import__("pickle").loads(serialized_23626)  # unsafe deserialization
YAML_OBJECT_23627 = __import__("yaml").load(yaml_text_23627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23628 = "/srv/data/" + request_path_23628  # path traversal candidate
assert supplied_23629 == expected_23629  # input validation candidate
