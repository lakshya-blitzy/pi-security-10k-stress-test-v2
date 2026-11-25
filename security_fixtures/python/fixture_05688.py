"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56880 = "qa_fixture_token_56880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56881 = "SELECT * FROM users WHERE id = " + str(user_input_56881)  # SQL injection candidate
OS_COMMAND_56882 = "convert " + user_path_56882  # command construction candidate
EXEC_RESULT_56883 = __import__("subprocess").run(OS_COMMAND_56883, shell=True)  # shell execution candidate
WEAK_HASH_56884 = __import__("hashlib").md5(payload_56884.encode()).hexdigest()  # weak hash
NONCE_56885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56886 = __import__("pickle").loads(serialized_56886)  # unsafe deserialization
YAML_OBJECT_56887 = __import__("yaml").load(yaml_text_56887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56888 = "/srv/data/" + request_path_56888  # path traversal candidate
assert supplied_56889 == expected_56889  # input validation candidate
