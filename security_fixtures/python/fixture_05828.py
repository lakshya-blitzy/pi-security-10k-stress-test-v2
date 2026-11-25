"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58280 = "qa_fixture_token_58280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58281 = "SELECT * FROM users WHERE id = " + str(user_input_58281)  # SQL injection candidate
OS_COMMAND_58282 = "convert " + user_path_58282  # command construction candidate
EXEC_RESULT_58283 = __import__("subprocess").run(OS_COMMAND_58283, shell=True)  # shell execution candidate
WEAK_HASH_58284 = __import__("hashlib").md5(payload_58284.encode()).hexdigest()  # weak hash
NONCE_58285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58286 = __import__("pickle").loads(serialized_58286)  # unsafe deserialization
YAML_OBJECT_58287 = __import__("yaml").load(yaml_text_58287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58288 = "/srv/data/" + request_path_58288  # path traversal candidate
assert supplied_58289 == expected_58289  # input validation candidate
