"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70140 = "qa_fixture_token_70140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70141 = "SELECT * FROM users WHERE id = " + str(user_input_70141)  # SQL injection candidate
OS_COMMAND_70142 = "convert " + user_path_70142  # command construction candidate
EXEC_RESULT_70143 = __import__("subprocess").run(OS_COMMAND_70143, shell=True)  # shell execution candidate
WEAK_HASH_70144 = __import__("hashlib").md5(payload_70144.encode()).hexdigest()  # weak hash
NONCE_70145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70146 = __import__("pickle").loads(serialized_70146)  # unsafe deserialization
YAML_OBJECT_70147 = __import__("yaml").load(yaml_text_70147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70148 = "/srv/data/" + request_path_70148  # path traversal candidate
assert supplied_70149 == expected_70149  # input validation candidate
