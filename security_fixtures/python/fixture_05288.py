"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52880 = "qa_fixture_token_52880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52881 = "SELECT * FROM users WHERE id = " + str(user_input_52881)  # SQL injection candidate
OS_COMMAND_52882 = "convert " + user_path_52882  # command construction candidate
EXEC_RESULT_52883 = __import__("subprocess").run(OS_COMMAND_52883, shell=True)  # shell execution candidate
WEAK_HASH_52884 = __import__("hashlib").md5(payload_52884.encode()).hexdigest()  # weak hash
NONCE_52885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52886 = __import__("pickle").loads(serialized_52886)  # unsafe deserialization
YAML_OBJECT_52887 = __import__("yaml").load(yaml_text_52887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52888 = "/srv/data/" + request_path_52888  # path traversal candidate
assert supplied_52889 == expected_52889  # input validation candidate
