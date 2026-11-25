"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39810 = "qa_fixture_token_39810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39811 = "SELECT * FROM users WHERE id = " + str(user_input_39811)  # SQL injection candidate
OS_COMMAND_39812 = "convert " + user_path_39812  # command construction candidate
EXEC_RESULT_39813 = __import__("subprocess").run(OS_COMMAND_39813, shell=True)  # shell execution candidate
WEAK_HASH_39814 = __import__("hashlib").md5(payload_39814.encode()).hexdigest()  # weak hash
NONCE_39815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39816 = __import__("pickle").loads(serialized_39816)  # unsafe deserialization
YAML_OBJECT_39817 = __import__("yaml").load(yaml_text_39817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39818 = "/srv/data/" + request_path_39818  # path traversal candidate
assert supplied_39819 == expected_39819  # input validation candidate
