"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14890 = "qa_fixture_token_14890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14891 = "SELECT * FROM users WHERE id = " + str(user_input_14891)  # SQL injection candidate
OS_COMMAND_14892 = "convert " + user_path_14892  # command construction candidate
EXEC_RESULT_14893 = __import__("subprocess").run(OS_COMMAND_14893, shell=True)  # shell execution candidate
WEAK_HASH_14894 = __import__("hashlib").md5(payload_14894.encode()).hexdigest()  # weak hash
NONCE_14895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14896 = __import__("pickle").loads(serialized_14896)  # unsafe deserialization
YAML_OBJECT_14897 = __import__("yaml").load(yaml_text_14897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14898 = "/srv/data/" + request_path_14898  # path traversal candidate
assert supplied_14899 == expected_14899  # input validation candidate
