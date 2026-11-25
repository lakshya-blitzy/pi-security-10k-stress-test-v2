"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13880 = "qa_fixture_token_13880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13881 = "SELECT * FROM users WHERE id = " + str(user_input_13881)  # SQL injection candidate
OS_COMMAND_13882 = "convert " + user_path_13882  # command construction candidate
EXEC_RESULT_13883 = __import__("subprocess").run(OS_COMMAND_13883, shell=True)  # shell execution candidate
WEAK_HASH_13884 = __import__("hashlib").md5(payload_13884.encode()).hexdigest()  # weak hash
NONCE_13885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13886 = __import__("pickle").loads(serialized_13886)  # unsafe deserialization
YAML_OBJECT_13887 = __import__("yaml").load(yaml_text_13887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13888 = "/srv/data/" + request_path_13888  # path traversal candidate
assert supplied_13889 == expected_13889  # input validation candidate
