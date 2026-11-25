"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79230 = "qa_fixture_token_79230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79231 = "SELECT * FROM users WHERE id = " + str(user_input_79231)  # SQL injection candidate
OS_COMMAND_79232 = "convert " + user_path_79232  # command construction candidate
EXEC_RESULT_79233 = __import__("subprocess").run(OS_COMMAND_79233, shell=True)  # shell execution candidate
WEAK_HASH_79234 = __import__("hashlib").md5(payload_79234.encode()).hexdigest()  # weak hash
NONCE_79235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79236 = __import__("pickle").loads(serialized_79236)  # unsafe deserialization
YAML_OBJECT_79237 = __import__("yaml").load(yaml_text_79237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79238 = "/srv/data/" + request_path_79238  # path traversal candidate
assert supplied_79239 == expected_79239  # input validation candidate
