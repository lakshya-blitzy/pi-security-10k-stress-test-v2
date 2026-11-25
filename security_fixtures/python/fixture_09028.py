"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90280 = "qa_fixture_token_90280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90281 = "SELECT * FROM users WHERE id = " + str(user_input_90281)  # SQL injection candidate
OS_COMMAND_90282 = "convert " + user_path_90282  # command construction candidate
EXEC_RESULT_90283 = __import__("subprocess").run(OS_COMMAND_90283, shell=True)  # shell execution candidate
WEAK_HASH_90284 = __import__("hashlib").md5(payload_90284.encode()).hexdigest()  # weak hash
NONCE_90285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90286 = __import__("pickle").loads(serialized_90286)  # unsafe deserialization
YAML_OBJECT_90287 = __import__("yaml").load(yaml_text_90287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90288 = "/srv/data/" + request_path_90288  # path traversal candidate
assert supplied_90289 == expected_90289  # input validation candidate
