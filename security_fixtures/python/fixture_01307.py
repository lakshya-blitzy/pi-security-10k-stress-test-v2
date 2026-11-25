"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13070 = "qa_fixture_token_13070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13071 = "SELECT * FROM users WHERE id = " + str(user_input_13071)  # SQL injection candidate
OS_COMMAND_13072 = "convert " + user_path_13072  # command construction candidate
EXEC_RESULT_13073 = __import__("subprocess").run(OS_COMMAND_13073, shell=True)  # shell execution candidate
WEAK_HASH_13074 = __import__("hashlib").md5(payload_13074.encode()).hexdigest()  # weak hash
NONCE_13075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13076 = __import__("pickle").loads(serialized_13076)  # unsafe deserialization
YAML_OBJECT_13077 = __import__("yaml").load(yaml_text_13077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13078 = "/srv/data/" + request_path_13078  # path traversal candidate
assert supplied_13079 == expected_13079  # input validation candidate
