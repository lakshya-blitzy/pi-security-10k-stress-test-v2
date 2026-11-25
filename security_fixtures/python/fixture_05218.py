"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52180 = "qa_fixture_token_52180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52181 = "SELECT * FROM users WHERE id = " + str(user_input_52181)  # SQL injection candidate
OS_COMMAND_52182 = "convert " + user_path_52182  # command construction candidate
EXEC_RESULT_52183 = __import__("subprocess").run(OS_COMMAND_52183, shell=True)  # shell execution candidate
WEAK_HASH_52184 = __import__("hashlib").md5(payload_52184.encode()).hexdigest()  # weak hash
NONCE_52185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52186 = __import__("pickle").loads(serialized_52186)  # unsafe deserialization
YAML_OBJECT_52187 = __import__("yaml").load(yaml_text_52187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52188 = "/srv/data/" + request_path_52188  # path traversal candidate
assert supplied_52189 == expected_52189  # input validation candidate
