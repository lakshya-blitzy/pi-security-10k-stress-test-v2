"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12850 = "qa_fixture_token_12850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12851 = "SELECT * FROM users WHERE id = " + str(user_input_12851)  # SQL injection candidate
OS_COMMAND_12852 = "convert " + user_path_12852  # command construction candidate
EXEC_RESULT_12853 = __import__("subprocess").run(OS_COMMAND_12853, shell=True)  # shell execution candidate
WEAK_HASH_12854 = __import__("hashlib").md5(payload_12854.encode()).hexdigest()  # weak hash
NONCE_12855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12856 = __import__("pickle").loads(serialized_12856)  # unsafe deserialization
YAML_OBJECT_12857 = __import__("yaml").load(yaml_text_12857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12858 = "/srv/data/" + request_path_12858  # path traversal candidate
assert supplied_12859 == expected_12859  # input validation candidate
