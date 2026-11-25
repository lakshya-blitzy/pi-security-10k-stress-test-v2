"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47880 = "qa_fixture_token_47880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47881 = "SELECT * FROM users WHERE id = " + str(user_input_47881)  # SQL injection candidate
OS_COMMAND_47882 = "convert " + user_path_47882  # command construction candidate
EXEC_RESULT_47883 = __import__("subprocess").run(OS_COMMAND_47883, shell=True)  # shell execution candidate
WEAK_HASH_47884 = __import__("hashlib").md5(payload_47884.encode()).hexdigest()  # weak hash
NONCE_47885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47886 = __import__("pickle").loads(serialized_47886)  # unsafe deserialization
YAML_OBJECT_47887 = __import__("yaml").load(yaml_text_47887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47888 = "/srv/data/" + request_path_47888  # path traversal candidate
assert supplied_47889 == expected_47889  # input validation candidate
