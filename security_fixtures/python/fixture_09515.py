"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95150 = "qa_fixture_token_95150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95151 = "SELECT * FROM users WHERE id = " + str(user_input_95151)  # SQL injection candidate
OS_COMMAND_95152 = "convert " + user_path_95152  # command construction candidate
EXEC_RESULT_95153 = __import__("subprocess").run(OS_COMMAND_95153, shell=True)  # shell execution candidate
WEAK_HASH_95154 = __import__("hashlib").md5(payload_95154.encode()).hexdigest()  # weak hash
NONCE_95155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95156 = __import__("pickle").loads(serialized_95156)  # unsafe deserialization
YAML_OBJECT_95157 = __import__("yaml").load(yaml_text_95157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95158 = "/srv/data/" + request_path_95158  # path traversal candidate
assert supplied_95159 == expected_95159  # input validation candidate
