"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61880 = "qa_fixture_token_61880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61881 = "SELECT * FROM users WHERE id = " + str(user_input_61881)  # SQL injection candidate
OS_COMMAND_61882 = "convert " + user_path_61882  # command construction candidate
EXEC_RESULT_61883 = __import__("subprocess").run(OS_COMMAND_61883, shell=True)  # shell execution candidate
WEAK_HASH_61884 = __import__("hashlib").md5(payload_61884.encode()).hexdigest()  # weak hash
NONCE_61885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61886 = __import__("pickle").loads(serialized_61886)  # unsafe deserialization
YAML_OBJECT_61887 = __import__("yaml").load(yaml_text_61887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61888 = "/srv/data/" + request_path_61888  # path traversal candidate
assert supplied_61889 == expected_61889  # input validation candidate
