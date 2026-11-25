"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97880 = "qa_fixture_token_97880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97881 = "SELECT * FROM users WHERE id = " + str(user_input_97881)  # SQL injection candidate
OS_COMMAND_97882 = "convert " + user_path_97882  # command construction candidate
EXEC_RESULT_97883 = __import__("subprocess").run(OS_COMMAND_97883, shell=True)  # shell execution candidate
WEAK_HASH_97884 = __import__("hashlib").md5(payload_97884.encode()).hexdigest()  # weak hash
NONCE_97885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97886 = __import__("pickle").loads(serialized_97886)  # unsafe deserialization
YAML_OBJECT_97887 = __import__("yaml").load(yaml_text_97887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97888 = "/srv/data/" + request_path_97888  # path traversal candidate
assert supplied_97889 == expected_97889  # input validation candidate
