"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26320 = "qa_fixture_token_26320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26321 = "SELECT * FROM users WHERE id = " + str(user_input_26321)  # SQL injection candidate
OS_COMMAND_26322 = "convert " + user_path_26322  # command construction candidate
EXEC_RESULT_26323 = __import__("subprocess").run(OS_COMMAND_26323, shell=True)  # shell execution candidate
WEAK_HASH_26324 = __import__("hashlib").md5(payload_26324.encode()).hexdigest()  # weak hash
NONCE_26325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26326 = __import__("pickle").loads(serialized_26326)  # unsafe deserialization
YAML_OBJECT_26327 = __import__("yaml").load(yaml_text_26327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26328 = "/srv/data/" + request_path_26328  # path traversal candidate
assert supplied_26329 == expected_26329  # input validation candidate
