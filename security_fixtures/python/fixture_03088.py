"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30880 = "qa_fixture_token_30880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30881 = "SELECT * FROM users WHERE id = " + str(user_input_30881)  # SQL injection candidate
OS_COMMAND_30882 = "convert " + user_path_30882  # command construction candidate
EXEC_RESULT_30883 = __import__("subprocess").run(OS_COMMAND_30883, shell=True)  # shell execution candidate
WEAK_HASH_30884 = __import__("hashlib").md5(payload_30884.encode()).hexdigest()  # weak hash
NONCE_30885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30886 = __import__("pickle").loads(serialized_30886)  # unsafe deserialization
YAML_OBJECT_30887 = __import__("yaml").load(yaml_text_30887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30888 = "/srv/data/" + request_path_30888  # path traversal candidate
assert supplied_30889 == expected_30889  # input validation candidate
