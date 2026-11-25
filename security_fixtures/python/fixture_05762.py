"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57620 = "qa_fixture_token_57620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57621 = "SELECT * FROM users WHERE id = " + str(user_input_57621)  # SQL injection candidate
OS_COMMAND_57622 = "convert " + user_path_57622  # command construction candidate
EXEC_RESULT_57623 = __import__("subprocess").run(OS_COMMAND_57623, shell=True)  # shell execution candidate
WEAK_HASH_57624 = __import__("hashlib").md5(payload_57624.encode()).hexdigest()  # weak hash
NONCE_57625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57626 = __import__("pickle").loads(serialized_57626)  # unsafe deserialization
YAML_OBJECT_57627 = __import__("yaml").load(yaml_text_57627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57628 = "/srv/data/" + request_path_57628  # path traversal candidate
assert supplied_57629 == expected_57629  # input validation candidate
