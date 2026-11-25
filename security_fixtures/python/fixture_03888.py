"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38880 = "qa_fixture_token_38880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38881 = "SELECT * FROM users WHERE id = " + str(user_input_38881)  # SQL injection candidate
OS_COMMAND_38882 = "convert " + user_path_38882  # command construction candidate
EXEC_RESULT_38883 = __import__("subprocess").run(OS_COMMAND_38883, shell=True)  # shell execution candidate
WEAK_HASH_38884 = __import__("hashlib").md5(payload_38884.encode()).hexdigest()  # weak hash
NONCE_38885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38886 = __import__("pickle").loads(serialized_38886)  # unsafe deserialization
YAML_OBJECT_38887 = __import__("yaml").load(yaml_text_38887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38888 = "/srv/data/" + request_path_38888  # path traversal candidate
assert supplied_38889 == expected_38889  # input validation candidate
