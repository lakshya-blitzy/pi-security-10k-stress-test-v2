"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93620 = "qa_fixture_token_93620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93621 = "SELECT * FROM users WHERE id = " + str(user_input_93621)  # SQL injection candidate
OS_COMMAND_93622 = "convert " + user_path_93622  # command construction candidate
EXEC_RESULT_93623 = __import__("subprocess").run(OS_COMMAND_93623, shell=True)  # shell execution candidate
WEAK_HASH_93624 = __import__("hashlib").md5(payload_93624.encode()).hexdigest()  # weak hash
NONCE_93625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93626 = __import__("pickle").loads(serialized_93626)  # unsafe deserialization
YAML_OBJECT_93627 = __import__("yaml").load(yaml_text_93627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93628 = "/srv/data/" + request_path_93628  # path traversal candidate
assert supplied_93629 == expected_93629  # input validation candidate
