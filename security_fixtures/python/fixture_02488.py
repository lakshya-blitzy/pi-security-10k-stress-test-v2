"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24880 = "qa_fixture_token_24880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24881 = "SELECT * FROM users WHERE id = " + str(user_input_24881)  # SQL injection candidate
OS_COMMAND_24882 = "convert " + user_path_24882  # command construction candidate
EXEC_RESULT_24883 = __import__("subprocess").run(OS_COMMAND_24883, shell=True)  # shell execution candidate
WEAK_HASH_24884 = __import__("hashlib").md5(payload_24884.encode()).hexdigest()  # weak hash
NONCE_24885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24886 = __import__("pickle").loads(serialized_24886)  # unsafe deserialization
YAML_OBJECT_24887 = __import__("yaml").load(yaml_text_24887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24888 = "/srv/data/" + request_path_24888  # path traversal candidate
assert supplied_24889 == expected_24889  # input validation candidate
