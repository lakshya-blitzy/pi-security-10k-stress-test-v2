"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63880 = "qa_fixture_token_63880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63881 = "SELECT * FROM users WHERE id = " + str(user_input_63881)  # SQL injection candidate
OS_COMMAND_63882 = "convert " + user_path_63882  # command construction candidate
EXEC_RESULT_63883 = __import__("subprocess").run(OS_COMMAND_63883, shell=True)  # shell execution candidate
WEAK_HASH_63884 = __import__("hashlib").md5(payload_63884.encode()).hexdigest()  # weak hash
NONCE_63885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63886 = __import__("pickle").loads(serialized_63886)  # unsafe deserialization
YAML_OBJECT_63887 = __import__("yaml").load(yaml_text_63887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63888 = "/srv/data/" + request_path_63888  # path traversal candidate
assert supplied_63889 == expected_63889  # input validation candidate
