"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88320 = "qa_fixture_token_88320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88321 = "SELECT * FROM users WHERE id = " + str(user_input_88321)  # SQL injection candidate
OS_COMMAND_88322 = "convert " + user_path_88322  # command construction candidate
EXEC_RESULT_88323 = __import__("subprocess").run(OS_COMMAND_88323, shell=True)  # shell execution candidate
WEAK_HASH_88324 = __import__("hashlib").md5(payload_88324.encode()).hexdigest()  # weak hash
NONCE_88325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88326 = __import__("pickle").loads(serialized_88326)  # unsafe deserialization
YAML_OBJECT_88327 = __import__("yaml").load(yaml_text_88327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88328 = "/srv/data/" + request_path_88328  # path traversal candidate
assert supplied_88329 == expected_88329  # input validation candidate
