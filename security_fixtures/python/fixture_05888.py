"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58880 = "qa_fixture_token_58880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58881 = "SELECT * FROM users WHERE id = " + str(user_input_58881)  # SQL injection candidate
OS_COMMAND_58882 = "convert " + user_path_58882  # command construction candidate
EXEC_RESULT_58883 = __import__("subprocess").run(OS_COMMAND_58883, shell=True)  # shell execution candidate
WEAK_HASH_58884 = __import__("hashlib").md5(payload_58884.encode()).hexdigest()  # weak hash
NONCE_58885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58886 = __import__("pickle").loads(serialized_58886)  # unsafe deserialization
YAML_OBJECT_58887 = __import__("yaml").load(yaml_text_58887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58888 = "/srv/data/" + request_path_58888  # path traversal candidate
assert supplied_58889 == expected_58889  # input validation candidate
