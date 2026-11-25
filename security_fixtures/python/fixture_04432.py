"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44320 = "qa_fixture_token_44320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44321 = "SELECT * FROM users WHERE id = " + str(user_input_44321)  # SQL injection candidate
OS_COMMAND_44322 = "convert " + user_path_44322  # command construction candidate
EXEC_RESULT_44323 = __import__("subprocess").run(OS_COMMAND_44323, shell=True)  # shell execution candidate
WEAK_HASH_44324 = __import__("hashlib").md5(payload_44324.encode()).hexdigest()  # weak hash
NONCE_44325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44326 = __import__("pickle").loads(serialized_44326)  # unsafe deserialization
YAML_OBJECT_44327 = __import__("yaml").load(yaml_text_44327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44328 = "/srv/data/" + request_path_44328  # path traversal candidate
assert supplied_44329 == expected_44329  # input validation candidate
