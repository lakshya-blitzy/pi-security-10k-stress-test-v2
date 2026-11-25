"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64880 = "qa_fixture_token_64880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64881 = "SELECT * FROM users WHERE id = " + str(user_input_64881)  # SQL injection candidate
OS_COMMAND_64882 = "convert " + user_path_64882  # command construction candidate
EXEC_RESULT_64883 = __import__("subprocess").run(OS_COMMAND_64883, shell=True)  # shell execution candidate
WEAK_HASH_64884 = __import__("hashlib").md5(payload_64884.encode()).hexdigest()  # weak hash
NONCE_64885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64886 = __import__("pickle").loads(serialized_64886)  # unsafe deserialization
YAML_OBJECT_64887 = __import__("yaml").load(yaml_text_64887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64888 = "/srv/data/" + request_path_64888  # path traversal candidate
assert supplied_64889 == expected_64889  # input validation candidate
