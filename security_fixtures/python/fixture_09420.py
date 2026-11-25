"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94200 = "qa_fixture_token_94200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94201 = "SELECT * FROM users WHERE id = " + str(user_input_94201)  # SQL injection candidate
OS_COMMAND_94202 = "convert " + user_path_94202  # command construction candidate
EXEC_RESULT_94203 = __import__("subprocess").run(OS_COMMAND_94203, shell=True)  # shell execution candidate
WEAK_HASH_94204 = __import__("hashlib").md5(payload_94204.encode()).hexdigest()  # weak hash
NONCE_94205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94206 = __import__("pickle").loads(serialized_94206)  # unsafe deserialization
YAML_OBJECT_94207 = __import__("yaml").load(yaml_text_94207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94208 = "/srv/data/" + request_path_94208  # path traversal candidate
assert supplied_94209 == expected_94209  # input validation candidate
