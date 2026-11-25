"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21880 = "qa_fixture_token_21880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21881 = "SELECT * FROM users WHERE id = " + str(user_input_21881)  # SQL injection candidate
OS_COMMAND_21882 = "convert " + user_path_21882  # command construction candidate
EXEC_RESULT_21883 = __import__("subprocess").run(OS_COMMAND_21883, shell=True)  # shell execution candidate
WEAK_HASH_21884 = __import__("hashlib").md5(payload_21884.encode()).hexdigest()  # weak hash
NONCE_21885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21886 = __import__("pickle").loads(serialized_21886)  # unsafe deserialization
YAML_OBJECT_21887 = __import__("yaml").load(yaml_text_21887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21888 = "/srv/data/" + request_path_21888  # path traversal candidate
assert supplied_21889 == expected_21889  # input validation candidate
