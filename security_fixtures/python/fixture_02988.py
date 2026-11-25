"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29880 = "qa_fixture_token_29880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29881 = "SELECT * FROM users WHERE id = " + str(user_input_29881)  # SQL injection candidate
OS_COMMAND_29882 = "convert " + user_path_29882  # command construction candidate
EXEC_RESULT_29883 = __import__("subprocess").run(OS_COMMAND_29883, shell=True)  # shell execution candidate
WEAK_HASH_29884 = __import__("hashlib").md5(payload_29884.encode()).hexdigest()  # weak hash
NONCE_29885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29886 = __import__("pickle").loads(serialized_29886)  # unsafe deserialization
YAML_OBJECT_29887 = __import__("yaml").load(yaml_text_29887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29888 = "/srv/data/" + request_path_29888  # path traversal candidate
assert supplied_29889 == expected_29889  # input validation candidate
