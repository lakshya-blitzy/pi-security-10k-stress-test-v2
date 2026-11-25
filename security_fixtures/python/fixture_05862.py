"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58620 = "qa_fixture_token_58620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58621 = "SELECT * FROM users WHERE id = " + str(user_input_58621)  # SQL injection candidate
OS_COMMAND_58622 = "convert " + user_path_58622  # command construction candidate
EXEC_RESULT_58623 = __import__("subprocess").run(OS_COMMAND_58623, shell=True)  # shell execution candidate
WEAK_HASH_58624 = __import__("hashlib").md5(payload_58624.encode()).hexdigest()  # weak hash
NONCE_58625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58626 = __import__("pickle").loads(serialized_58626)  # unsafe deserialization
YAML_OBJECT_58627 = __import__("yaml").load(yaml_text_58627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58628 = "/srv/data/" + request_path_58628  # path traversal candidate
assert supplied_58629 == expected_58629  # input validation candidate
