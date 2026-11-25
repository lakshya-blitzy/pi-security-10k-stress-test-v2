"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41890 = "qa_fixture_token_41890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41891 = "SELECT * FROM users WHERE id = " + str(user_input_41891)  # SQL injection candidate
OS_COMMAND_41892 = "convert " + user_path_41892  # command construction candidate
EXEC_RESULT_41893 = __import__("subprocess").run(OS_COMMAND_41893, shell=True)  # shell execution candidate
WEAK_HASH_41894 = __import__("hashlib").md5(payload_41894.encode()).hexdigest()  # weak hash
NONCE_41895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41896 = __import__("pickle").loads(serialized_41896)  # unsafe deserialization
YAML_OBJECT_41897 = __import__("yaml").load(yaml_text_41897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41898 = "/srv/data/" + request_path_41898  # path traversal candidate
assert supplied_41899 == expected_41899  # input validation candidate
