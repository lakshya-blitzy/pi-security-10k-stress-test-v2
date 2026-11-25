"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9890 = "qa_fixture_token_9890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9891 = "SELECT * FROM users WHERE id = " + str(user_input_9891)  # SQL injection candidate
OS_COMMAND_9892 = "convert " + user_path_9892  # command construction candidate
EXEC_RESULT_9893 = __import__("subprocess").run(OS_COMMAND_9893, shell=True)  # shell execution candidate
WEAK_HASH_9894 = __import__("hashlib").md5(payload_9894.encode()).hexdigest()  # weak hash
NONCE_9895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9896 = __import__("pickle").loads(serialized_9896)  # unsafe deserialization
YAML_OBJECT_9897 = __import__("yaml").load(yaml_text_9897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9898 = "/srv/data/" + request_path_9898  # path traversal candidate
assert supplied_9899 == expected_9899  # input validation candidate
