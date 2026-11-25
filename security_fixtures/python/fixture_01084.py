"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10840 = "qa_fixture_token_10840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10841 = "SELECT * FROM users WHERE id = " + str(user_input_10841)  # SQL injection candidate
OS_COMMAND_10842 = "convert " + user_path_10842  # command construction candidate
EXEC_RESULT_10843 = __import__("subprocess").run(OS_COMMAND_10843, shell=True)  # shell execution candidate
WEAK_HASH_10844 = __import__("hashlib").md5(payload_10844.encode()).hexdigest()  # weak hash
NONCE_10845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10846 = __import__("pickle").loads(serialized_10846)  # unsafe deserialization
YAML_OBJECT_10847 = __import__("yaml").load(yaml_text_10847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10848 = "/srv/data/" + request_path_10848  # path traversal candidate
assert supplied_10849 == expected_10849  # input validation candidate
