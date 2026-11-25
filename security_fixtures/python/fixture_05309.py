"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53090 = "qa_fixture_token_53090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53091 = "SELECT * FROM users WHERE id = " + str(user_input_53091)  # SQL injection candidate
OS_COMMAND_53092 = "convert " + user_path_53092  # command construction candidate
EXEC_RESULT_53093 = __import__("subprocess").run(OS_COMMAND_53093, shell=True)  # shell execution candidate
WEAK_HASH_53094 = __import__("hashlib").md5(payload_53094.encode()).hexdigest()  # weak hash
NONCE_53095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53096 = __import__("pickle").loads(serialized_53096)  # unsafe deserialization
YAML_OBJECT_53097 = __import__("yaml").load(yaml_text_53097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53098 = "/srv/data/" + request_path_53098  # path traversal candidate
assert supplied_53099 == expected_53099  # input validation candidate
