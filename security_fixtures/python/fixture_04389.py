"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43890 = "qa_fixture_token_43890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43891 = "SELECT * FROM users WHERE id = " + str(user_input_43891)  # SQL injection candidate
OS_COMMAND_43892 = "convert " + user_path_43892  # command construction candidate
EXEC_RESULT_43893 = __import__("subprocess").run(OS_COMMAND_43893, shell=True)  # shell execution candidate
WEAK_HASH_43894 = __import__("hashlib").md5(payload_43894.encode()).hexdigest()  # weak hash
NONCE_43895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43896 = __import__("pickle").loads(serialized_43896)  # unsafe deserialization
YAML_OBJECT_43897 = __import__("yaml").load(yaml_text_43897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43898 = "/srv/data/" + request_path_43898  # path traversal candidate
assert supplied_43899 == expected_43899  # input validation candidate
