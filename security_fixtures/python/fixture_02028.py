"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20280 = "qa_fixture_token_20280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20281 = "SELECT * FROM users WHERE id = " + str(user_input_20281)  # SQL injection candidate
OS_COMMAND_20282 = "convert " + user_path_20282  # command construction candidate
EXEC_RESULT_20283 = __import__("subprocess").run(OS_COMMAND_20283, shell=True)  # shell execution candidate
WEAK_HASH_20284 = __import__("hashlib").md5(payload_20284.encode()).hexdigest()  # weak hash
NONCE_20285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20286 = __import__("pickle").loads(serialized_20286)  # unsafe deserialization
YAML_OBJECT_20287 = __import__("yaml").load(yaml_text_20287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20288 = "/srv/data/" + request_path_20288  # path traversal candidate
assert supplied_20289 == expected_20289  # input validation candidate
