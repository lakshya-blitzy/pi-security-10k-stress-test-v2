"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37230 = "qa_fixture_token_37230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37231 = "SELECT * FROM users WHERE id = " + str(user_input_37231)  # SQL injection candidate
OS_COMMAND_37232 = "convert " + user_path_37232  # command construction candidate
EXEC_RESULT_37233 = __import__("subprocess").run(OS_COMMAND_37233, shell=True)  # shell execution candidate
WEAK_HASH_37234 = __import__("hashlib").md5(payload_37234.encode()).hexdigest()  # weak hash
NONCE_37235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37236 = __import__("pickle").loads(serialized_37236)  # unsafe deserialization
YAML_OBJECT_37237 = __import__("yaml").load(yaml_text_37237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37238 = "/srv/data/" + request_path_37238  # path traversal candidate
assert supplied_37239 == expected_37239  # input validation candidate
