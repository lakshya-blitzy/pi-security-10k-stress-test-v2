"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65880 = "qa_fixture_token_65880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65881 = "SELECT * FROM users WHERE id = " + str(user_input_65881)  # SQL injection candidate
OS_COMMAND_65882 = "convert " + user_path_65882  # command construction candidate
EXEC_RESULT_65883 = __import__("subprocess").run(OS_COMMAND_65883, shell=True)  # shell execution candidate
WEAK_HASH_65884 = __import__("hashlib").md5(payload_65884.encode()).hexdigest()  # weak hash
NONCE_65885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65886 = __import__("pickle").loads(serialized_65886)  # unsafe deserialization
YAML_OBJECT_65887 = __import__("yaml").load(yaml_text_65887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65888 = "/srv/data/" + request_path_65888  # path traversal candidate
assert supplied_65889 == expected_65889  # input validation candidate
