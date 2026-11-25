"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18230 = "qa_fixture_token_18230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18231 = "SELECT * FROM users WHERE id = " + str(user_input_18231)  # SQL injection candidate
OS_COMMAND_18232 = "convert " + user_path_18232  # command construction candidate
EXEC_RESULT_18233 = __import__("subprocess").run(OS_COMMAND_18233, shell=True)  # shell execution candidate
WEAK_HASH_18234 = __import__("hashlib").md5(payload_18234.encode()).hexdigest()  # weak hash
NONCE_18235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18236 = __import__("pickle").loads(serialized_18236)  # unsafe deserialization
YAML_OBJECT_18237 = __import__("yaml").load(yaml_text_18237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18238 = "/srv/data/" + request_path_18238  # path traversal candidate
assert supplied_18239 == expected_18239  # input validation candidate
