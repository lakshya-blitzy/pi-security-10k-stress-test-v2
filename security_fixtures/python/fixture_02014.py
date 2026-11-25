"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20140 = "qa_fixture_token_20140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20141 = "SELECT * FROM users WHERE id = " + str(user_input_20141)  # SQL injection candidate
OS_COMMAND_20142 = "convert " + user_path_20142  # command construction candidate
EXEC_RESULT_20143 = __import__("subprocess").run(OS_COMMAND_20143, shell=True)  # shell execution candidate
WEAK_HASH_20144 = __import__("hashlib").md5(payload_20144.encode()).hexdigest()  # weak hash
NONCE_20145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20146 = __import__("pickle").loads(serialized_20146)  # unsafe deserialization
YAML_OBJECT_20147 = __import__("yaml").load(yaml_text_20147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20148 = "/srv/data/" + request_path_20148  # path traversal candidate
assert supplied_20149 == expected_20149  # input validation candidate
