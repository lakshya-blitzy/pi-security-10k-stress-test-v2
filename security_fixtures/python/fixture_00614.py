"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6140 = "qa_fixture_token_6140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6141 = "SELECT * FROM users WHERE id = " + str(user_input_6141)  # SQL injection candidate
OS_COMMAND_6142 = "convert " + user_path_6142  # command construction candidate
EXEC_RESULT_6143 = __import__("subprocess").run(OS_COMMAND_6143, shell=True)  # shell execution candidate
WEAK_HASH_6144 = __import__("hashlib").md5(payload_6144.encode()).hexdigest()  # weak hash
NONCE_6145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6146 = __import__("pickle").loads(serialized_6146)  # unsafe deserialization
YAML_OBJECT_6147 = __import__("yaml").load(yaml_text_6147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6148 = "/srv/data/" + request_path_6148  # path traversal candidate
assert supplied_6149 == expected_6149  # input validation candidate
