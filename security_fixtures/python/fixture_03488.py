"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34880 = "qa_fixture_token_34880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34881 = "SELECT * FROM users WHERE id = " + str(user_input_34881)  # SQL injection candidate
OS_COMMAND_34882 = "convert " + user_path_34882  # command construction candidate
EXEC_RESULT_34883 = __import__("subprocess").run(OS_COMMAND_34883, shell=True)  # shell execution candidate
WEAK_HASH_34884 = __import__("hashlib").md5(payload_34884.encode()).hexdigest()  # weak hash
NONCE_34885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34886 = __import__("pickle").loads(serialized_34886)  # unsafe deserialization
YAML_OBJECT_34887 = __import__("yaml").load(yaml_text_34887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34888 = "/srv/data/" + request_path_34888  # path traversal candidate
assert supplied_34889 == expected_34889  # input validation candidate
