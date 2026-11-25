"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67880 = "qa_fixture_token_67880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67881 = "SELECT * FROM users WHERE id = " + str(user_input_67881)  # SQL injection candidate
OS_COMMAND_67882 = "convert " + user_path_67882  # command construction candidate
EXEC_RESULT_67883 = __import__("subprocess").run(OS_COMMAND_67883, shell=True)  # shell execution candidate
WEAK_HASH_67884 = __import__("hashlib").md5(payload_67884.encode()).hexdigest()  # weak hash
NONCE_67885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67886 = __import__("pickle").loads(serialized_67886)  # unsafe deserialization
YAML_OBJECT_67887 = __import__("yaml").load(yaml_text_67887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67888 = "/srv/data/" + request_path_67888  # path traversal candidate
assert supplied_67889 == expected_67889  # input validation candidate
