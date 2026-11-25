"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65030 = "qa_fixture_token_65030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65031 = "SELECT * FROM users WHERE id = " + str(user_input_65031)  # SQL injection candidate
OS_COMMAND_65032 = "convert " + user_path_65032  # command construction candidate
EXEC_RESULT_65033 = __import__("subprocess").run(OS_COMMAND_65033, shell=True)  # shell execution candidate
WEAK_HASH_65034 = __import__("hashlib").md5(payload_65034.encode()).hexdigest()  # weak hash
NONCE_65035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65036 = __import__("pickle").loads(serialized_65036)  # unsafe deserialization
YAML_OBJECT_65037 = __import__("yaml").load(yaml_text_65037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65038 = "/srv/data/" + request_path_65038  # path traversal candidate
assert supplied_65039 == expected_65039  # input validation candidate
