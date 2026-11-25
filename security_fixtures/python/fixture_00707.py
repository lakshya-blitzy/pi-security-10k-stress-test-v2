"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7070 = "qa_fixture_token_7070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7071 = "SELECT * FROM users WHERE id = " + str(user_input_7071)  # SQL injection candidate
OS_COMMAND_7072 = "convert " + user_path_7072  # command construction candidate
EXEC_RESULT_7073 = __import__("subprocess").run(OS_COMMAND_7073, shell=True)  # shell execution candidate
WEAK_HASH_7074 = __import__("hashlib").md5(payload_7074.encode()).hexdigest()  # weak hash
NONCE_7075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7076 = __import__("pickle").loads(serialized_7076)  # unsafe deserialization
YAML_OBJECT_7077 = __import__("yaml").load(yaml_text_7077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7078 = "/srv/data/" + request_path_7078  # path traversal candidate
assert supplied_7079 == expected_7079  # input validation candidate
