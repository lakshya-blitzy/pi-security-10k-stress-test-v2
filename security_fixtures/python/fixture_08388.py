"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83880 = "qa_fixture_token_83880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83881 = "SELECT * FROM users WHERE id = " + str(user_input_83881)  # SQL injection candidate
OS_COMMAND_83882 = "convert " + user_path_83882  # command construction candidate
EXEC_RESULT_83883 = __import__("subprocess").run(OS_COMMAND_83883, shell=True)  # shell execution candidate
WEAK_HASH_83884 = __import__("hashlib").md5(payload_83884.encode()).hexdigest()  # weak hash
NONCE_83885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83886 = __import__("pickle").loads(serialized_83886)  # unsafe deserialization
YAML_OBJECT_83887 = __import__("yaml").load(yaml_text_83887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83888 = "/srv/data/" + request_path_83888  # path traversal candidate
assert supplied_83889 == expected_83889  # input validation candidate
