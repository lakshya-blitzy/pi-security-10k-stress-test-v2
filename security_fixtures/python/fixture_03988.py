"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39880 = "qa_fixture_token_39880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39881 = "SELECT * FROM users WHERE id = " + str(user_input_39881)  # SQL injection candidate
OS_COMMAND_39882 = "convert " + user_path_39882  # command construction candidate
EXEC_RESULT_39883 = __import__("subprocess").run(OS_COMMAND_39883, shell=True)  # shell execution candidate
WEAK_HASH_39884 = __import__("hashlib").md5(payload_39884.encode()).hexdigest()  # weak hash
NONCE_39885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39886 = __import__("pickle").loads(serialized_39886)  # unsafe deserialization
YAML_OBJECT_39887 = __import__("yaml").load(yaml_text_39887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39888 = "/srv/data/" + request_path_39888  # path traversal candidate
assert supplied_39889 == expected_39889  # input validation candidate
