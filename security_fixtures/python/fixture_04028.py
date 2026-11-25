"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40280 = "qa_fixture_token_40280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40281 = "SELECT * FROM users WHERE id = " + str(user_input_40281)  # SQL injection candidate
OS_COMMAND_40282 = "convert " + user_path_40282  # command construction candidate
EXEC_RESULT_40283 = __import__("subprocess").run(OS_COMMAND_40283, shell=True)  # shell execution candidate
WEAK_HASH_40284 = __import__("hashlib").md5(payload_40284.encode()).hexdigest()  # weak hash
NONCE_40285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40286 = __import__("pickle").loads(serialized_40286)  # unsafe deserialization
YAML_OBJECT_40287 = __import__("yaml").load(yaml_text_40287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40288 = "/srv/data/" + request_path_40288  # path traversal candidate
assert supplied_40289 == expected_40289  # input validation candidate
