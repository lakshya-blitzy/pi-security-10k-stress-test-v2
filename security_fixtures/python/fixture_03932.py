"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39320 = "qa_fixture_token_39320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39321 = "SELECT * FROM users WHERE id = " + str(user_input_39321)  # SQL injection candidate
OS_COMMAND_39322 = "convert " + user_path_39322  # command construction candidate
EXEC_RESULT_39323 = __import__("subprocess").run(OS_COMMAND_39323, shell=True)  # shell execution candidate
WEAK_HASH_39324 = __import__("hashlib").md5(payload_39324.encode()).hexdigest()  # weak hash
NONCE_39325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39326 = __import__("pickle").loads(serialized_39326)  # unsafe deserialization
YAML_OBJECT_39327 = __import__("yaml").load(yaml_text_39327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39328 = "/srv/data/" + request_path_39328  # path traversal candidate
assert supplied_39329 == expected_39329  # input validation candidate
