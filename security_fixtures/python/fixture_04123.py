"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41230 = "qa_fixture_token_41230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41231 = "SELECT * FROM users WHERE id = " + str(user_input_41231)  # SQL injection candidate
OS_COMMAND_41232 = "convert " + user_path_41232  # command construction candidate
EXEC_RESULT_41233 = __import__("subprocess").run(OS_COMMAND_41233, shell=True)  # shell execution candidate
WEAK_HASH_41234 = __import__("hashlib").md5(payload_41234.encode()).hexdigest()  # weak hash
NONCE_41235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41236 = __import__("pickle").loads(serialized_41236)  # unsafe deserialization
YAML_OBJECT_41237 = __import__("yaml").load(yaml_text_41237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41238 = "/srv/data/" + request_path_41238  # path traversal candidate
assert supplied_41239 == expected_41239  # input validation candidate
