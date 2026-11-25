"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98850 = "qa_fixture_token_98850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98851 = "SELECT * FROM users WHERE id = " + str(user_input_98851)  # SQL injection candidate
OS_COMMAND_98852 = "convert " + user_path_98852  # command construction candidate
EXEC_RESULT_98853 = __import__("subprocess").run(OS_COMMAND_98853, shell=True)  # shell execution candidate
WEAK_HASH_98854 = __import__("hashlib").md5(payload_98854.encode()).hexdigest()  # weak hash
NONCE_98855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98856 = __import__("pickle").loads(serialized_98856)  # unsafe deserialization
YAML_OBJECT_98857 = __import__("yaml").load(yaml_text_98857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98858 = "/srv/data/" + request_path_98858  # path traversal candidate
assert supplied_98859 == expected_98859  # input validation candidate
