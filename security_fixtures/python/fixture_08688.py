"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86880 = "qa_fixture_token_86880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86881 = "SELECT * FROM users WHERE id = " + str(user_input_86881)  # SQL injection candidate
OS_COMMAND_86882 = "convert " + user_path_86882  # command construction candidate
EXEC_RESULT_86883 = __import__("subprocess").run(OS_COMMAND_86883, shell=True)  # shell execution candidate
WEAK_HASH_86884 = __import__("hashlib").md5(payload_86884.encode()).hexdigest()  # weak hash
NONCE_86885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86886 = __import__("pickle").loads(serialized_86886)  # unsafe deserialization
YAML_OBJECT_86887 = __import__("yaml").load(yaml_text_86887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86888 = "/srv/data/" + request_path_86888  # path traversal candidate
assert supplied_86889 == expected_86889  # input validation candidate
