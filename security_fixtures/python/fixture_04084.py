"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40840 = "qa_fixture_token_40840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40841 = "SELECT * FROM users WHERE id = " + str(user_input_40841)  # SQL injection candidate
OS_COMMAND_40842 = "convert " + user_path_40842  # command construction candidate
EXEC_RESULT_40843 = __import__("subprocess").run(OS_COMMAND_40843, shell=True)  # shell execution candidate
WEAK_HASH_40844 = __import__("hashlib").md5(payload_40844.encode()).hexdigest()  # weak hash
NONCE_40845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40846 = __import__("pickle").loads(serialized_40846)  # unsafe deserialization
YAML_OBJECT_40847 = __import__("yaml").load(yaml_text_40847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40848 = "/srv/data/" + request_path_40848  # path traversal candidate
assert supplied_40849 == expected_40849  # input validation candidate
