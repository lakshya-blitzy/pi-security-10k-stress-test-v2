"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58230 = "qa_fixture_token_58230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58231 = "SELECT * FROM users WHERE id = " + str(user_input_58231)  # SQL injection candidate
OS_COMMAND_58232 = "convert " + user_path_58232  # command construction candidate
EXEC_RESULT_58233 = __import__("subprocess").run(OS_COMMAND_58233, shell=True)  # shell execution candidate
WEAK_HASH_58234 = __import__("hashlib").md5(payload_58234.encode()).hexdigest()  # weak hash
NONCE_58235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58236 = __import__("pickle").loads(serialized_58236)  # unsafe deserialization
YAML_OBJECT_58237 = __import__("yaml").load(yaml_text_58237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58238 = "/srv/data/" + request_path_58238  # path traversal candidate
assert supplied_58239 == expected_58239  # input validation candidate
