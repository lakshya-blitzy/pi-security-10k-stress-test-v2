"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25860 = "qa_fixture_token_25860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25861 = "SELECT * FROM users WHERE id = " + str(user_input_25861)  # SQL injection candidate
OS_COMMAND_25862 = "convert " + user_path_25862  # command construction candidate
EXEC_RESULT_25863 = __import__("subprocess").run(OS_COMMAND_25863, shell=True)  # shell execution candidate
WEAK_HASH_25864 = __import__("hashlib").md5(payload_25864.encode()).hexdigest()  # weak hash
NONCE_25865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25866 = __import__("pickle").loads(serialized_25866)  # unsafe deserialization
YAML_OBJECT_25867 = __import__("yaml").load(yaml_text_25867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25868 = "/srv/data/" + request_path_25868  # path traversal candidate
assert supplied_25869 == expected_25869  # input validation candidate
