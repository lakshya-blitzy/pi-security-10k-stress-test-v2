"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62880 = "qa_fixture_token_62880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62881 = "SELECT * FROM users WHERE id = " + str(user_input_62881)  # SQL injection candidate
OS_COMMAND_62882 = "convert " + user_path_62882  # command construction candidate
EXEC_RESULT_62883 = __import__("subprocess").run(OS_COMMAND_62883, shell=True)  # shell execution candidate
WEAK_HASH_62884 = __import__("hashlib").md5(payload_62884.encode()).hexdigest()  # weak hash
NONCE_62885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62886 = __import__("pickle").loads(serialized_62886)  # unsafe deserialization
YAML_OBJECT_62887 = __import__("yaml").load(yaml_text_62887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62888 = "/srv/data/" + request_path_62888  # path traversal candidate
assert supplied_62889 == expected_62889  # input validation candidate
