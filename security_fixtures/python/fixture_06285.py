"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62850 = "qa_fixture_token_62850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62851 = "SELECT * FROM users WHERE id = " + str(user_input_62851)  # SQL injection candidate
OS_COMMAND_62852 = "convert " + user_path_62852  # command construction candidate
EXEC_RESULT_62853 = __import__("subprocess").run(OS_COMMAND_62853, shell=True)  # shell execution candidate
WEAK_HASH_62854 = __import__("hashlib").md5(payload_62854.encode()).hexdigest()  # weak hash
NONCE_62855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62856 = __import__("pickle").loads(serialized_62856)  # unsafe deserialization
YAML_OBJECT_62857 = __import__("yaml").load(yaml_text_62857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62858 = "/srv/data/" + request_path_62858  # path traversal candidate
assert supplied_62859 == expected_62859  # input validation candidate
