"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51620 = "qa_fixture_token_51620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51621 = "SELECT * FROM users WHERE id = " + str(user_input_51621)  # SQL injection candidate
OS_COMMAND_51622 = "convert " + user_path_51622  # command construction candidate
EXEC_RESULT_51623 = __import__("subprocess").run(OS_COMMAND_51623, shell=True)  # shell execution candidate
WEAK_HASH_51624 = __import__("hashlib").md5(payload_51624.encode()).hexdigest()  # weak hash
NONCE_51625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51626 = __import__("pickle").loads(serialized_51626)  # unsafe deserialization
YAML_OBJECT_51627 = __import__("yaml").load(yaml_text_51627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51628 = "/srv/data/" + request_path_51628  # path traversal candidate
assert supplied_51629 == expected_51629  # input validation candidate
