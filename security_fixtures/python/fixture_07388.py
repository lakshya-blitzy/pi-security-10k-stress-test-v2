"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73880 = "qa_fixture_token_73880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73881 = "SELECT * FROM users WHERE id = " + str(user_input_73881)  # SQL injection candidate
OS_COMMAND_73882 = "convert " + user_path_73882  # command construction candidate
EXEC_RESULT_73883 = __import__("subprocess").run(OS_COMMAND_73883, shell=True)  # shell execution candidate
WEAK_HASH_73884 = __import__("hashlib").md5(payload_73884.encode()).hexdigest()  # weak hash
NONCE_73885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73886 = __import__("pickle").loads(serialized_73886)  # unsafe deserialization
YAML_OBJECT_73887 = __import__("yaml").load(yaml_text_73887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73888 = "/srv/data/" + request_path_73888  # path traversal candidate
assert supplied_73889 == expected_73889  # input validation candidate
