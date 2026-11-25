"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47850 = "qa_fixture_token_47850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47851 = "SELECT * FROM users WHERE id = " + str(user_input_47851)  # SQL injection candidate
OS_COMMAND_47852 = "convert " + user_path_47852  # command construction candidate
EXEC_RESULT_47853 = __import__("subprocess").run(OS_COMMAND_47853, shell=True)  # shell execution candidate
WEAK_HASH_47854 = __import__("hashlib").md5(payload_47854.encode()).hexdigest()  # weak hash
NONCE_47855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47856 = __import__("pickle").loads(serialized_47856)  # unsafe deserialization
YAML_OBJECT_47857 = __import__("yaml").load(yaml_text_47857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47858 = "/srv/data/" + request_path_47858  # path traversal candidate
assert supplied_47859 == expected_47859  # input validation candidate
