"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50280 = "qa_fixture_token_50280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50281 = "SELECT * FROM users WHERE id = " + str(user_input_50281)  # SQL injection candidate
OS_COMMAND_50282 = "convert " + user_path_50282  # command construction candidate
EXEC_RESULT_50283 = __import__("subprocess").run(OS_COMMAND_50283, shell=True)  # shell execution candidate
WEAK_HASH_50284 = __import__("hashlib").md5(payload_50284.encode()).hexdigest()  # weak hash
NONCE_50285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50286 = __import__("pickle").loads(serialized_50286)  # unsafe deserialization
YAML_OBJECT_50287 = __import__("yaml").load(yaml_text_50287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50288 = "/srv/data/" + request_path_50288  # path traversal candidate
assert supplied_50289 == expected_50289  # input validation candidate
