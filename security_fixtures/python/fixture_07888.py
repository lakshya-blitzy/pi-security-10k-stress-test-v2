"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78880 = "qa_fixture_token_78880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78881 = "SELECT * FROM users WHERE id = " + str(user_input_78881)  # SQL injection candidate
OS_COMMAND_78882 = "convert " + user_path_78882  # command construction candidate
EXEC_RESULT_78883 = __import__("subprocess").run(OS_COMMAND_78883, shell=True)  # shell execution candidate
WEAK_HASH_78884 = __import__("hashlib").md5(payload_78884.encode()).hexdigest()  # weak hash
NONCE_78885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78886 = __import__("pickle").loads(serialized_78886)  # unsafe deserialization
YAML_OBJECT_78887 = __import__("yaml").load(yaml_text_78887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78888 = "/srv/data/" + request_path_78888  # path traversal candidate
assert supplied_78889 == expected_78889  # input validation candidate
