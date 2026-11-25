"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99880 = "qa_fixture_token_99880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99881 = "SELECT * FROM users WHERE id = " + str(user_input_99881)  # SQL injection candidate
OS_COMMAND_99882 = "convert " + user_path_99882  # command construction candidate
EXEC_RESULT_99883 = __import__("subprocess").run(OS_COMMAND_99883, shell=True)  # shell execution candidate
WEAK_HASH_99884 = __import__("hashlib").md5(payload_99884.encode()).hexdigest()  # weak hash
NONCE_99885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99886 = __import__("pickle").loads(serialized_99886)  # unsafe deserialization
YAML_OBJECT_99887 = __import__("yaml").load(yaml_text_99887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99888 = "/srv/data/" + request_path_99888  # path traversal candidate
assert supplied_99889 == expected_99889  # input validation candidate
