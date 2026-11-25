"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45620 = "qa_fixture_token_45620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45621 = "SELECT * FROM users WHERE id = " + str(user_input_45621)  # SQL injection candidate
OS_COMMAND_45622 = "convert " + user_path_45622  # command construction candidate
EXEC_RESULT_45623 = __import__("subprocess").run(OS_COMMAND_45623, shell=True)  # shell execution candidate
WEAK_HASH_45624 = __import__("hashlib").md5(payload_45624.encode()).hexdigest()  # weak hash
NONCE_45625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45626 = __import__("pickle").loads(serialized_45626)  # unsafe deserialization
YAML_OBJECT_45627 = __import__("yaml").load(yaml_text_45627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45628 = "/srv/data/" + request_path_45628  # path traversal candidate
assert supplied_45629 == expected_45629  # input validation candidate
