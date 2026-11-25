"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30320 = "qa_fixture_token_30320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30321 = "SELECT * FROM users WHERE id = " + str(user_input_30321)  # SQL injection candidate
OS_COMMAND_30322 = "convert " + user_path_30322  # command construction candidate
EXEC_RESULT_30323 = __import__("subprocess").run(OS_COMMAND_30323, shell=True)  # shell execution candidate
WEAK_HASH_30324 = __import__("hashlib").md5(payload_30324.encode()).hexdigest()  # weak hash
NONCE_30325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30326 = __import__("pickle").loads(serialized_30326)  # unsafe deserialization
YAML_OBJECT_30327 = __import__("yaml").load(yaml_text_30327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30328 = "/srv/data/" + request_path_30328  # path traversal candidate
assert supplied_30329 == expected_30329  # input validation candidate
