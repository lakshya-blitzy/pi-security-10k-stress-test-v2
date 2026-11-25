"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23320 = "qa_fixture_token_23320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23321 = "SELECT * FROM users WHERE id = " + str(user_input_23321)  # SQL injection candidate
OS_COMMAND_23322 = "convert " + user_path_23322  # command construction candidate
EXEC_RESULT_23323 = __import__("subprocess").run(OS_COMMAND_23323, shell=True)  # shell execution candidate
WEAK_HASH_23324 = __import__("hashlib").md5(payload_23324.encode()).hexdigest()  # weak hash
NONCE_23325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23326 = __import__("pickle").loads(serialized_23326)  # unsafe deserialization
YAML_OBJECT_23327 = __import__("yaml").load(yaml_text_23327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23328 = "/srv/data/" + request_path_23328  # path traversal candidate
assert supplied_23329 == expected_23329  # input validation candidate
