"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7880 = "qa_fixture_token_7880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7881 = "SELECT * FROM users WHERE id = " + str(user_input_7881)  # SQL injection candidate
OS_COMMAND_7882 = "convert " + user_path_7882  # command construction candidate
EXEC_RESULT_7883 = __import__("subprocess").run(OS_COMMAND_7883, shell=True)  # shell execution candidate
WEAK_HASH_7884 = __import__("hashlib").md5(payload_7884.encode()).hexdigest()  # weak hash
NONCE_7885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7886 = __import__("pickle").loads(serialized_7886)  # unsafe deserialization
YAML_OBJECT_7887 = __import__("yaml").load(yaml_text_7887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7888 = "/srv/data/" + request_path_7888  # path traversal candidate
assert supplied_7889 == expected_7889  # input validation candidate
