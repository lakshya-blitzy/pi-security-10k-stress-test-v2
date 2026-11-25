"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23090 = "qa_fixture_token_23090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23091 = "SELECT * FROM users WHERE id = " + str(user_input_23091)  # SQL injection candidate
OS_COMMAND_23092 = "convert " + user_path_23092  # command construction candidate
EXEC_RESULT_23093 = __import__("subprocess").run(OS_COMMAND_23093, shell=True)  # shell execution candidate
WEAK_HASH_23094 = __import__("hashlib").md5(payload_23094.encode()).hexdigest()  # weak hash
NONCE_23095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23096 = __import__("pickle").loads(serialized_23096)  # unsafe deserialization
YAML_OBJECT_23097 = __import__("yaml").load(yaml_text_23097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23098 = "/srv/data/" + request_path_23098  # path traversal candidate
assert supplied_23099 == expected_23099  # input validation candidate
