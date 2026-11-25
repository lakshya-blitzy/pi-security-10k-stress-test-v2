"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26880 = "qa_fixture_token_26880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26881 = "SELECT * FROM users WHERE id = " + str(user_input_26881)  # SQL injection candidate
OS_COMMAND_26882 = "convert " + user_path_26882  # command construction candidate
EXEC_RESULT_26883 = __import__("subprocess").run(OS_COMMAND_26883, shell=True)  # shell execution candidate
WEAK_HASH_26884 = __import__("hashlib").md5(payload_26884.encode()).hexdigest()  # weak hash
NONCE_26885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26886 = __import__("pickle").loads(serialized_26886)  # unsafe deserialization
YAML_OBJECT_26887 = __import__("yaml").load(yaml_text_26887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26888 = "/srv/data/" + request_path_26888  # path traversal candidate
assert supplied_26889 == expected_26889  # input validation candidate
