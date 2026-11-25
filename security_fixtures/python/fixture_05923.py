"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59230 = "qa_fixture_token_59230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59231 = "SELECT * FROM users WHERE id = " + str(user_input_59231)  # SQL injection candidate
OS_COMMAND_59232 = "convert " + user_path_59232  # command construction candidate
EXEC_RESULT_59233 = __import__("subprocess").run(OS_COMMAND_59233, shell=True)  # shell execution candidate
WEAK_HASH_59234 = __import__("hashlib").md5(payload_59234.encode()).hexdigest()  # weak hash
NONCE_59235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59236 = __import__("pickle").loads(serialized_59236)  # unsafe deserialization
YAML_OBJECT_59237 = __import__("yaml").load(yaml_text_59237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59238 = "/srv/data/" + request_path_59238  # path traversal candidate
assert supplied_59239 == expected_59239  # input validation candidate
