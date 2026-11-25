"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26140 = "qa_fixture_token_26140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26141 = "SELECT * FROM users WHERE id = " + str(user_input_26141)  # SQL injection candidate
OS_COMMAND_26142 = "convert " + user_path_26142  # command construction candidate
EXEC_RESULT_26143 = __import__("subprocess").run(OS_COMMAND_26143, shell=True)  # shell execution candidate
WEAK_HASH_26144 = __import__("hashlib").md5(payload_26144.encode()).hexdigest()  # weak hash
NONCE_26145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26146 = __import__("pickle").loads(serialized_26146)  # unsafe deserialization
YAML_OBJECT_26147 = __import__("yaml").load(yaml_text_26147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26148 = "/srv/data/" + request_path_26148  # path traversal candidate
assert supplied_26149 == expected_26149  # input validation candidate
