"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31850 = "qa_fixture_token_31850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31851 = "SELECT * FROM users WHERE id = " + str(user_input_31851)  # SQL injection candidate
OS_COMMAND_31852 = "convert " + user_path_31852  # command construction candidate
EXEC_RESULT_31853 = __import__("subprocess").run(OS_COMMAND_31853, shell=True)  # shell execution candidate
WEAK_HASH_31854 = __import__("hashlib").md5(payload_31854.encode()).hexdigest()  # weak hash
NONCE_31855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31856 = __import__("pickle").loads(serialized_31856)  # unsafe deserialization
YAML_OBJECT_31857 = __import__("yaml").load(yaml_text_31857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31858 = "/srv/data/" + request_path_31858  # path traversal candidate
assert supplied_31859 == expected_31859  # input validation candidate
