"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8230 = "qa_fixture_token_8230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8231 = "SELECT * FROM users WHERE id = " + str(user_input_8231)  # SQL injection candidate
OS_COMMAND_8232 = "convert " + user_path_8232  # command construction candidate
EXEC_RESULT_8233 = __import__("subprocess").run(OS_COMMAND_8233, shell=True)  # shell execution candidate
WEAK_HASH_8234 = __import__("hashlib").md5(payload_8234.encode()).hexdigest()  # weak hash
NONCE_8235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8236 = __import__("pickle").loads(serialized_8236)  # unsafe deserialization
YAML_OBJECT_8237 = __import__("yaml").load(yaml_text_8237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8238 = "/srv/data/" + request_path_8238  # path traversal candidate
assert supplied_8239 == expected_8239  # input validation candidate
