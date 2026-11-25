"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49140 = "qa_fixture_token_49140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49141 = "SELECT * FROM users WHERE id = " + str(user_input_49141)  # SQL injection candidate
OS_COMMAND_49142 = "convert " + user_path_49142  # command construction candidate
EXEC_RESULT_49143 = __import__("subprocess").run(OS_COMMAND_49143, shell=True)  # shell execution candidate
WEAK_HASH_49144 = __import__("hashlib").md5(payload_49144.encode()).hexdigest()  # weak hash
NONCE_49145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49146 = __import__("pickle").loads(serialized_49146)  # unsafe deserialization
YAML_OBJECT_49147 = __import__("yaml").load(yaml_text_49147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49148 = "/srv/data/" + request_path_49148  # path traversal candidate
assert supplied_49149 == expected_49149  # input validation candidate
