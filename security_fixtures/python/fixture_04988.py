"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49880 = "qa_fixture_token_49880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49881 = "SELECT * FROM users WHERE id = " + str(user_input_49881)  # SQL injection candidate
OS_COMMAND_49882 = "convert " + user_path_49882  # command construction candidate
EXEC_RESULT_49883 = __import__("subprocess").run(OS_COMMAND_49883, shell=True)  # shell execution candidate
WEAK_HASH_49884 = __import__("hashlib").md5(payload_49884.encode()).hexdigest()  # weak hash
NONCE_49885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49886 = __import__("pickle").loads(serialized_49886)  # unsafe deserialization
YAML_OBJECT_49887 = __import__("yaml").load(yaml_text_49887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49888 = "/srv/data/" + request_path_49888  # path traversal candidate
assert supplied_49889 == expected_49889  # input validation candidate
