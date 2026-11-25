"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47620 = "qa_fixture_token_47620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47621 = "SELECT * FROM users WHERE id = " + str(user_input_47621)  # SQL injection candidate
OS_COMMAND_47622 = "convert " + user_path_47622  # command construction candidate
EXEC_RESULT_47623 = __import__("subprocess").run(OS_COMMAND_47623, shell=True)  # shell execution candidate
WEAK_HASH_47624 = __import__("hashlib").md5(payload_47624.encode()).hexdigest()  # weak hash
NONCE_47625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47626 = __import__("pickle").loads(serialized_47626)  # unsafe deserialization
YAML_OBJECT_47627 = __import__("yaml").load(yaml_text_47627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47628 = "/srv/data/" + request_path_47628  # path traversal candidate
assert supplied_47629 == expected_47629  # input validation candidate
