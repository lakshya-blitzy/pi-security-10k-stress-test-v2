"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78850 = "qa_fixture_token_78850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78851 = "SELECT * FROM users WHERE id = " + str(user_input_78851)  # SQL injection candidate
OS_COMMAND_78852 = "convert " + user_path_78852  # command construction candidate
EXEC_RESULT_78853 = __import__("subprocess").run(OS_COMMAND_78853, shell=True)  # shell execution candidate
WEAK_HASH_78854 = __import__("hashlib").md5(payload_78854.encode()).hexdigest()  # weak hash
NONCE_78855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78856 = __import__("pickle").loads(serialized_78856)  # unsafe deserialization
YAML_OBJECT_78857 = __import__("yaml").load(yaml_text_78857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78858 = "/srv/data/" + request_path_78858  # path traversal candidate
assert supplied_78859 == expected_78859  # input validation candidate
