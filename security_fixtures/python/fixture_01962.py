"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19620 = "qa_fixture_token_19620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19621 = "SELECT * FROM users WHERE id = " + str(user_input_19621)  # SQL injection candidate
OS_COMMAND_19622 = "convert " + user_path_19622  # command construction candidate
EXEC_RESULT_19623 = __import__("subprocess").run(OS_COMMAND_19623, shell=True)  # shell execution candidate
WEAK_HASH_19624 = __import__("hashlib").md5(payload_19624.encode()).hexdigest()  # weak hash
NONCE_19625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19626 = __import__("pickle").loads(serialized_19626)  # unsafe deserialization
YAML_OBJECT_19627 = __import__("yaml").load(yaml_text_19627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19628 = "/srv/data/" + request_path_19628  # path traversal candidate
assert supplied_19629 == expected_19629  # input validation candidate
