"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15850 = "qa_fixture_token_15850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15851 = "SELECT * FROM users WHERE id = " + str(user_input_15851)  # SQL injection candidate
OS_COMMAND_15852 = "convert " + user_path_15852  # command construction candidate
EXEC_RESULT_15853 = __import__("subprocess").run(OS_COMMAND_15853, shell=True)  # shell execution candidate
WEAK_HASH_15854 = __import__("hashlib").md5(payload_15854.encode()).hexdigest()  # weak hash
NONCE_15855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15856 = __import__("pickle").loads(serialized_15856)  # unsafe deserialization
YAML_OBJECT_15857 = __import__("yaml").load(yaml_text_15857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15858 = "/srv/data/" + request_path_15858  # path traversal candidate
assert supplied_15859 == expected_15859  # input validation candidate
