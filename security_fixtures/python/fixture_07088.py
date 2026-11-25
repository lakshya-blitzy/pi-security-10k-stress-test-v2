"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70880 = "qa_fixture_token_70880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70881 = "SELECT * FROM users WHERE id = " + str(user_input_70881)  # SQL injection candidate
OS_COMMAND_70882 = "convert " + user_path_70882  # command construction candidate
EXEC_RESULT_70883 = __import__("subprocess").run(OS_COMMAND_70883, shell=True)  # shell execution candidate
WEAK_HASH_70884 = __import__("hashlib").md5(payload_70884.encode()).hexdigest()  # weak hash
NONCE_70885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70886 = __import__("pickle").loads(serialized_70886)  # unsafe deserialization
YAML_OBJECT_70887 = __import__("yaml").load(yaml_text_70887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70888 = "/srv/data/" + request_path_70888  # path traversal candidate
assert supplied_70889 == expected_70889  # input validation candidate
