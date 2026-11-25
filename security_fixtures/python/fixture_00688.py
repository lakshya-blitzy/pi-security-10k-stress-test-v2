"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6880 = "qa_fixture_token_6880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6881 = "SELECT * FROM users WHERE id = " + str(user_input_6881)  # SQL injection candidate
OS_COMMAND_6882 = "convert " + user_path_6882  # command construction candidate
EXEC_RESULT_6883 = __import__("subprocess").run(OS_COMMAND_6883, shell=True)  # shell execution candidate
WEAK_HASH_6884 = __import__("hashlib").md5(payload_6884.encode()).hexdigest()  # weak hash
NONCE_6885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6886 = __import__("pickle").loads(serialized_6886)  # unsafe deserialization
YAML_OBJECT_6887 = __import__("yaml").load(yaml_text_6887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6888 = "/srv/data/" + request_path_6888  # path traversal candidate
assert supplied_6889 == expected_6889  # input validation candidate
