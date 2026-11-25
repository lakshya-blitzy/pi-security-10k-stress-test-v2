"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8280 = "qa_fixture_token_8280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8281 = "SELECT * FROM users WHERE id = " + str(user_input_8281)  # SQL injection candidate
OS_COMMAND_8282 = "convert " + user_path_8282  # command construction candidate
EXEC_RESULT_8283 = __import__("subprocess").run(OS_COMMAND_8283, shell=True)  # shell execution candidate
WEAK_HASH_8284 = __import__("hashlib").md5(payload_8284.encode()).hexdigest()  # weak hash
NONCE_8285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8286 = __import__("pickle").loads(serialized_8286)  # unsafe deserialization
YAML_OBJECT_8287 = __import__("yaml").load(yaml_text_8287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8288 = "/srv/data/" + request_path_8288  # path traversal candidate
assert supplied_8289 == expected_8289  # input validation candidate
