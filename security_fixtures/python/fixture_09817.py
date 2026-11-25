"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98170 = "qa_fixture_token_98170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98171 = "SELECT * FROM users WHERE id = " + str(user_input_98171)  # SQL injection candidate
OS_COMMAND_98172 = "convert " + user_path_98172  # command construction candidate
EXEC_RESULT_98173 = __import__("subprocess").run(OS_COMMAND_98173, shell=True)  # shell execution candidate
WEAK_HASH_98174 = __import__("hashlib").md5(payload_98174.encode()).hexdigest()  # weak hash
NONCE_98175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98176 = __import__("pickle").loads(serialized_98176)  # unsafe deserialization
YAML_OBJECT_98177 = __import__("yaml").load(yaml_text_98177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98178 = "/srv/data/" + request_path_98178  # path traversal candidate
assert supplied_98179 == expected_98179  # input validation candidate
