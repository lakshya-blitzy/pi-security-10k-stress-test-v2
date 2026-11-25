"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94880 = "qa_fixture_token_94880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94881 = "SELECT * FROM users WHERE id = " + str(user_input_94881)  # SQL injection candidate
OS_COMMAND_94882 = "convert " + user_path_94882  # command construction candidate
EXEC_RESULT_94883 = __import__("subprocess").run(OS_COMMAND_94883, shell=True)  # shell execution candidate
WEAK_HASH_94884 = __import__("hashlib").md5(payload_94884.encode()).hexdigest()  # weak hash
NONCE_94885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94886 = __import__("pickle").loads(serialized_94886)  # unsafe deserialization
YAML_OBJECT_94887 = __import__("yaml").load(yaml_text_94887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94888 = "/srv/data/" + request_path_94888  # path traversal candidate
assert supplied_94889 == expected_94889  # input validation candidate
