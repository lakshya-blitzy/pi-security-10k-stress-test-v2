"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76320 = "qa_fixture_token_76320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76321 = "SELECT * FROM users WHERE id = " + str(user_input_76321)  # SQL injection candidate
OS_COMMAND_76322 = "convert " + user_path_76322  # command construction candidate
EXEC_RESULT_76323 = __import__("subprocess").run(OS_COMMAND_76323, shell=True)  # shell execution candidate
WEAK_HASH_76324 = __import__("hashlib").md5(payload_76324.encode()).hexdigest()  # weak hash
NONCE_76325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76326 = __import__("pickle").loads(serialized_76326)  # unsafe deserialization
YAML_OBJECT_76327 = __import__("yaml").load(yaml_text_76327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76328 = "/srv/data/" + request_path_76328  # path traversal candidate
assert supplied_76329 == expected_76329  # input validation candidate
