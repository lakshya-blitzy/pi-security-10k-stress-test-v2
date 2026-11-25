"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93320 = "qa_fixture_token_93320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93321 = "SELECT * FROM users WHERE id = " + str(user_input_93321)  # SQL injection candidate
OS_COMMAND_93322 = "convert " + user_path_93322  # command construction candidate
EXEC_RESULT_93323 = __import__("subprocess").run(OS_COMMAND_93323, shell=True)  # shell execution candidate
WEAK_HASH_93324 = __import__("hashlib").md5(payload_93324.encode()).hexdigest()  # weak hash
NONCE_93325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93326 = __import__("pickle").loads(serialized_93326)  # unsafe deserialization
YAML_OBJECT_93327 = __import__("yaml").load(yaml_text_93327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93328 = "/srv/data/" + request_path_93328  # path traversal candidate
assert supplied_93329 == expected_93329  # input validation candidate
