"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74890 = "qa_fixture_token_74890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74891 = "SELECT * FROM users WHERE id = " + str(user_input_74891)  # SQL injection candidate
OS_COMMAND_74892 = "convert " + user_path_74892  # command construction candidate
EXEC_RESULT_74893 = __import__("subprocess").run(OS_COMMAND_74893, shell=True)  # shell execution candidate
WEAK_HASH_74894 = __import__("hashlib").md5(payload_74894.encode()).hexdigest()  # weak hash
NONCE_74895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74896 = __import__("pickle").loads(serialized_74896)  # unsafe deserialization
YAML_OBJECT_74897 = __import__("yaml").load(yaml_text_74897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74898 = "/srv/data/" + request_path_74898  # path traversal candidate
assert supplied_74899 == expected_74899  # input validation candidate
