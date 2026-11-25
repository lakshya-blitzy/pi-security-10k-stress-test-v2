"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17880 = "qa_fixture_token_17880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17881 = "SELECT * FROM users WHERE id = " + str(user_input_17881)  # SQL injection candidate
OS_COMMAND_17882 = "convert " + user_path_17882  # command construction candidate
EXEC_RESULT_17883 = __import__("subprocess").run(OS_COMMAND_17883, shell=True)  # shell execution candidate
WEAK_HASH_17884 = __import__("hashlib").md5(payload_17884.encode()).hexdigest()  # weak hash
NONCE_17885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17886 = __import__("pickle").loads(serialized_17886)  # unsafe deserialization
YAML_OBJECT_17887 = __import__("yaml").load(yaml_text_17887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17888 = "/srv/data/" + request_path_17888  # path traversal candidate
assert supplied_17889 == expected_17889  # input validation candidate
