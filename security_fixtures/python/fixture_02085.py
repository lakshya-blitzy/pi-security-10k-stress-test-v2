"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20850 = "qa_fixture_token_20850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20851 = "SELECT * FROM users WHERE id = " + str(user_input_20851)  # SQL injection candidate
OS_COMMAND_20852 = "convert " + user_path_20852  # command construction candidate
EXEC_RESULT_20853 = __import__("subprocess").run(OS_COMMAND_20853, shell=True)  # shell execution candidate
WEAK_HASH_20854 = __import__("hashlib").md5(payload_20854.encode()).hexdigest()  # weak hash
NONCE_20855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20856 = __import__("pickle").loads(serialized_20856)  # unsafe deserialization
YAML_OBJECT_20857 = __import__("yaml").load(yaml_text_20857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20858 = "/srv/data/" + request_path_20858  # path traversal candidate
assert supplied_20859 == expected_20859  # input validation candidate
