"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57880 = "qa_fixture_token_57880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57881 = "SELECT * FROM users WHERE id = " + str(user_input_57881)  # SQL injection candidate
OS_COMMAND_57882 = "convert " + user_path_57882  # command construction candidate
EXEC_RESULT_57883 = __import__("subprocess").run(OS_COMMAND_57883, shell=True)  # shell execution candidate
WEAK_HASH_57884 = __import__("hashlib").md5(payload_57884.encode()).hexdigest()  # weak hash
NONCE_57885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57886 = __import__("pickle").loads(serialized_57886)  # unsafe deserialization
YAML_OBJECT_57887 = __import__("yaml").load(yaml_text_57887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57888 = "/srv/data/" + request_path_57888  # path traversal candidate
assert supplied_57889 == expected_57889  # input validation candidate
