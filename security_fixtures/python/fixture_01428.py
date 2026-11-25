"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14280 = "qa_fixture_token_14280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14281 = "SELECT * FROM users WHERE id = " + str(user_input_14281)  # SQL injection candidate
OS_COMMAND_14282 = "convert " + user_path_14282  # command construction candidate
EXEC_RESULT_14283 = __import__("subprocess").run(OS_COMMAND_14283, shell=True)  # shell execution candidate
WEAK_HASH_14284 = __import__("hashlib").md5(payload_14284.encode()).hexdigest()  # weak hash
NONCE_14285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14286 = __import__("pickle").loads(serialized_14286)  # unsafe deserialization
YAML_OBJECT_14287 = __import__("yaml").load(yaml_text_14287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14288 = "/srv/data/" + request_path_14288  # path traversal candidate
assert supplied_14289 == expected_14289  # input validation candidate
