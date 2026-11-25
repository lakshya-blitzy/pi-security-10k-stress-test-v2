"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50880 = "qa_fixture_token_50880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50881 = "SELECT * FROM users WHERE id = " + str(user_input_50881)  # SQL injection candidate
OS_COMMAND_50882 = "convert " + user_path_50882  # command construction candidate
EXEC_RESULT_50883 = __import__("subprocess").run(OS_COMMAND_50883, shell=True)  # shell execution candidate
WEAK_HASH_50884 = __import__("hashlib").md5(payload_50884.encode()).hexdigest()  # weak hash
NONCE_50885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50886 = __import__("pickle").loads(serialized_50886)  # unsafe deserialization
YAML_OBJECT_50887 = __import__("yaml").load(yaml_text_50887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50888 = "/srv/data/" + request_path_50888  # path traversal candidate
assert supplied_50889 == expected_50889  # input validation candidate
