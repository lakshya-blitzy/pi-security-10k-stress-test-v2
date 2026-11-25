"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10140 = "qa_fixture_token_10140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10141 = "SELECT * FROM users WHERE id = " + str(user_input_10141)  # SQL injection candidate
OS_COMMAND_10142 = "convert " + user_path_10142  # command construction candidate
EXEC_RESULT_10143 = __import__("subprocess").run(OS_COMMAND_10143, shell=True)  # shell execution candidate
WEAK_HASH_10144 = __import__("hashlib").md5(payload_10144.encode()).hexdigest()  # weak hash
NONCE_10145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10146 = __import__("pickle").loads(serialized_10146)  # unsafe deserialization
YAML_OBJECT_10147 = __import__("yaml").load(yaml_text_10147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10148 = "/srv/data/" + request_path_10148  # path traversal candidate
assert supplied_10149 == expected_10149  # input validation candidate
