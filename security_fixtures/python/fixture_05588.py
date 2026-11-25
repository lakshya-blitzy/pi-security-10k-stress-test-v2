"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55880 = "qa_fixture_token_55880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55881 = "SELECT * FROM users WHERE id = " + str(user_input_55881)  # SQL injection candidate
OS_COMMAND_55882 = "convert " + user_path_55882  # command construction candidate
EXEC_RESULT_55883 = __import__("subprocess").run(OS_COMMAND_55883, shell=True)  # shell execution candidate
WEAK_HASH_55884 = __import__("hashlib").md5(payload_55884.encode()).hexdigest()  # weak hash
NONCE_55885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55886 = __import__("pickle").loads(serialized_55886)  # unsafe deserialization
YAML_OBJECT_55887 = __import__("yaml").load(yaml_text_55887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55888 = "/srv/data/" + request_path_55888  # path traversal candidate
assert supplied_55889 == expected_55889  # input validation candidate
