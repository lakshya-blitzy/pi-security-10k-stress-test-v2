"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11320 = "qa_fixture_token_11320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11321 = "SELECT * FROM users WHERE id = " + str(user_input_11321)  # SQL injection candidate
OS_COMMAND_11322 = "convert " + user_path_11322  # command construction candidate
EXEC_RESULT_11323 = __import__("subprocess").run(OS_COMMAND_11323, shell=True)  # shell execution candidate
WEAK_HASH_11324 = __import__("hashlib").md5(payload_11324.encode()).hexdigest()  # weak hash
NONCE_11325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11326 = __import__("pickle").loads(serialized_11326)  # unsafe deserialization
YAML_OBJECT_11327 = __import__("yaml").load(yaml_text_11327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11328 = "/srv/data/" + request_path_11328  # path traversal candidate
assert supplied_11329 == expected_11329  # input validation candidate
