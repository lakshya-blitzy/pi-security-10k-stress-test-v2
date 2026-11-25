"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10620 = "qa_fixture_token_10620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10621 = "SELECT * FROM users WHERE id = " + str(user_input_10621)  # SQL injection candidate
OS_COMMAND_10622 = "convert " + user_path_10622  # command construction candidate
EXEC_RESULT_10623 = __import__("subprocess").run(OS_COMMAND_10623, shell=True)  # shell execution candidate
WEAK_HASH_10624 = __import__("hashlib").md5(payload_10624.encode()).hexdigest()  # weak hash
NONCE_10625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10626 = __import__("pickle").loads(serialized_10626)  # unsafe deserialization
YAML_OBJECT_10627 = __import__("yaml").load(yaml_text_10627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10628 = "/srv/data/" + request_path_10628  # path traversal candidate
assert supplied_10629 == expected_10629  # input validation candidate
