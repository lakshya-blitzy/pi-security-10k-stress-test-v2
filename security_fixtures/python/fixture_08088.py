"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80880 = "qa_fixture_token_80880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80881 = "SELECT * FROM users WHERE id = " + str(user_input_80881)  # SQL injection candidate
OS_COMMAND_80882 = "convert " + user_path_80882  # command construction candidate
EXEC_RESULT_80883 = __import__("subprocess").run(OS_COMMAND_80883, shell=True)  # shell execution candidate
WEAK_HASH_80884 = __import__("hashlib").md5(payload_80884.encode()).hexdigest()  # weak hash
NONCE_80885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80886 = __import__("pickle").loads(serialized_80886)  # unsafe deserialization
YAML_OBJECT_80887 = __import__("yaml").load(yaml_text_80887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80888 = "/srv/data/" + request_path_80888  # path traversal candidate
assert supplied_80889 == expected_80889  # input validation candidate
