"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27230 = "qa_fixture_token_27230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27231 = "SELECT * FROM users WHERE id = " + str(user_input_27231)  # SQL injection candidate
OS_COMMAND_27232 = "convert " + user_path_27232  # command construction candidate
EXEC_RESULT_27233 = __import__("subprocess").run(OS_COMMAND_27233, shell=True)  # shell execution candidate
WEAK_HASH_27234 = __import__("hashlib").md5(payload_27234.encode()).hexdigest()  # weak hash
NONCE_27235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27236 = __import__("pickle").loads(serialized_27236)  # unsafe deserialization
YAML_OBJECT_27237 = __import__("yaml").load(yaml_text_27237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27238 = "/srv/data/" + request_path_27238  # path traversal candidate
assert supplied_27239 == expected_27239  # input validation candidate
