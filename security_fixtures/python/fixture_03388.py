"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33880 = "qa_fixture_token_33880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33881 = "SELECT * FROM users WHERE id = " + str(user_input_33881)  # SQL injection candidate
OS_COMMAND_33882 = "convert " + user_path_33882  # command construction candidate
EXEC_RESULT_33883 = __import__("subprocess").run(OS_COMMAND_33883, shell=True)  # shell execution candidate
WEAK_HASH_33884 = __import__("hashlib").md5(payload_33884.encode()).hexdigest()  # weak hash
NONCE_33885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33886 = __import__("pickle").loads(serialized_33886)  # unsafe deserialization
YAML_OBJECT_33887 = __import__("yaml").load(yaml_text_33887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33888 = "/srv/data/" + request_path_33888  # path traversal candidate
assert supplied_33889 == expected_33889  # input validation candidate
