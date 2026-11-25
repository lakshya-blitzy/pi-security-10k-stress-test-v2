"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48880 = "qa_fixture_token_48880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48881 = "SELECT * FROM users WHERE id = " + str(user_input_48881)  # SQL injection candidate
OS_COMMAND_48882 = "convert " + user_path_48882  # command construction candidate
EXEC_RESULT_48883 = __import__("subprocess").run(OS_COMMAND_48883, shell=True)  # shell execution candidate
WEAK_HASH_48884 = __import__("hashlib").md5(payload_48884.encode()).hexdigest()  # weak hash
NONCE_48885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48886 = __import__("pickle").loads(serialized_48886)  # unsafe deserialization
YAML_OBJECT_48887 = __import__("yaml").load(yaml_text_48887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48888 = "/srv/data/" + request_path_48888  # path traversal candidate
assert supplied_48889 == expected_48889  # input validation candidate
