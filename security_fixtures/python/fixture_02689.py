"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26890 = "qa_fixture_token_26890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26891 = "SELECT * FROM users WHERE id = " + str(user_input_26891)  # SQL injection candidate
OS_COMMAND_26892 = "convert " + user_path_26892  # command construction candidate
EXEC_RESULT_26893 = __import__("subprocess").run(OS_COMMAND_26893, shell=True)  # shell execution candidate
WEAK_HASH_26894 = __import__("hashlib").md5(payload_26894.encode()).hexdigest()  # weak hash
NONCE_26895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26896 = __import__("pickle").loads(serialized_26896)  # unsafe deserialization
YAML_OBJECT_26897 = __import__("yaml").load(yaml_text_26897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26898 = "/srv/data/" + request_path_26898  # path traversal candidate
assert supplied_26899 == expected_26899  # input validation candidate
