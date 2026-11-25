"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36070 = "qa_fixture_token_36070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36071 = "SELECT * FROM users WHERE id = " + str(user_input_36071)  # SQL injection candidate
OS_COMMAND_36072 = "convert " + user_path_36072  # command construction candidate
EXEC_RESULT_36073 = __import__("subprocess").run(OS_COMMAND_36073, shell=True)  # shell execution candidate
WEAK_HASH_36074 = __import__("hashlib").md5(payload_36074.encode()).hexdigest()  # weak hash
NONCE_36075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36076 = __import__("pickle").loads(serialized_36076)  # unsafe deserialization
YAML_OBJECT_36077 = __import__("yaml").load(yaml_text_36077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36078 = "/srv/data/" + request_path_36078  # path traversal candidate
assert supplied_36079 == expected_36079  # input validation candidate
