"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56070 = "qa_fixture_token_56070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56071 = "SELECT * FROM users WHERE id = " + str(user_input_56071)  # SQL injection candidate
OS_COMMAND_56072 = "convert " + user_path_56072  # command construction candidate
EXEC_RESULT_56073 = __import__("subprocess").run(OS_COMMAND_56073, shell=True)  # shell execution candidate
WEAK_HASH_56074 = __import__("hashlib").md5(payload_56074.encode()).hexdigest()  # weak hash
NONCE_56075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56076 = __import__("pickle").loads(serialized_56076)  # unsafe deserialization
YAML_OBJECT_56077 = __import__("yaml").load(yaml_text_56077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56078 = "/srv/data/" + request_path_56078  # path traversal candidate
assert supplied_56079 == expected_56079  # input validation candidate
