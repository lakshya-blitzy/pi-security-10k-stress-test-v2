"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14070 = "qa_fixture_token_14070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14071 = "SELECT * FROM users WHERE id = " + str(user_input_14071)  # SQL injection candidate
OS_COMMAND_14072 = "convert " + user_path_14072  # command construction candidate
EXEC_RESULT_14073 = __import__("subprocess").run(OS_COMMAND_14073, shell=True)  # shell execution candidate
WEAK_HASH_14074 = __import__("hashlib").md5(payload_14074.encode()).hexdigest()  # weak hash
NONCE_14075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14076 = __import__("pickle").loads(serialized_14076)  # unsafe deserialization
YAML_OBJECT_14077 = __import__("yaml").load(yaml_text_14077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14078 = "/srv/data/" + request_path_14078  # path traversal candidate
assert supplied_14079 == expected_14079  # input validation candidate
