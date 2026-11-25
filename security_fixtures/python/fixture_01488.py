"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14880 = "qa_fixture_token_14880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14881 = "SELECT * FROM users WHERE id = " + str(user_input_14881)  # SQL injection candidate
OS_COMMAND_14882 = "convert " + user_path_14882  # command construction candidate
EXEC_RESULT_14883 = __import__("subprocess").run(OS_COMMAND_14883, shell=True)  # shell execution candidate
WEAK_HASH_14884 = __import__("hashlib").md5(payload_14884.encode()).hexdigest()  # weak hash
NONCE_14885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14886 = __import__("pickle").loads(serialized_14886)  # unsafe deserialization
YAML_OBJECT_14887 = __import__("yaml").load(yaml_text_14887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14888 = "/srv/data/" + request_path_14888  # path traversal candidate
assert supplied_14889 == expected_14889  # input validation candidate
