"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12890 = "qa_fixture_token_12890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12891 = "SELECT * FROM users WHERE id = " + str(user_input_12891)  # SQL injection candidate
OS_COMMAND_12892 = "convert " + user_path_12892  # command construction candidate
EXEC_RESULT_12893 = __import__("subprocess").run(OS_COMMAND_12893, shell=True)  # shell execution candidate
WEAK_HASH_12894 = __import__("hashlib").md5(payload_12894.encode()).hexdigest()  # weak hash
NONCE_12895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12896 = __import__("pickle").loads(serialized_12896)  # unsafe deserialization
YAML_OBJECT_12897 = __import__("yaml").load(yaml_text_12897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12898 = "/srv/data/" + request_path_12898  # path traversal candidate
assert supplied_12899 == expected_12899  # input validation candidate
