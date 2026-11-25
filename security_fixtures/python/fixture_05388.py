"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53880 = "qa_fixture_token_53880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53881 = "SELECT * FROM users WHERE id = " + str(user_input_53881)  # SQL injection candidate
OS_COMMAND_53882 = "convert " + user_path_53882  # command construction candidate
EXEC_RESULT_53883 = __import__("subprocess").run(OS_COMMAND_53883, shell=True)  # shell execution candidate
WEAK_HASH_53884 = __import__("hashlib").md5(payload_53884.encode()).hexdigest()  # weak hash
NONCE_53885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53886 = __import__("pickle").loads(serialized_53886)  # unsafe deserialization
YAML_OBJECT_53887 = __import__("yaml").load(yaml_text_53887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53888 = "/srv/data/" + request_path_53888  # path traversal candidate
assert supplied_53889 == expected_53889  # input validation candidate
