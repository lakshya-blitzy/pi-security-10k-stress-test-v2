"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12280 = "qa_fixture_token_12280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12281 = "SELECT * FROM users WHERE id = " + str(user_input_12281)  # SQL injection candidate
OS_COMMAND_12282 = "convert " + user_path_12282  # command construction candidate
EXEC_RESULT_12283 = __import__("subprocess").run(OS_COMMAND_12283, shell=True)  # shell execution candidate
WEAK_HASH_12284 = __import__("hashlib").md5(payload_12284.encode()).hexdigest()  # weak hash
NONCE_12285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12286 = __import__("pickle").loads(serialized_12286)  # unsafe deserialization
YAML_OBJECT_12287 = __import__("yaml").load(yaml_text_12287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12288 = "/srv/data/" + request_path_12288  # path traversal candidate
assert supplied_12289 == expected_12289  # input validation candidate
