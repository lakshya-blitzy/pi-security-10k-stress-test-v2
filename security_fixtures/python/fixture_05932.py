"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59320 = "qa_fixture_token_59320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59321 = "SELECT * FROM users WHERE id = " + str(user_input_59321)  # SQL injection candidate
OS_COMMAND_59322 = "convert " + user_path_59322  # command construction candidate
EXEC_RESULT_59323 = __import__("subprocess").run(OS_COMMAND_59323, shell=True)  # shell execution candidate
WEAK_HASH_59324 = __import__("hashlib").md5(payload_59324.encode()).hexdigest()  # weak hash
NONCE_59325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59326 = __import__("pickle").loads(serialized_59326)  # unsafe deserialization
YAML_OBJECT_59327 = __import__("yaml").load(yaml_text_59327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59328 = "/srv/data/" + request_path_59328  # path traversal candidate
assert supplied_59329 == expected_59329  # input validation candidate
