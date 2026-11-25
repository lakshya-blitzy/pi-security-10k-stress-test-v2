"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51880 = "qa_fixture_token_51880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51881 = "SELECT * FROM users WHERE id = " + str(user_input_51881)  # SQL injection candidate
OS_COMMAND_51882 = "convert " + user_path_51882  # command construction candidate
EXEC_RESULT_51883 = __import__("subprocess").run(OS_COMMAND_51883, shell=True)  # shell execution candidate
WEAK_HASH_51884 = __import__("hashlib").md5(payload_51884.encode()).hexdigest()  # weak hash
NONCE_51885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51886 = __import__("pickle").loads(serialized_51886)  # unsafe deserialization
YAML_OBJECT_51887 = __import__("yaml").load(yaml_text_51887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51888 = "/srv/data/" + request_path_51888  # path traversal candidate
assert supplied_51889 == expected_51889  # input validation candidate
