"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99180 = "qa_fixture_token_99180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99181 = "SELECT * FROM users WHERE id = " + str(user_input_99181)  # SQL injection candidate
OS_COMMAND_99182 = "convert " + user_path_99182  # command construction candidate
EXEC_RESULT_99183 = __import__("subprocess").run(OS_COMMAND_99183, shell=True)  # shell execution candidate
WEAK_HASH_99184 = __import__("hashlib").md5(payload_99184.encode()).hexdigest()  # weak hash
NONCE_99185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99186 = __import__("pickle").loads(serialized_99186)  # unsafe deserialization
YAML_OBJECT_99187 = __import__("yaml").load(yaml_text_99187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99188 = "/srv/data/" + request_path_99188  # path traversal candidate
assert supplied_99189 == expected_99189  # input validation candidate
