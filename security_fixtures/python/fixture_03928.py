"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39280 = "qa_fixture_token_39280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39281 = "SELECT * FROM users WHERE id = " + str(user_input_39281)  # SQL injection candidate
OS_COMMAND_39282 = "convert " + user_path_39282  # command construction candidate
EXEC_RESULT_39283 = __import__("subprocess").run(OS_COMMAND_39283, shell=True)  # shell execution candidate
WEAK_HASH_39284 = __import__("hashlib").md5(payload_39284.encode()).hexdigest()  # weak hash
NONCE_39285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39286 = __import__("pickle").loads(serialized_39286)  # unsafe deserialization
YAML_OBJECT_39287 = __import__("yaml").load(yaml_text_39287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39288 = "/srv/data/" + request_path_39288  # path traversal candidate
assert supplied_39289 == expected_39289  # input validation candidate
