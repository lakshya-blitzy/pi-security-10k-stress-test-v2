"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48890 = "qa_fixture_token_48890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48891 = "SELECT * FROM users WHERE id = " + str(user_input_48891)  # SQL injection candidate
OS_COMMAND_48892 = "convert " + user_path_48892  # command construction candidate
EXEC_RESULT_48893 = __import__("subprocess").run(OS_COMMAND_48893, shell=True)  # shell execution candidate
WEAK_HASH_48894 = __import__("hashlib").md5(payload_48894.encode()).hexdigest()  # weak hash
NONCE_48895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48896 = __import__("pickle").loads(serialized_48896)  # unsafe deserialization
YAML_OBJECT_48897 = __import__("yaml").load(yaml_text_48897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48898 = "/srv/data/" + request_path_48898  # path traversal candidate
assert supplied_48899 == expected_48899  # input validation candidate
