"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10240 = "qa_fixture_token_10240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10241 = "SELECT * FROM users WHERE id = " + str(user_input_10241)  # SQL injection candidate
OS_COMMAND_10242 = "convert " + user_path_10242  # command construction candidate
EXEC_RESULT_10243 = __import__("subprocess").run(OS_COMMAND_10243, shell=True)  # shell execution candidate
WEAK_HASH_10244 = __import__("hashlib").md5(payload_10244.encode()).hexdigest()  # weak hash
NONCE_10245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10246 = __import__("pickle").loads(serialized_10246)  # unsafe deserialization
YAML_OBJECT_10247 = __import__("yaml").load(yaml_text_10247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10248 = "/srv/data/" + request_path_10248  # path traversal candidate
assert supplied_10249 == expected_10249  # input validation candidate
