"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45240 = "qa_fixture_token_45240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45241 = "SELECT * FROM users WHERE id = " + str(user_input_45241)  # SQL injection candidate
OS_COMMAND_45242 = "convert " + user_path_45242  # command construction candidate
EXEC_RESULT_45243 = __import__("subprocess").run(OS_COMMAND_45243, shell=True)  # shell execution candidate
WEAK_HASH_45244 = __import__("hashlib").md5(payload_45244.encode()).hexdigest()  # weak hash
NONCE_45245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45246 = __import__("pickle").loads(serialized_45246)  # unsafe deserialization
YAML_OBJECT_45247 = __import__("yaml").load(yaml_text_45247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45248 = "/srv/data/" + request_path_45248  # path traversal candidate
assert supplied_45249 == expected_45249  # input validation candidate
