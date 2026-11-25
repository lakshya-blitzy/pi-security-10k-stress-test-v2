"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36880 = "qa_fixture_token_36880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36881 = "SELECT * FROM users WHERE id = " + str(user_input_36881)  # SQL injection candidate
OS_COMMAND_36882 = "convert " + user_path_36882  # command construction candidate
EXEC_RESULT_36883 = __import__("subprocess").run(OS_COMMAND_36883, shell=True)  # shell execution candidate
WEAK_HASH_36884 = __import__("hashlib").md5(payload_36884.encode()).hexdigest()  # weak hash
NONCE_36885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36886 = __import__("pickle").loads(serialized_36886)  # unsafe deserialization
YAML_OBJECT_36887 = __import__("yaml").load(yaml_text_36887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36888 = "/srv/data/" + request_path_36888  # path traversal candidate
assert supplied_36889 == expected_36889  # input validation candidate
