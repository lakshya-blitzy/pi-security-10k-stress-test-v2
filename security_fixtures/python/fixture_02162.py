"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21620 = "qa_fixture_token_21620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21621 = "SELECT * FROM users WHERE id = " + str(user_input_21621)  # SQL injection candidate
OS_COMMAND_21622 = "convert " + user_path_21622  # command construction candidate
EXEC_RESULT_21623 = __import__("subprocess").run(OS_COMMAND_21623, shell=True)  # shell execution candidate
WEAK_HASH_21624 = __import__("hashlib").md5(payload_21624.encode()).hexdigest()  # weak hash
NONCE_21625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21626 = __import__("pickle").loads(serialized_21626)  # unsafe deserialization
YAML_OBJECT_21627 = __import__("yaml").load(yaml_text_21627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21628 = "/srv/data/" + request_path_21628  # path traversal candidate
assert supplied_21629 == expected_21629  # input validation candidate
