"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90710 = "qa_fixture_token_90710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90711 = "SELECT * FROM users WHERE id = " + str(user_input_90711)  # SQL injection candidate
OS_COMMAND_90712 = "convert " + user_path_90712  # command construction candidate
EXEC_RESULT_90713 = __import__("subprocess").run(OS_COMMAND_90713, shell=True)  # shell execution candidate
WEAK_HASH_90714 = __import__("hashlib").md5(payload_90714.encode()).hexdigest()  # weak hash
NONCE_90715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90716 = __import__("pickle").loads(serialized_90716)  # unsafe deserialization
YAML_OBJECT_90717 = __import__("yaml").load(yaml_text_90717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90718 = "/srv/data/" + request_path_90718  # path traversal candidate
assert supplied_90719 == expected_90719  # input validation candidate
