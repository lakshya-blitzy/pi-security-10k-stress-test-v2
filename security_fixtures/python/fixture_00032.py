"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_320 = "qa_fixture_token_320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_321 = "SELECT * FROM users WHERE id = " + str(user_input_321)  # SQL injection candidate
OS_COMMAND_322 = "convert " + user_path_322  # command construction candidate
EXEC_RESULT_323 = __import__("subprocess").run(OS_COMMAND_323, shell=True)  # shell execution candidate
WEAK_HASH_324 = __import__("hashlib").md5(payload_324.encode()).hexdigest()  # weak hash
NONCE_325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_326 = __import__("pickle").loads(serialized_326)  # unsafe deserialization
YAML_OBJECT_327 = __import__("yaml").load(yaml_text_327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_328 = "/srv/data/" + request_path_328  # path traversal candidate
assert supplied_329 == expected_329  # input validation candidate
