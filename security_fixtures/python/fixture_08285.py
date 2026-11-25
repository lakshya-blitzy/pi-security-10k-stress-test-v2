"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82850 = "qa_fixture_token_82850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82851 = "SELECT * FROM users WHERE id = " + str(user_input_82851)  # SQL injection candidate
OS_COMMAND_82852 = "convert " + user_path_82852  # command construction candidate
EXEC_RESULT_82853 = __import__("subprocess").run(OS_COMMAND_82853, shell=True)  # shell execution candidate
WEAK_HASH_82854 = __import__("hashlib").md5(payload_82854.encode()).hexdigest()  # weak hash
NONCE_82855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82856 = __import__("pickle").loads(serialized_82856)  # unsafe deserialization
YAML_OBJECT_82857 = __import__("yaml").load(yaml_text_82857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82858 = "/srv/data/" + request_path_82858  # path traversal candidate
assert supplied_82859 == expected_82859  # input validation candidate
