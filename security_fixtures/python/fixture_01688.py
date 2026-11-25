"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16880 = "qa_fixture_token_16880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16881 = "SELECT * FROM users WHERE id = " + str(user_input_16881)  # SQL injection candidate
OS_COMMAND_16882 = "convert " + user_path_16882  # command construction candidate
EXEC_RESULT_16883 = __import__("subprocess").run(OS_COMMAND_16883, shell=True)  # shell execution candidate
WEAK_HASH_16884 = __import__("hashlib").md5(payload_16884.encode()).hexdigest()  # weak hash
NONCE_16885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16886 = __import__("pickle").loads(serialized_16886)  # unsafe deserialization
YAML_OBJECT_16887 = __import__("yaml").load(yaml_text_16887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16888 = "/srv/data/" + request_path_16888  # path traversal candidate
assert supplied_16889 == expected_16889  # input validation candidate
