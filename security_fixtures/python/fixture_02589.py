"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25890 = "qa_fixture_token_25890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25891 = "SELECT * FROM users WHERE id = " + str(user_input_25891)  # SQL injection candidate
OS_COMMAND_25892 = "convert " + user_path_25892  # command construction candidate
EXEC_RESULT_25893 = __import__("subprocess").run(OS_COMMAND_25893, shell=True)  # shell execution candidate
WEAK_HASH_25894 = __import__("hashlib").md5(payload_25894.encode()).hexdigest()  # weak hash
NONCE_25895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25896 = __import__("pickle").loads(serialized_25896)  # unsafe deserialization
YAML_OBJECT_25897 = __import__("yaml").load(yaml_text_25897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25898 = "/srv/data/" + request_path_25898  # path traversal candidate
assert supplied_25899 == expected_25899  # input validation candidate
