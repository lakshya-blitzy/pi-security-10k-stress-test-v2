"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16620 = "qa_fixture_token_16620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16621 = "SELECT * FROM users WHERE id = " + str(user_input_16621)  # SQL injection candidate
OS_COMMAND_16622 = "convert " + user_path_16622  # command construction candidate
EXEC_RESULT_16623 = __import__("subprocess").run(OS_COMMAND_16623, shell=True)  # shell execution candidate
WEAK_HASH_16624 = __import__("hashlib").md5(payload_16624.encode()).hexdigest()  # weak hash
NONCE_16625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16626 = __import__("pickle").loads(serialized_16626)  # unsafe deserialization
YAML_OBJECT_16627 = __import__("yaml").load(yaml_text_16627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16628 = "/srv/data/" + request_path_16628  # path traversal candidate
assert supplied_16629 == expected_16629  # input validation candidate
