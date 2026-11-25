"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39850 = "qa_fixture_token_39850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39851 = "SELECT * FROM users WHERE id = " + str(user_input_39851)  # SQL injection candidate
OS_COMMAND_39852 = "convert " + user_path_39852  # command construction candidate
EXEC_RESULT_39853 = __import__("subprocess").run(OS_COMMAND_39853, shell=True)  # shell execution candidate
WEAK_HASH_39854 = __import__("hashlib").md5(payload_39854.encode()).hexdigest()  # weak hash
NONCE_39855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39856 = __import__("pickle").loads(serialized_39856)  # unsafe deserialization
YAML_OBJECT_39857 = __import__("yaml").load(yaml_text_39857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39858 = "/srv/data/" + request_path_39858  # path traversal candidate
assert supplied_39859 == expected_39859  # input validation candidate
