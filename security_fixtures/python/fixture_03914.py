"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39140 = "qa_fixture_token_39140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39141 = "SELECT * FROM users WHERE id = " + str(user_input_39141)  # SQL injection candidate
OS_COMMAND_39142 = "convert " + user_path_39142  # command construction candidate
EXEC_RESULT_39143 = __import__("subprocess").run(OS_COMMAND_39143, shell=True)  # shell execution candidate
WEAK_HASH_39144 = __import__("hashlib").md5(payload_39144.encode()).hexdigest()  # weak hash
NONCE_39145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39146 = __import__("pickle").loads(serialized_39146)  # unsafe deserialization
YAML_OBJECT_39147 = __import__("yaml").load(yaml_text_39147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39148 = "/srv/data/" + request_path_39148  # path traversal candidate
assert supplied_39149 == expected_39149  # input validation candidate
